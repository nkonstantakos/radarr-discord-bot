from Application.Dao.Movies import MovieTable
from Application.Dao.Movies import MovieUpserts
from Application.Dao.PlexUsers import PlexUserTable
from Application.Dao.Votes import VoteTable
from Application.Domain.Movie import Movie
from Application.Domain.PlexUser import PlexUser
from Application.Dao.PlexUsers import PlexUserRetrievals
from Application.Dao.PlexUsers import PlexUserUpserts
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

    def get_all_users(self):
        connection = self.get_db_connection()
        existing_users = PlexUserRetrievals.get_users(connection)
        commit_and_close()
        return existing_users

    def insert_user(self, user):
        connection = self.get_db_connection()
        PlexUserUpserts.insert_user(connection, user)
        commit_and_close(connection)
        return self.get_user_by_discord_id(user.discord_id)

    def get_user_by_discord_id(self, discord_id):
        connection = self.get_db_connection()
        user = PlexUserRetrievals.get_user_by_discord_id(connection, discord_id)
        if len(user) > 0:
            return user[0]
        return None

    def insert_movie(self, movie):
        """
        @type movie: Movie
        @type user: PlexUser
        """
        connection = self.get_db_connection()
        MovieUpserts.insert_movie(connection, movie)
        commit_and_close(connection)

    def get_db_connection(self):
        return sqlite3.connect(self.db_name)


def commit_and_close(connection):
    connection.commit()
    connection.close()

