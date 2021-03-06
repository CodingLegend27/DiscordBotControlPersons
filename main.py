import discord
from discord import activity
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
import os

TOKEN = os.getenv('DISCORD_TOKEN')

# intents = discord.Intents.default()
# intents.members = True

intents = discord.Intents.all()


# intents = discord.Intents()
# intents.messages=True
# intents.all()


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
bot_member=None
counter=0


@bot.event
async def on_message(message):
    global bot_member, counter
    
    print(f"[LOG] {str(message.author)} -> {message.content}")
    # print(f"Neue Message: {message}")
    
    # if (message.author.bot == True):
        # print("> Nachricht von einem Bot")
        
    # if not bot_member and counter==0:
    #     counter+=1
    if not bot_member and counter==0:
        bot_member = message.author
    if type(message.author) == discord.User:
        # cnt = message.content
        # ctx = await bot.get_context(message)
        message.author=bot_member
        # print("\n\n\n")
        # print(str(message.author))
        # print(f">> {message}")
        # await ctx.send(cnt)
        # await message.author.edit()
        # await on_message(cnt)

    
    if (message.content[0]=='!' or message.author.bot==True): await message.edit(delete_after=6.942)
    
    
    
    # TODO wieder aktivieren
    await bot.process_commands(message)


bot.run(TOKEN, bot=True, reconnect=True)
