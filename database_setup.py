###############################################################################
# This module defines the structure of the database used in the application   #
#                                                                             #
# The database is formed by two tables: genre and game. The former stores     #
# game genres (i.e. "Adventure", "Strategy", etc), and the latter stores      #
# specific games that belong to one and only one of the previous categories.  #
###############################################################################

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import _elementtree as et


# base class from which the rest of classes in the database derive
Base = declarative_base()


class Genre(Base):
    """Defines the genre table in the database"""
    __tablename__ = 'genre'

    # identifier of the genre
    id = Column(Integer, primary_key=True)
    # name of the genre
    name = Column(String(250), nullable=False)

    # Serialization properties
    @property
    def serialize(self):
        """JSON serialization of a genre"""
        return {
            'id': self.id,
            'name': self.name,
        }

    # XML serializable format
    @property
    def serializeXML(self):
        """XML serialization of a genre"""
        genre = et.Element(self.__tablename__)
        id_element = et.SubElement(genre, 'id')
        id_element.text = str(self.id)
        name = et.SubElement(genre, 'name')
        name.text = self.name
        return genre


class Game(Base):
    """Defines the game table in the database"""
    __tablename__ = 'game'

    # identifier of the game
    id = Column(Integer, primary_key=True)
    # title of the game
    title = Column(String(250), nullable=False)
    # a description of the game
    description = Column(String(250), nullable=False)
    # date in which the game was released (allows ordering games by date)
    releaseDate = Column(Date, nullable=False)
    # URL of a game image (optional)
    pictureURL = Column(String(250))
    # identifier of the genre of the game
    genre_id = Column(Integer, ForeignKey('genre.id'))
    # relationship with its corresponding genre
    genre = relationship(Genre)

    # Serialization properties
    @property
    def serialize(self):
        """JSON serialization of a game"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'releaseDate': str(self.releaseDate),
            'pictureURL': self.pictureURL,
            'genre_id': self.genre_id,
        }

    # XML serializable format
    @property
    def serializeXML(self):
        """XML serialization of a game"""
        game = et.Element(self.__tablename__)
        id_element = et.SubElement(game, 'id')
        id_element.text = str(self.id)
        title = et.SubElement(game, 'title')
        title.text = self.title
        description = et.SubElement(game, 'description')
        description.text = self.description
        releaseDate = et.SubElement(game, 'releaseDate')
        releaseDate.text = str(self.releaseDate)
        pictureURL = et.SubElement(game, 'pictureURL')
        pictureURL.text = self.pictureURL
        genre_id = et.SubElement(game, 'genre_id')
        genre_id.text = str(self.genre_id)
        return game


# the database is created in the following path
engine = create_engine('sqlite:///game_catalog.db')
Base.metadata.create_all(engine)
