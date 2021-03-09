# main.py 
# author: Christoph Waffler

# main file of a bot to control persons in a discord voice channel

import discord
from discord import activity
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
import os

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    description="Kinderaufsicht",
    case_insensitive=True,
    intents=intents,
    activity=discord.Game(name="Fortnait"),
)
cogs = ['cogs.bot']

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")
    for cog in cogs:
        bot.load_extension(cog)

global bot_member, counter
bot_member = None
counter = 0


@bot.event
async def on_message(message):
    print(f"[LOG] {str(message.author)} -> {message.content}")
    
    global bot_member, counter
    if not bot_member and counter == 0:
        bot_member = message.author
    if type(message.author) == discord.User:
        message.author=bot_member

    
    if (message.content[0] == '!' or message.author.bot == True): 
        await message.edit(delete_after=6.942)

    await bot.process_commands(message)

bot.run(TOKEN, bot=True, reconnect=True)