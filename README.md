# Item Catalog - Full Stack Web Developer Nanodegree project


## Index of contents

1. General description
2. Running the application
3. Implemented features
4. Description of files 


## General description

The project implements a videogame catalog with different game genres and 
game descriptions belonging to those genres. The user can see the latest 
games (by release date) in the initial screen, click on a specific genre 
to see its games, or click in a game to see its detailed information.

The application implements google's authentication system, providing 
logged users the ability to add, edit and delete games.

The games' data is retrieved from an SQLite database located in 
game_catalog.db. This file is created with the script located in 
database_setup.py, and populated with database_populator.py.

All the information about the games was extracted from steam.com.


## Running the application

To run the application, clone the code to a computer with python 2.7.9 
installed, and execute:
 
`python.exe runserver.py <port>`

Where `<port>` shall be replaced by the port number where the server will run.

To open the application, go to `localhost:<port>` or `localhost:<port>/catalog` 
in any browser (it has been tested in firefox and chrome).

To quit it, press CTRL+C.


## Implemented features

The project implements all mandatory and all optional features:

* **CRUD operations**: users can read data about a game, edit its information, 
create new games, or delete existing ones. Games include an optional image, 
provided through a URL. The application will check if there is any value 
in this field before attempting to display it on the screen.

* **API endpoints**: users can retrieve both JSON and XML data for the main app 
functions.

* **Authentication & Authorization**: the app implements google's sign in system.
Logged users gain the ability to add, edit and delete games. There are public 
pages for unlogged users where necessary. Restricted pages are forbidden for 
unlogged users, even if they attempt to ented the URL directly in the browser.


##Description of files

The app contains one package (itemcatalog) that stores the main logic.

There are 5 files in the root:

* **database_setup.py**: script for building the structure of the SQLite database.
* **database_populator.py**: populates the database with genres and games.
* **game_catalog.db**: the database in its initial state (built, populated)
* **README.md**: this file.
* **runserver.py**: the file used to launch the application.

The itemcatalog contains additional files and directories:

* **/static/styles.css**: the style for the application
* **/templates**: contains the html templates for the application (see below)
*_**_init__.py**: script that initializes the application
* **client_secrets.json**: file containing authentication data for google's sign in
* **views.py**: contains all the endpoints of the application, and the main logic

The templates directory contains the following files:

* **deleteGame.html**: page for deleting an existing game. Unavailable to unlogged users.
* **editGame.html**: page for editing the information of a game. Unavailable to unlogged users.
* **game.html**: page that displays the information about a game (title, picture, description, release date). For logged users only.
* **gamePublic.html**: public version (for unlogged users) of the previous page. Omits the edit and delete links.
* **genre.html**: page that shows the games for a specific genre. Available to all users.
* **header.html**: piece of html code that shows the top bar, including the app name and login/logout links.
* **home.html**: initial app page, showing all genres and the latest games, and a link for adding a new game. For logged users only.
* **homePublic.html**: public version (for unlogged users) of the previous page. Omits the add game link.
* **login.html**: page for login through google's sign in. Once the user presses on the button and selects an account, he will be redirected to the initial page.
* **main.html**: html template that contains the main structure for all pages (header and main div).
* **messages.html**: html template that shows pending flask messages.
* **newGame.html**: page for adding a new game to the database.