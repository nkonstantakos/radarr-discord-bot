from Application.Api.MovieManager import MovieManager


class PrintCommand(object):
    def __init__(self, bot, movie_manager):
        """
        @type bot: Connection
        @type movie_manager: MovieManager
        """
        self.bot = bot
        self.movie_manager = movie_manager

    def print_all(self, message):
        """
        @type message: discord.Message
        """
