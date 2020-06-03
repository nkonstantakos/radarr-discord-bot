from Application.Api.Dao.Movies import MovieTable, MovieUpserts, MovieRetrievals
from Application.Api.Dao.Movies.MovieDTO import MovieDTO
from Application.Api.Dao.Votes import VoteTable, VoteRetrievals
from Application.Api.Domain.Movie import Movie
from Application.Api.Domain.PlexUser import PlexUser
from Application.Api.Domain.Vote import Vote
from Application.Api.Dao.PlexUsers import PlexUserRetrievals, PlexUserTable, PlexUserUpserts
from typing import List
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

    def get_users_by_user_ids(self, user_ids: List[int]):
        connection = self.get_db_connection()
        user = PlexUserRetrievals.get_users_by_user_ids(connection, user_ids)
        connection.close()
        return get_first_record_or_return(user)

    def insert_movie(self, movie: Movie):
        connection = self.get_db_connection()
        MovieUpserts.insert_movie(connection, movie)
        connection.commit()
        new_movie: Movie = self.get_movie(movie.imdb_id)
        connection.close()
        return new_movie

    def get_votes_by_movie_ids(self, movie_ids: List[int]):
        connection = self.get_db_connection()
        votes = VoteRetrievals.get_votes_for_movies(connection, movie_ids)
        connection.close()
        return votes if len(votes) > 0 else None

    def get_movie(self, movie_id: int = None, imdb_id: str = None):
        connection = self.get_db_connection()
        if movie_id is not None:
            movie_records: List[MovieDTO] = MovieRetrievals.get_movie_by_imdb_id(connection, imdb_id)
        elif imdb_id is not None:
            movie_records: List[MovieDTO] = MovieRetrievals.get_movie_by_imdb_id(connection, imdb_id)
        else:
            print('Raise exception!')
            return
        movies = self.populate_movie_details(movie_records)
        connection.close()
        return movies[0] if movies is not None else None

    def get_movies(self, channel_id: int = None):
        connection = self.get_db_connection()
        if channel_id is not None:
            movie_records: List[MovieDTO] = MovieRetrievals.get_all_movies_by_channel(connection, channel_id)
        else:
            print('Raise exception!')
            return
        movie = self.populate_movie_details(movie_records)
        connection.close()
        return movie

    def populate_movie_details(self, movies: List[MovieDTO]):
        if movies is not None and len(movies) > 0:
            for movie in movies:
                if movie is not None:
                    user: PlexUser = self.get_users_by_user_ids([movie.creator_id])
                    votes: List[Vote] = self.get_votes_by_movie_ids([movie.movie_id])
                    movie.creator = user
                    movie.votes = votes
        else:
            return None
        return movies

    def get_db_connection(self):
        return sqlite3.connect(self.db_name)


def commit_and_close(connection):
    connection.commit()
    connection.close()


def get_first_record_or_return(record_list):
    if len(record_list) > 0:
        return record_list[0]
    return None
