from Application.Api.MovieManager import MovieManager
from Application.Dao.MovieBotDao import MovieBotDao


class BotManager(object):
    def __init__(self, bot, config):
        self.bot = bot
        self.movie_manager = MovieManager(config)
        self.dao = MovieBotDao(config['APPLICATION']['dbName'])
        self.dao.create_tables()

    def process_message(self, message):
        """
        @type message: discord.Message
        """
        if message.content.startswith("!addMovie"):
            self.movie_manager.add_movie(message)
        elif message.content.startswith("!approveMovie"):
            self.movie_manager.approve_movie(message)
        elif message.content.startswith("!approveAllMovies"):
            self.movie_manager.approve_movie(message)
        elif message.content.startswith("!removeMovie"):
            self.movie_manager.remove_move(message)
