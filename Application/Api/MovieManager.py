from Application.Dao.MovieBotDao import MovieBotDao
from Application.Api.Functions.AddMovieFunction import AddMovieFunction
import discord.channel

IMDB_BASE_URL = 'https://www.imdb.com/title/'


class MovieManager(object):
    def __init__(self, config):
        self.config = config
        self.dao = MovieBotDao(config['APPLICATION']['dbName'])
        self.dao.create_tables()
        self.add_movie_function = AddMovieFunction(self.config, self.dao)

    def add_movie(self, message):
        """
        @type message: discord.Message
        """
        imdb_id = None
        message_pieces = message.content.split()
        if message_pieces[1].startswith(IMDB_BASE_URL):
            url_part = message_pieces[1][len(IMDB_BASE_URL):]
            imdb_id = url_part.split('/')[0]
        private = is_private(message)
        return self.add_movie_function.add_movie(message.author, imdb_id, private)

    def approve_movie(self, message):
        print('Approve Movie')

    def approve_all_movies(self, message):
        print('Approve All')

    def remove_movie(self, message):
        print('Remove Movie')


def is_private(message):
    """
    @type message: discord.Message
    """
    print(message.channel.type)
    return message.channel.type[0] == 'private'
