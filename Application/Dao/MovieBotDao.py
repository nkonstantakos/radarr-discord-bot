from Application.Dao.Movies import MovieTable
from Application.Dao.PlexUsers import PlexUserTable
from Application.Dao.PlexUsers import PlexUserRetrievals
from Application.Domain.Movie import Movie
import sqlite3


class MovieBotDao(object):

    def __init__(self, db_name):
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        connection = self.get_db_connection()
        MovieTable.create_movie_table(connection)
        PlexUserTable.create_user_table(connection)
        commit_and_close(connection)

    def insert_movie(self, movie):
        """
        @type movie: Movie
        """

    def get_db_connection(self):
        return sqlite3.connect(self.db_name)


def commit_and_close(connection):
    connection.commit()
    connection.close()

