from Application.Api.MovieManager import MovieManager
from Application.Trakt.TraktManager import TraktManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
import discord


class VoteCommand(BotCommandBase):
    def __init__(self, bot: discord.Client, movie_manager: MovieManager, trakt_manager: TraktManager):
        super().__init__(bot, movie_manager, trakt_manager)

    def vote_movie(self, message: discord.Message):
        print('vote_movie')

    def downvote_movie(self, message: discord.Message):
        print('downvote_move')
