from Application.Dao.Movies import MovieTable
from Application.Dao.PlexUsers import PlexUserTable
from Application.Dao.Votes import VoteTable
from Application.Domain.Movie import Movie
from Application.Domain.PlexUser import PlexUser
import sqlite3


class MovieBotDao(object):

    def __init__(self, db_name):
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        connection = self.get_db_connection()
        PlexUserTable.create_user_table(connection)
        MovieTable.create_movie_table(connection)
        PlexUserTable.create_user_table(connection)
        VoteTable.create_vote_table(connection)
        commit_and_close(connection)

    def insert_movie(self, movie, user):
        """
        @type movie: Movie
        @type user: PlexUser
        """
        # Get all users
        # See if exists
        # If not, add them
        # Construct movie object
        # Default to approved if admin or mod

    def get_db_connection(self):
        return sqlite3.connect(self.db_name)


def commit_and_close(connection):
    connection.commit()
    connection.close()

