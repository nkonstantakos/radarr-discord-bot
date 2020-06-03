from Application.Api.Dao.MovieBotDao import MovieBotDao
from Application.Api.Functions.AddMovieFunction import AddMovieFunction


class MovieManager(object):
    def __init__(self, config):
        self.config = config
        self.dao = MovieBotDao(config['APPLICATION']['dbName'])
        self.dao.create_tables()
        self.add_movie_function = AddMovieFunction(self.config, self.dao)

    def add_movie(self, imdb_id, trakt_id, movie_name, creator_id, creator_name, is_private, channel_id):
        return self.add_movie_function.add_movie(imdb_id, trakt_id, movie_name, creator_id,
                                                 creator_name, is_private, channel_id)

    def get_movie(self, movie_id: int = None, imdb_id: str = None):
        return self.dao.get_movie(movie_id=movie_id, imdb_id=imdb_id)

    def get_user(self, discord_id: int):
        return self.dao.get_user_by_discord_id(discord_id)

    def approve_movie(self, message):
        print('Approve Movie')

    def approve_all_movies(self, message):
        print('Approve All')

    def remove_movie(self, message):
        print('Remove Movie')
