from Application.Api.MovieManager import MovieManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
import discord


class PrintCommand(BotCommandBase):
    def __init__(self, bot: discord.connection, movie_manager: MovieManager):
        super(self, PrintCommand).__init__(self, bot, movie_manager)

    def print_all(self, message):
        """
        @type message: discord.Message
        """
