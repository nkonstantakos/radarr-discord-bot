from Application.Api.MovieManager import MovieManager
from Application.Bot.Commands.AddCommand import AddCommand
from Application.Bot.Commands.ApproveCommand import ApproveCommand
from Application.Bot.Commands.AuthenticateCommand import AuthenticateCommand
from Application.Bot.Commands.PrintCommand import PrintCommand
from Application.Bot.Commands.VoteCommand import VoteCommand
import discord
import configparser


class BotManager(object):
    def __init__(self, bot, config):
        """
        @type bot: discord.Client
        @type config: configparser.ConfigParser
        """
        self.bot = bot
        self.movie_manager = MovieManager(config)
        self.addCommand = AddCommand(self.bot, self.movie_manager)
        self.approveCommand = ApproveCommand(self.bot, self.movie_manager)
        self.authenticateCommand = AuthenticateCommand(self.bot, self.movie_manager)
        self.printCommand = PrintCommand(self.bot, self.movie_manager)
        self.voteCommand = VoteCommand(self.bot, self.movie_manager)

    def process_message(self, message):
        """
        @type message: discord.Message
        """
        if message.content.startswith("!addMovie"):
            self.addCommand.add_movie(message)
        elif message.content.startswith("!approveMovie"):
            self.approveCommand.approve_movie()
        elif message.content.startswith("!approveAllMovies"):
            self.approveCommand.approve_movie()
        elif message.content.startswith("!removeMovie"):
            self.movie_manager.remove_move(message)
