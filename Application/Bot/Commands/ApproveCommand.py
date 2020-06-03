from Application.Api.MovieManager import MovieManager
from Application.Trakt.TraktManager import TraktManager
from Application.Bot.Commands.BotCommandBase import BotCommandBase
from Application.Api.Domain.Movie import Movie
from Application.Api.Domain.PlexUser import PlexUser
import discord


class ApproveCommand(BotCommandBase):
    def __init__(self, bot: discord.Client, movie_manager: MovieManager, trakt_manager: TraktManager):
        super().__init__(bot, movie_manager, trakt_manager)

    async def approve_movie(self, message: discord.Message):
        if message.content.startswith("!approveMovie"):
            self.approve_movie(message)
        elif message.content.startswith("!approveAllMovies"):
            self.approve_all_movies(message)

    async def approve_single_movie(self, message: discord.Message):
        channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
        user: PlexUser = self.movie_manager.get_user(message.author.id)
        if user is not None and not(user.moderator or user.admin):
            await channel.send('Sorry, you need to be an admin or moderator to perform this action!')
        message_pieces = message.content.split(' ')
        movie_id = message_pieces[1]
        movie_record: Movie = self.movie_manager.get_movie(movie_id=movie_id)
        response = self.trakt_manager.add_movie(movie_record)
        if response is None:
            # Send message to admin to re-authenticate
            await channel.send("Something went wrong...either I couldn't find the movie or an admin needs to "
                               "reauthorize me.")
            return
        updated_movie: Movie = self.movie_manager.approve_movie(movie_id)
        if updated_movie.approved:
            await channel.send('All set! Movie has been marked as approved and download should begin shortly.')
        else:
            await channel.send('Well fuck. Something seems to have gone wrong here, better let someone know.')

    async def approve_all_movies(self, message: discord.Message):
        channel: discord.GroupChannel = self.bot.get_channel(message.channel.id)
        await channel.send('Sorry, I don\'t support that kind of request yet!')

