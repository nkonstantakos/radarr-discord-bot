from Application.Api.MovieManager import MovieManager
from Application.Bot.Commands.AddCommand import AddCommand
from Application.Bot.Commands.ApproveCommand import ApproveCommand
from Application.Bot.Commands.AuthenticateCommand import AuthenticateCommand
from Application.Bot.Commands.PrintCommand import PrintCommand
from Application.Bot.Commands.VoteCommand import VoteCommand
from Application.Trakt.TraktManager import TraktManager
import discord
import configparser


class BotManager(object):
    def __init__(self, bot: discord.Client, config: configparser.ConfigParser):
        self.bot = bot
        self.movie_manager = MovieManager(config)
        self.trakt_manager = TraktManager(config)
        self.addCommand = AddCommand(self.bot, self.movie_manager, self.trakt_manager)
        self.approveCommand = ApproveCommand(self.bot, self.movie_manager, self.trakt_manager)
        self.authenticateCommand = AuthenticateCommand(self.bot, self.movie_manager, self.trakt_manager)
        self.printCommand = PrintCommand(self.bot, self.movie_manager, self.trakt_manager)
        self.voteCommand = VoteCommand(self.bot, self.movie_manager, self.trakt_manager)

    async def process_message(self, message: discord.Message):
        if message.content.startswith("!addMovie"):
            await self.addCommand.add_movie(message)
        elif message.content.startswith("!approveMovie"):
            await self.approveCommand.approve_movie(message)
        elif message.content.startswith("!approveAllMovies"):
            await self.approveCommand.approve_movie(message)
        elif message.content.startswith("!print"):
            await self.printCommand.print(message)
        elif message.content.startswith("!removeMovie"):
            await self.movie_manager.remove_move(message)
        elif message.content.startswith("!auth"):
            await self.authenticateCommand.authenticate(message)
        elif message.content.startswith("!test"):
            search_results = self.trakt_manager.search_movie('tt6193424')
            print(search_results[0].keys)
            for tup in search_results[0].keys:
                if tup[0] == 'trakt':
                    print(tup[1])
            print("nothin to test")
