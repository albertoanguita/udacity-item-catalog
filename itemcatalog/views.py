###############################################################################
# This module defines the application endpoints and main logic                #
#                                                                             #
# The application counts with 6 main pages and 1 user login page.             #
#                                                                             #
# Main pages:                                                                 #
# - home.html: the initial page, showing all genres and the latest games.     #
#              Has public and private versions                                #
#    + path: '/' or '/catalog'                                                #
#    + endpoint: all_genres                                                   #
# - newGame.html: page for adding new games to the application                #
#    + path: '/catalog/new'                                                   #
#    + endpoint: add_game                                                     #
# - genre.html: displays the information about a specific genre               #
#    + path: '/catalog/<string:genre_name>/games'                             #
#    + endpoint: game_genres                                                  #
# - game.html: shows the information of a specific game. Has public and       #
#              private versions                                               #
#    + path: '/catalog/<string:genre_name>/games/<string:game_title>'         #
#    + endpoint: game_info                                                    #
# - editGame.html: shows a form for editing an existing game                  #
#    + path: '/catalog/<string:genre_name>/games/<string:game_title>/edit'    #
#    + endpoint: edit_game                                                    #
# - deleteGame.html: allows deleting an existing game                         #
#    + path: '/catalog/<string:genre_name>/games/<string:game_title>/delete'  #
#    + endpoint: delete_game                                                  #
#                                                                             #
# User connection pages:                                                      #
# - login.html: shows a button for logging with a google account              #
#    + path; '/login'                                                         #
#    + endpoint: show_login()                                                 #
#                                                                             #
# There are 2 additional endpoints (for logging in and logging out):          #
# - google_connect(): implements the OAuth flow with google                   #
# - disconnect: logs out a connected user                                     #
###############################################################################

from flask import render_template, request, redirect, url_for, flash, jsonify
from flask import abort, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from itemcatalog import app
from database_setup import Base, Genre, Game
import _elementtree as et
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
import json, random, string, httplib2, requests
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError


# load the security information for the google oauth functionality
CLIENT_ID = json.loads(
    open('itemcatalog/client_secrets.json', 'r').read())['web']['client_id']
# APPLICATION_NAME = "My Game Catalog"


# load the database and define the session for working with it
engine = create_engine('sqlite:///game_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#####################################
# Application endpoints             #
#####################################


# display the home page, that shows all registered game genres and the
# latest games (by release date)
# Although the page is not restricted to unlogged users, there is a public
# version of the page that does not offer adding new games
@app.route('/')
@app.route('/catalog')
def all_genres():
    genres = session.query(Genre).all()
    latest_games = session.query(Game). \
        order_by(Game.releaseDate.desc()). \
        limit(10).all()
    # only logged users will see the home.html, containing the link for
    # adding new games
    if 'username' not in login_session:
        return render_template('homePublic.html', genres=genres,
                               latest_games=latest_games,
                               get_genre_name=get_genre_name)
    else:
        return render_template('home.html', genres=genres,
                               latest_games=latest_games,
                               get_genre_name=get_genre_name)


# Display the login page, issuing the user to log through google's sign it
@app.route('/login')
def show_login():
    # Create anti-forgery state token
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/google_connect', methods=['POST'])
def google_connect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('itemcatalog/client_secrets.json',
                                             scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = \
            make_response(json.dumps('Current user is already connected.'),
                          200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    flash("you are now logged in as %s" % login_session['username'])
    return output


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'username' in login_session:
        google_disconnect()
        del login_session['gplus_id']
        del login_session['credentials']
        del login_session['username']
        flash("You have successfully been logged out.")
        return redirect(url_for('all_genres'))
    else:
        flash("You were not logged in")
        return redirect(url_for('all_genres'))


# form for adding a new game, accepting both GET and POST petitions
# this page is not available to unlogged users
@app.route('/catalog/new', methods=['GET', 'POST'])
def add_game():
    # check users login status. If not logged, redirect to login page
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        # POST requests include all data for the new game. This data is
        # processed and a new game is added to the database
        release_date = datetime.strptime(request.form['releaseDate'],
                                         "%Y-%m-%d").date()
        new_game = Game(title=request.form['title'],
                        description=request.form['description'],
                        releaseDate=release_date,
                        pictureURL=request.form['pictureURL'],
                        genre_id=get_genre_id(request.form['genre']))
        session.add(new_game)
        session.commit()
        flash("New game added!")
        return redirect(url_for('all_genres'))
    else:
        # GET request render the form for inputting the new game data
        genres = session.query(Genre).all()
        return render_template('newGame.html', genres=genres)


# page with the list of games of a specific genre
# no user login status is performed, as it is considered that unregistered
# users are allowed to visit this page without restrictions
@app.route('/catalog/<string:genre_name>/games')
def genre_games(genre_name):
    genres = session.query(Genre).all()
    genre = None
    try:
        genre = session.query(Genre).filter_by(name=genre_name).one()
    except NoResultFound:
        abort(404)
    games = session.query(Game).filter_by(genre_id=genre.id).all()
    return render_template('genre.html', genres=genres, genre_name=genre_name,
                           game_list=games, get_genre_name=get_genre_name)


# page for a specific game, where its details are shown to the user
# all users can visit this page
@app.route('/catalog/<string:genre_name>/games/<string:game_title>')
def game_info(genre_name, game_title):
    game = None
    try:
        game = session.query(Game).filter_by(title=game_title).one()
    except NoResultFound:
        abort(404)
    # only logged users have the possibility to edit or delete the game,
    # so a public version of the page is presented to unlogged users
    if 'username' not in login_session:
        return render_template('gamePublic.html',
                               game=game, genre_name=genre_name)
    else:
        return render_template('game.html', game=game, genre_name=genre_name)


# page for editing a game
# only logged users can see this page
@app.route('/catalog/<string:genre_name>/games/<string:game_title>/edit',
           methods=['GET', 'POST'])
def edit_game(genre_name, game_title):
    # check users login status. If not logged, redirect to login page
    if 'username' not in login_session:
        return redirect('/login')
    game = None
    if request.method == 'POST':
        # POST request include the information provided by the user. This
        # information is processed, and the edited game is properly updated
        try:
            game = session.query(Game).filter_by(title=game_title).one()
        except NoResultFound:
            abort(404)
        game.title = request.form['title']
        game.description = request.form['description']
        game.releaseDate = datetime.strptime(request.form['releaseDate'],
                                             "%Y-%m-%d").date()
        game.pictureURL = request.form['pictureURL']
        game.genre_id = get_genre_id(request.form['genre'])
        session.add(game)
        session.commit()
        flash("Game successfully edited!")
        return redirect(url_for('game_info',
                                genre_name=genre_name, game_title=game.title))
    else:
        # show the edit game form to the user
        genres = session.query(Genre).all()
        game = session.query(Game).filter_by(title=game_title).one()
        return render_template('editGame.html', genres=genres,
                               genre_name=genre_name, game=game,
                               get_genre_name=get_genre_name)


# page for deleting an existing game
# only logged users can see this page
@app.route('/catalog/<string:genre_name>/games/<string:game_title>/delete',
           methods=['GET', 'POST'])
def delete_game(genre_name, game_title):
    # check users login status. If not logged, redirect to login page
    if 'username' not in login_session:
        return redirect('/login')
    game = None
    if request.method == 'POST':
        # POST requests are processed to actually delete the game. Game is
        # searched in the database and properly deleted
        try:
            game = session.query(Game).filter_by(title=game_title).one()
        except NoResultFound:
            abort(404)
        session.delete(game)
        session.commit()
        flash("Game successfully deleted!")
        return redirect(url_for('all_genres'))
    else:
        # show the delete game page to the user
        game = session.query(Game).filter_by(title=game_title).one()
        return render_template('deleteGame.html',
                               genre_name=genre_name,
                               game=game)


###############################################
# API endpoints                               #
# Includes endpoints for JSON and XML         #
###############################################


# JSON endpoint for retrieving information about all available genres
@app.route('/catalog.json')
def all_genres_json():
    genres = session.query(Genre).all()
    return jsonify(genres=[i.serialize for i in genres])


# JSON endpoint for retrieving information about all games of a specific genre
@app.route('/catalog/<string:genre_name>/games.json')
def genre_games_json(genre_name):
    genre = session.query(Genre).filter_by(name=genre_name).one()
    games = session.query(Game).filter_by(genre_id=genre.id).all()
    return jsonify(games=[i.serialize for i in games])


# JSON endpoint for retrieving information about a specific game
@app.route('/catalog/<string:genre_name>/games/<string:game_title>.json')
def game_info_json(genre_name, game_title):
    game = session.query(Game).filter_by(title=game_title).one()
    return jsonify(game.serialize)


# XML endpoint for retrieving information about all available genres
@app.route('/catalog.xml')
def all_genres_xml():
    genres = session.query(Genre).all()
    genres_elements = [i.serializeXML for i in genres]
    root = et.Element('genres')
    for genre in genres_elements:
        root.append(genre)
    return app.response_class(et.tostring(root), mimetype='application/xml')


# XML endpoint for retrieving information about all games of a specific genre
@app.route('/catalog/<string:genre_name>/games.xml')
def genre_games_xml(genre_name):
    genre = session.query(Genre).filter_by(name=genre_name).one()
    games = session.query(Game).filter_by(genre_id=genre.id).all()
    games_elements = [i.serializeXML for i in games]
    root = et.Element('games')
    for game in games_elements:
        root.append(game)
    return app.response_class(et.tostring(root), mimetype='application/xml')


# JSON endpoint for retrieving information about a specific game
@app.route('/catalog/<string:genre_name>/games/<string:game_title>.xml')
def game_info_xml(genre_name, game_title):
    game = session.query(Game).filter_by(title=game_title).one()
    return app.response_class(str(game.serializeXML),
                              mimetype='application/xml')


#############################
# ADDITIONAL HELPER METHODS #
#############################


def get_genre_name(genre_id):
    """Returns the genre name, given its id"""
    genre = session.query(Genre).filter_by(id=genre_id).one()
    return genre.name


def get_genre_id(genre_name):
    """Returns the genre id, given its name"""
    genre = session.query(Genre).filter_by(name=genre_name).one()
    return genre.id


def google_disconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('credentials')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response
