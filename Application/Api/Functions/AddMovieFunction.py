from Application.Api.Dao.MovieBotDao import MovieBotDao
from Application.Api.Domain.PlexUser import PlexUser
from Application.Api.Exceptions.MovieExistsException import MovieExistsException
from Application.Api.Domain.Movie import Movie
import configparser


class AddMovieFunction(object):
    def __init__(self, config: configparser.ConfigParser, dao: MovieBotDao):
        self.config: configparser.ConfigParser = config
        self.dao: MovieBotDao = dao

    def add_movie(self, imdb_id, trakt_id, movie_name, creator_id, creator_name, private, channel_id):
        user_record: PlexUser = self.dao.get_user_by_discord_id(creator_id)
        if user_record is None:
            new_user: PlexUser = PlexUser(None, creator_id, creator_name, False, False)
            user_record = self.dao.insert_user(new_user)

        self.check_movie_exists(imdb_id)
        approved: bool = user_record.admin or user_record.moderator
        new_movie: Movie = Movie(None, imdb_id, movie_name, user_record, approved, False, False, private, channel_id,
                                 trakt_id, None)
        inserted_movie: Movie = self.dao.insert_movie(new_movie)
        return inserted_movie

    def check_movie_exists(self, imdb_id: str):
        existing_movie = self.dao.get_movie(imdb_id=imdb_id)
        if existing_movie is not None:
            raise MovieExistsException(existing_movie.movie_name, existing_movie.creator.nickname)

