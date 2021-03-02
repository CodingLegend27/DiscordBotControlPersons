# bot.py
# Author: Christoph Waffler

import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

print(TOKEN)

@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord!")


async def set_to_deafed(member: discord.Member):
    await member.edit(deafen=True)

async def set_to_undeafed(member: discord.Member):
    await member.edit(deafen=False)
    
async def kick(member: discord.Member):
    await member.edit(voice_channel=None)

# @client.command()
# @commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()


@client.event
async def on_message(message):
    
    """reaction to the send message of a mod"""
    
    if message.content == "mute daniel":
        response = "> Downiel wird gemutet!"
        await message.channel.send(response)
        
        
        # TODO implement mute of daniel
        
    elif message.content == "dc daniel":
        response = "> Downiel wird disconnected!"
        await message.channel.send(response)
        
        # TODO implement disconnect of daniel
    
    

client.run(TOKEN)