from Application.Api.MovieManager import MovieManager


class ApproveCommand(object):
    def __init__(self, bot, movie_manager):
        """
        @type bot: Connection
        @type movie_manager: MovieManager
        """
        self.bot = bot
        self.movie_manager = movie_manager

    def approve_movie(self, message):
        """
        @type message: discord.Message
        """
        if message.content.startswith("!approveMovie"):
            self.approve_movie(message)
        elif message.content.startswith("!approveAllMovies"):
            self.approve_all_movies(message)

    def approve_single_movie(self, message):
        """
        @type message: discord.Message
        """

    def approve_all_movies(self, message):
        """
        @type message: discord.Message
        """
