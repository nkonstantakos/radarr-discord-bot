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
            if search_results is not None and len(search_results) > 0:
                movie_name = search_results[0].title
            else:
                channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
                await channel.send('Sorry, couldn\'t find that movie, check that the url is valid')
                return
            trakt_id = self.get_trakt_id(search_results[0])
            movie: Movie = self.movie_manager.add_movie(imdb_id, trakt_id, movie_name, message.author.id,
                                                        message.author.name, private, message.channel.id)
            channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
            await channel.send('Thanks ' + message.author.name + '! I\'ve added '
                               + movie.movie_name + ' to the list.')
        except MovieExistsException as e:
            channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
            # count this as a vote if not deleted, declined or approved
            await channel.send('No need to add \'' + e.movie_name + '\', ' + e.creator_name + ' already added it!')
