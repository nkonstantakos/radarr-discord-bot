from Application.Api.MovieManager import MovieManager
from Application.Trakt.TraktManager import TraktManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
import discord


class AuthenticateCommand(BotCommandBase):
    def __init__(self, bot: discord.Client, movie_manager: MovieManager, trakt_manager: TraktManager):
        super().__init__(bot, movie_manager, trakt_manager)

    async def authenticate(self, message: discord.Message):
        pin: str = message.content.split(' ')[1]
        success: bool = self.trakt_manager.authenticate(pin)
        channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
        if success:
            await channel.send("I've successfully authenticated you with Trakt.")
        else:
            await channel.send("Something went wrong, authentication failed. This is the pin I tried: " + pin)
