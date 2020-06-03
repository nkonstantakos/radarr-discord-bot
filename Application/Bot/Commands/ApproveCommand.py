from Application.Api.MovieManager import MovieManager
from Application.Trakt.TraktManager import TraktManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
import discord


class ApproveCommand(BotCommandBase):
    def __init__(self, bot: discord.Client, movie_manager: MovieManager, trakt_manager: TraktManager):
        super().__init__(bot, movie_manager, trakt_manager)

    def approve_movie(self, message: discord.Message):
        if message.content.startswith("!approveMovie"):
            self.approve_movie(message)
        elif message.content.startswith("!approveAllMovies"):
            self.approve_all_movies(message)

    def approve_single_movie(self, message: discord.Message):
        print('approve')

    def approve_all_movies(self, message: discord.Message):
        print('approve all')

