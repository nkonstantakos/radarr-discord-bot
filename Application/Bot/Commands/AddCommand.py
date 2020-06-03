from Application.Api.MovieManager import MovieManager
from Application.Trakt.TraktManager import TraktManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
from Application.Api.Domain.Movie import Movie
from Application.Api.Exceptions.MovieExistsException import MovieExistsException
import discord


class AddCommand(BotCommandBase):
    def __init__(self, bot: discord.Client, movie_manager: MovieManager, trakt_manager: TraktManager):
        super().__init__(bot, movie_manager, trakt_manager)

    async def add_movie(self, message: discord.Message):
        try:
            imdb_id = self.get_imdb_id_from_message(message)
            private = self.is_private(message)
            search_results = self.trakt_manager.search_movie(imdb_id)
            if len(search_results) > 0:
                movie_name = search_results[0].title
            else:
                channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
                await channel.send('Sorry, couldn\'t find that movie, check that the url is valid')
                return
            movie: Movie = self.movie_manager.add_movie(imdb_id, movie_name, message.author.id,
                                                        message.author.name, private)
            url = self.IMDB_BASE_URL + imdb_id
            channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
            self.trakt_manager.add_movie(movie)
            await channel.send('Thanks ' + message.author.name + '! I\'ve added '
                               + movie.movie_name + ' to the list.\n' + url)
        except MovieExistsException as e:
            channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
            await channel.send('Hmm sorry looks like someone has already added that movie. (' + e.imdb_id + ')')
