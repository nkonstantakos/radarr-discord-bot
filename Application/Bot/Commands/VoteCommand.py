from Application.Api.MovieManager import MovieManager


class VoteCommand(object):
    def __init__(self, bot, movie_manager):
        """
        @type bot: Connection
        @type movie_manager: MovieManager
        """
        self.bot = bot
        self.movie_manager = movie_manager

    def vote_movie(self, message):
        """
        @type message: discord.Message
        """

    def downvote_movie(self, message):
        """
        @type message: discord.Message
        """
