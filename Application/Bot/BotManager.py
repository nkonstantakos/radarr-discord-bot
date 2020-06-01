from Application.Api import MovieManager


class BotManager(object):
    def __init__(self, bot, config):
        self.bot = bot
        self.manager = MovieManager(config)

    def process_message(self, message):
        """
        @type message: discord.Message
        """
        if message.content.startswith("!addMovie"):
            self.manager.add_movie(message)
        elif message.content.startswith("!approveMovie"):
            self.manager.approve_movie(message)
        elif message.content.startswith("!approveAllMovies"):
            self.manager.approve_movie(message)
        elif message.content.startswith("!removeMovie"):
            self.manager.remove_move(message)
