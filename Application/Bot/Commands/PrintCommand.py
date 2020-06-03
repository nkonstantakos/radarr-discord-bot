from Application.Api.MovieManager import MovieManager
from Application.Trakt.TraktManager import TraktManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
import discord


class PrintCommand(BotCommandBase):
    def __init__(self, bot: discord.Client, movie_manager: MovieManager, trakt_manager: TraktManager):
        super().__init__(bot, movie_manager, trakt_manager)

    async def print_all(self, message: discord.Message):
        channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
        await channel.send('Sorry, I don\'t support that kind of request yet!')
