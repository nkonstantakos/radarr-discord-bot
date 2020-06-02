from Application.Api.Dao.Movies import MovieTable, MovieUpserts, MovieRetrievals, MovieDTO
from Application.Api.Dao.Votes import VoteTable
from Application.Api.Domain.Movie import Movie
from Application.Api.Domain.PlexUser import PlexUser
from Application.Api.Dao.PlexUsers import PlexUserRetrievals, PlexUserTable, PlexUserUpserts
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
        connection.close()
        return existing_users

    def insert_user(self, user):
        connection = self.get_db_connection()
        PlexUserUpserts.insert_user(connection, user)
        commit_and_close(connection)
        return self.get_user_by_discord_id(user.discord_id)

    def get_user_by_discord_id(self, discord_id):
        connection = self.get_db_connection()
        user = PlexUserRetrievals.get_user_by_discord_id(connection, discord_id)
        connection.close()
        return get_first_record_or_return(user)

    def get_user_by_user_id(self, user_id):
        connection = self.get_db_connection()
        user = PlexUserRetrievals.get_user_by_user_id(connection, user_id)
        connection.close()
        return get_first_record_or_return(user)

    def insert_movie(self, movie: Movie):
        connection = self.get_db_connection()
        MovieUpserts.insert_movie(connection, movie)
        connection.commit()
        new_movie: Movie = self.get_movie(movie.imdb_id)
        connection.close()
        return new_movie

    def get_movie(self, imdb_id: str):
        connection = self.get_db_connection()
        movie: MovieDTO = MovieRetrievals.get_movie_by_imdb_id(connection, imdb_id)
        if movie is not None:
            user: PlexUser = self.get_user_by_user_id(movie.creator_id)
            movie.creator = user
        connection.close()
        return movie

    def get_db_connection(self):
        return sqlite3.connect(self.db_name)


def commit_and_close(connection):
    connection.commit()
    connection.close()


def get_first_record_or_return(record_list):
    if len(record_list) > 0:
        return record_list[0]
    return None
