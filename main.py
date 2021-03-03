import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
import os

TOKEN = os.getenv('DISCORD_TOKEN')
# TOKEN = "ODE2NDI4OTQ2NjU2NTkxOTIx.YD60tQ.Pq2KNFDQs-4ltn9JnuIaSpGq-gE"

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(
    command_prefix="!",
    description="Kinderaufsicht",
    case_insensitive=True,
    intents=intents
)
cogs = ['cogs.bot']

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")
    for cog in cogs:
        bot.load_extension(cog)


bot.run(TOKEN, bot=True, reconnect=True)