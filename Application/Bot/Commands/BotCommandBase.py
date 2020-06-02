from Application.Api.MovieManager import MovieManager
import discord


class BotCommandBase(object):
    def __init__(self, bot, movie_manager):
        self.bot: discord.Client = bot
        self.movie_manager: MovieManager = movie_manager
        self.IMDB_BASE_URL = 'https://www.imdb.com/title/'

    def get_imdb_id_from_message(self, message: discord.Message):
        imdb_id = None
        message_pieces = message.content.split()
        if message_pieces[1].startswith(self.IMDB_BASE_URL):
            url_part = message_pieces[1][len(self.IMDB_BASE_URL):]
            imdb_id = url_part.split('/')[0]
        return imdb_id


def is_private(message: discord.Message):
    return message.channel.type[0] == 'private'

