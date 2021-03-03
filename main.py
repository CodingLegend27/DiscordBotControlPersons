import discord
from discord import activity
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
import os

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(
    command_prefix="!",
    description="Kinderaufsicht",
    case_insensitive=True,
    intents=intents,
    activity=discord.Game(name="Forniteee")
)
cogs = ['cogs.bot']

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")
    for cog in cogs:
        bot.load_extension(cog)


bot.run(TOKEN, bot=True, reconnect=True)