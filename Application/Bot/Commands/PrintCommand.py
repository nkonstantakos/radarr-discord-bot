from typing import List
import prettytable
from Application.Api.Domain.Movie import Movie
from Application.Api.MovieManager import MovieManager
from Application.Trakt.TraktManager import TraktManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
import discord


class PrintCommand(BotCommandBase):
    def __init__(self, bot: discord.Client, movie_manager: MovieManager, trakt_manager: TraktManager):
        super().__init__(bot, movie_manager, trakt_manager)

    async def print(self, message: discord.Message):
        movies: List[Movie] = self.movie_manager.get_movies(channel_id=message.channel.id)
        response: str = self.generate_movie_table(movies)
        channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
        await channel.send(response)

    def generate_movie_table(self, movies: List[Movie]):
        response = prettytable.PrettyTable(["ID", "Name", "Added By"])
        for movie in movies:
            response.add_row([movie.movie_id, movie.movie_name, movie.creator.nickname])
        return "``" + response.get_string() + "``"
