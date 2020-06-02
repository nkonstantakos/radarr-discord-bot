from Application.Api.MovieManager import MovieManager


class AddCommand(object):
    def __init__(self, bot, movie_manager):
        """
        @type bot: Connection
        @type movie_manager: MovieManager
        """
        self.bot = bot
        self.movie_manager = movie_manager

    def add_movie(self, message):
        """
        @type message: discord.Message
        """
        self.movie_manager.add_movie(message)
