# import logging
# import discord
# from discord import app_commands
#
# intents = discord.Intents.default()
# intents.message_content = True
# intents.members = True
#
# client = discord.Client(intents=intents)
# tree = app_commands.CommandTree(client)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
#
# @client.event
# async def on_ready():
#     await tree.sync(guild=discord.Object(id=1432262035676336170))
#     print("Ready!")
#
# @tree.command(
#     name="commandname",
#     description="My first application Command",
#     guild=discord.Object(id=1432262035676336170)
# )
# async def first_command(interaction):
#     print(interaction)
#     await interaction.response.send_message("Hello!")
#
# client.run('MTQ1MzQzNTQ5OTYwNjcwNDE3OQ.GxT-TI.LwmxccHdYDoK6oUm0uD4YGec5ibLmgB4yI4Q-4', log_handler=handler, log_level=logging.DEBUG)


import json

import discord
from discord import app_commands
from discord.app_commands import CommandTree
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/EvilBot', intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    #await tree.sync(guild=discord.Object(id=1432262035676336170))
    #tree.clear_commands(guild=discord.Object(id=1432262035676336170))
    #bot.tree.clear_commands(guild=discord.Object(id=1432262035676336170))
    await tree.sync(guild=discord.Object(id=1432262035676336170))
    await bot.tree.sync(guild=discord.Object(id=1432262035676336170))
    print("Ready!")

@bot.tree.command(
    name="messageallies",
    description="Allows traitors and masterminds to message each other",
    guild=discord.Object(id=1432262035676336170)
)
@app_commands.describe(message = 'The message you wish to send to your co-conspirators.')
async def first_command(interaction : discord.Interaction, message : str):
    if (message == '' or message == None):
        await interaction.response.send_message("Please provide a message!")
        return

    if interaction.user.name == 'doecommajohn' and interaction.channel.name == 'john-channel':
        await send_messages('JohnTestAccount', 'john-channel-2', message)
    elif interaction.user.name == 'lazyskylight' and interaction.channel.name == 'freya':
        await send_messages('Pattern', 'freya', message)
        await send_messages('Pattern', 'juna', message)
        await send_messages('Pattern', 'allister', message)
    elif interaction.user.name == 'itzellis' and interaction.channel.name == 'juna':
        await send_messages('skibitoilet67', 'freya', message)
        await send_messages('skibitoilet67', 'juna', message)
        await send_messages('skibitoilet67', 'allister', message)
    elif interaction.user.name == 'firthyy' and interaction.channel.name == 'allister':
        await send_messages('Bloodyrose', 'freya', message)
        await send_messages('Bloodyrose', 'juna', message)
        await send_messages('Bloodyrose', 'allister', message)
    elif interaction.user.name == 'caine_.21' and interaction.channel.name == 'lin':
        await send_messages('Phosphorus', 'lin', message)
        await send_messages('Phosphorus', 'famine', message)
        await send_messages('Phosphorus', 'nikolai', message)
    elif interaction.user.name == 'ghosteteer' and interaction.channel.name == 'famine':
        await send_messages('Angel of Gluttony', 'lin', message)
        await send_messages('Angel of Gluttony', 'famine', message)
        await send_messages('Angel of Gluttony', 'nikolai', message)
    elif interaction.user.name == 'solarixxx' and interaction.channel.name == 'nikolai':
        await send_messages('Hydrangea', 'lin', message)
        await send_messages('Hydrangea', 'famine', message)
        await send_messages('Hydrangea', 'nikolai', message)
    else:
        await interaction.response.send_message("This functionality is only available to traitors and masterminds within their private channels. If this is you, give John Doe a ping and he'll fix it. Probably")

    await interaction.response.send_message("Message sent!")

async def send_messages(sender, destination, msg):
    guild = bot.get_guild(1432262035676336170)
    channelMatch = None

    for x in guild.channels:
        if x.name == destination and x.category.name == "Assholes":
            channelMatch = x
            break

    if channelMatch is None:
        raise 'Could not find channel!'

    await channelMatch.send('Message received from ' + sender + ': ' + msg)
    #print(len(deleteMe.channels))
    #bot.get_all_channels()

bot.run(token, log_handler=handler, log_level=logging.DEBUG)