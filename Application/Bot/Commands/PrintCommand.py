from Application.Api.MovieManager import MovieManager
from Application.Trakt.TraktManager import TraktManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
import discord


class PrintCommand(BotCommandBase):
    def __init__(self, bot: discord.Client, movie_manager: MovieManager, trakt_manager: TraktManager):
        super().__init__(bot, movie_manager, trakt_manager)

    def print_all(self, message: discord.Message):
        print('print_all')
