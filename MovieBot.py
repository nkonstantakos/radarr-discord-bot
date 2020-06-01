import discord
import sys
import configparser
from trakt import Trakt


config = configparser.ConfigParser()
config.read('properties.ini')
bot = discord.Client()

Trakt.configuration.defaults.client(
    id=config['TRAKT']['clientId'],
    secret=config['TRAKT']['clientSecret']
)


def run(args):
    global config
    # bot.run(config['DISCORD']['botKey'])


def addMovie(message):
    """
    @type message: discord.Message
    """




@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.get_channel(int(config['DISCORD']['channelId'])).send('Welp, hopefully I did something')


@bot.event
async def on_message(message):
    """
    @type message: discord.Message
    """

    if str(message.author) == bot.user:
        return
    elif message.content.startswith("!"):
        if message.content.startswith("!addMovie"):
            addMovie(message)
        elif message.content.startswith("!approveMovie"):
            approveMovie()
        elif message.content.startswith("!addMovie"):
            approveAllMovies()
        elif message.content.startswith("!removeMovie"):
            removeMovie()

if __name__ == "__main__":
    run(sys.argv[1:])
