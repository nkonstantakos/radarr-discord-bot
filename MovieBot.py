import discord
import configparser
from Application.Bot.BotManager import BotManager


config = configparser.ConfigParser()
config.read('properties.ini')
bot = discord.Client()
manager: BotManager = BotManager(bot, config)


def run():
    global config
    bot.run(config['DISCORD']['botKey'])


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    """
    @type message: discord.Message
    """
    global manager
    if str(message.author) == bot.user:
        return
    elif message.content.startswith("!"):
        await manager.process_message(message)

if __name__ == "__main__":
    run()
