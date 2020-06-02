from Application.Api.MovieManager import MovieManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
import discord


class ApproveCommand(BotCommandBase):
    def __init__(self, bot: discord.connection, movie_manager: MovieManager):
        super(self, ApproveCommand).__init__(self, bot, movie_manager)

    def approve_movie(self, message: discord.Message):
        if message.content.startswith("!approveMovie"):
            self.approve_movie(message)
        elif message.content.startswith("!approveAllMovies"):
            self.approve_all_movies(message)

    def approve_single_movie(self, message: discord.Message):
        print('approve')

    def approve_all_movies(self, message: discord.Message):
        print('approve all')

