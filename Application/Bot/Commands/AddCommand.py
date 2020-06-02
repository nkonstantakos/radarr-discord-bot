from Application.Api.MovieManager import MovieManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
from Application.Api.Domain.Movie import Movie
from Application.Api.Exceptions.MovieExistsException import MovieExistsException
import discord


IMDB_BASE_URL = 'https://www.imdb.com/title/'


class AddCommand(BotCommandBase):
    def __init__(self, bot: discord.connection, movie_manager: MovieManager):
        super(self, AddCommand).__init__(self, bot, movie_manager)

    async def add_movie(self, message: discord.Message):
        try:
            imdb_id = self.get_imdb_id_from_message(message)
            private = self.is_private(message)
            movie_name = 'temp'
            movie: Movie = self.movie_manager.add_movie(imdb_id, movie_name, message.author.id, message.author.name, private)

        except MovieExistsException as e:
            channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
            await channel.send('Hmm sorry looks like someone has already added that movie. (' + e.imdb_id + ')')
