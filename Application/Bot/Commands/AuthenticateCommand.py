from Application.Api.MovieManager import MovieManager
from Application.Trakt.TraktManager import TraktManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
import discord


class AuthenticateCommand(BotCommandBase):
    def __init__(self, bot: discord.Client, movie_manager: MovieManager, trakt_manager: TraktManager):
        super().__init__(bot, movie_manager, trakt_manager)

    def authenticate(self, message: discord.Message):
        pin: str = message.content[6:]
        self.trakt_manager.authenticate(pin)
