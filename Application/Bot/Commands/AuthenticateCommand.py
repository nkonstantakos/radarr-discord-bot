from Application.Api.MovieManager import MovieManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
import discord


class AuthenticateCommand(BotCommandBase):
    def __init__(self, bot: discord.connection, movie_manager: MovieManager):
        super(self, AuthenticateCommand).__init__(self, bot, movie_manager)

    def authenticate(self, message: discord.Message):
        print('Authenticate')
