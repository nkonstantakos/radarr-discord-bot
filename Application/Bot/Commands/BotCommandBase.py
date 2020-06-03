from Application.Api.MovieManager import MovieManager
from Application.Trakt.TraktManager import TraktManager
import discord


class BotCommandBase(object):
    def __init__(self, bot: discord.Client, movie_manager: MovieManager, trakt_manager: TraktManager):
        self.bot: discord.Client = bot
        self.movie_manager: MovieManager = movie_manager
        self.trakt_manager = trakt_manager
        self.IMDB_BASE_URL = 'https://www.imdb.com/title/'
        self.TRAKT_ID_NAME = 'trakt'

    def get_imdb_id_from_message(self, message: discord.Message):
        imdb_id = None
        message_pieces = message.content.split()
        if message_pieces[1].startswith(self.IMDB_BASE_URL):
            url_part = message_pieces[1][len(self.IMDB_BASE_URL):]
            imdb_id = url_part.split('/')[0]
        return imdb_id

    def get_trakt_id(self, search_result):
        for pair in search_result.keys:
            if pair[0] == self.TRAKT_ID_NAME:
                return pair[1]

    def is_private(self, message: discord.Message):
        return message.channel.type[0] == 'private'

