from Application.Api.MovieManager import MovieManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
import discord


class VoteCommand(BotCommandBase):
    def __init__(self, bot: discord.connection, movie_manager: MovieManager):
        super(self, VoteCommand).__init__(self, bot, movie_manager)

    def vote_movie(self, message: discord.Message):
        print('vote_movie')

    def downvote_movie(self, message: discord.Message):
        print('downvote_move')
