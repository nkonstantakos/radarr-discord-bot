from Application.Api.Dao.MovieBotDao import MovieBotDao
from Application.Api.Functions.AddMovieFunction import AddMovieFunction


class MovieManager(object):
    def __init__(self, config):
        self.config = config
        self.dao = MovieBotDao(config['APPLICATION']['dbName'])
        self.dao.create_tables()
        self.add_movie_function = AddMovieFunction(self.config, self.dao)

    def add_movie(self, imdb_id, movie_name, creator_id, creator_name, is_private):
        return self.add_movie_function.add_movie(imdb_id, movie_name, creator_id, creator_name, is_private)

    def approve_movie(self, message):
        print('Approve Movie')

    def approve_all_movies(self, message):
        print('Approve All')

    def remove_movie(self, message):
        print('Remove Movie')
