# bot.py
# Author: Christoph Waffler

from operator import truediv
import os
import discord
from discord import message
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext.commands.core import command
from discord.abc import Messageable


class Bot(commands.Cog):

    def __init__(self, bot, *command_prefix, **self_bot):
        # commands.Bot.__init__(self, command_prefix=command_prefix, self_bot=self_bot)
        self.bot = bot
        # intents = discord.Intents.default()
        # intents.members = True
        
        # client = discord.Client(intents=intents)
        
        self.connected = False
        
        self.dan1string = "DANI#2390"
        self.dan2string = "DANI#8237"
        self.chrissistring ="Chrissi#0997"
        
        self.felixstring = "LiveYourTIme#1683"

        self.daniel_names = ["daniel", "dani", "downiel"]
        self.chriss_names = ["chrissi", "chris"]
        self.felix_names = ["felix", "fixel", "fixl"]

        # global variables
        # self.dan1
        # self.dan2=None
        # self.chrissi=None


    @commands.command(
        name="kicken",
        description="disconnect a person from the voice channel",
        aliases=['k']
    )
    async def kicken(self, ctx, arg):
        """ disconnect a person from the voice channel """
        print(ctx)
        print(arg)
        
        if not self.connected:
            await self.connect(ctx)
        
        if arg in self.daniel_names:
            await self.kick(self.dan1, ctx)
            await self.kick(self.dan2, ctx)
        
        elif arg in self.chriss_names:
            await self.kick(self.chrissi, ctx)
            
        elif arg in self.felix_names:
            await self.kick(self.felix, ctx)

    # def add_commands(self):
        # @self.command(name="status", pass_context=True)
    @commands.command(
        name='mute',
        description="mute a person serverwide",
        aliases=['m']
    )
    async def mute(self, ctx, arg):
        """ mute a person serverwide """
        if not self.connected:
            await self.connect(ctx)

        # INFO await nicht vergessen
        
        if arg in self.daniel_names:
            await self.set_to_muted(self.dan1, ctx)
            await self.set_to_muted(self.dan2, ctx)
        
        elif arg in self.chriss_names:
            print("log: ban chris")
            await self.set_to_muted(self.chrissi, ctx)
            
        elif arg in self.felix_names:
            await self.set_to_muted(self.felix, ctx)

    @commands.command(
        name='unmute',
        description="unmute a person serverwide",
        aliases=['um']
    )
    async def unmute(self, ctx, arg):
        """ unmute a person serverwide """
        if not self.connected:
            await self.connect(ctx)

        
        if arg in self.daniel_names:
            await self.set_to_unmuted(self.dan1, ctx)
            await self.set_to_unmuted(self.dan2, ctx)
        
        elif arg in self.chriss_names:
            await self.set_to_unmuted(self.chrissi, ctx)
        
        elif arg in self.felix_names:
            await self.set_to_unmuted(self.felix, ctx)
            
    @commands.command(
        name='silence',
        description="mute and deaf a person",
        aliases=["s"]
    )
    async def silence(self, ctx, arg):
        """ silence: mute and deafe a person serverwide """
        if not self.connected:
            await self.connect(ctx)
        
        await self.mute(ctx, arg)
        
        if arg in self.daniel_names:
            await self.set_to_deafen(self.dan1, ctx)
            await self.set_to_deafen(self.dan2, ctx)
        
        elif arg in self.chriss_names:
            await self.set_to_deafen(self.chrissi, ctx)
        
        elif arg in self.felix_names:
            await self.set_to_deafen(self.felix, ctx)
    

    @commands.command(
        name="connect",
        description="status of the bot",
        aliases=['c']
    )
    async def connect(self, ctx):
        """ status of the bot """
        members = ctx.guild.members
        
        # await self.change_presence(activity=discord.Game(name="a game"))
        
        print("hello")
        # activityvar = discord.Game(name="Fornite")
        # await self.change_presence(activity=activityvar)

        
        # print(f"type {type(members[0])}")
        
        # for member in members:
        #     if str(member) == self.dan1string:
        #         self.dan1 = member
        #     elif str(member) == self.dan2string:
        #         self.dan2 = member
        #     elif str(member) == self.chrissistring:
        #         self.chrissi = member
                
        for i in range(len(members)):
            if str(members[i]) == self.dan1string:
                self.dan1 = members[i].id
            elif str(members[i]) == self.dan2string:
                self.dan2 = members[i].id
            elif str(members[i]) == self.chrissistring:
                self.chrissi = members[i].id
            elif str(members[i]) == self.felixstring:
                self.felix = members[i].id
        
        self.dan1 = ctx.message.guild.get_member(self.dan1)
        self.dan2 = ctx.message.guild.get_member(self.dan2)
        self.chrissi = ctx.message.guild.get_member(self.chrissi)
        
        self.felix = ctx.message.guild.get_member(self.felix)


        
        print(f"type {type(self.dan1)}")
        
        # self.dan1 = ctx.message.guild.get_member(self.dan1string)
        # self.dan2 = ctx.message.guild.get_member(self.dan2string)
        # self.chrissi = ctx.message.guild.get_member(self.chrissistring)
        
        # print(str(self.chrissi))
        
        # print(str(s))
        
        
        # for member in ctx.channel.users:
        #     string = str(member)
        #     if string == dan1string:
        #         dan1 = member
        #     elif string == dan2string:
        #         dan2 = member
        #     elif string == chrissistring:
        #         chrissi = member
        
        # print("log: connect")
        # print(arg)
        
        
        self.connected = True
        
        await ctx.send("> Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")
        await ctx.send("> Kinderaufsicht eingestaltet!!! 🚨🚨🚨")


    # TODO finish
    # @commands.command()
    # async def clear(self, ctx, number):
    #     mgs = []
    #     number = int(number)
    #     async for x in Messageable.history(ctx.message.channel, limit=number):
    #         if x[0]=='!': mgs.append(x)
    #     # await ctx.delete_messages(mgs)
    #     await self.delete_nam 

    async def check_connected(self, context) -> bool:
        voice_state = context.member.voice
        return voice_state is not None

    # @bot.event
    async def on_ready(self):
        print(f"{bot.user.name} has connected to Discord!")


    async def set_to_muted(self, member: discord.Member, ctx):
        if member is None: return
        
        response = f"> {member} wird gemutet!"
        await ctx.send(response)
        
        await member.edit(mute=True)

    # @bot.event()
    async def set_to_unmuted(self, member: discord.Member, ctx):
        if member is None: return
        response = f"> {member} wird ungemutet!"
        await ctx.send(response)
        await member.edit(mute=False)
        await member.edit(deafen=False)
        
    async def set_to_deafen(self, member: discord.Member, ctx):
        if member is None: return
        response = f"> {member} wird taub!"
        await ctx.send(response)
        await member.edit(deafen=True)    
    
    # @bot.event()
    async def kick(self, member: discord.Member, ctx):
        if member is None: return
        
        response = f"> {member} wird gekickt!"
        await ctx.send(response)
        await member.edit(voice_channel=None)
        
    # # @client.command()
    # # @commands.is_owner()
    # async def shutdown(ctx):
    #     await ctx.bot.logout()


    # @bot.command()
    # async def get_input(ctx, arg):
    #     await ctx.send(arg)
        
    # @bot.command()
    
    
    # async def on_message(self, message):
    #     # ctx = await bot.get_context(message)
    #     ctx = await ctx.message.guild.get_context(message)
    #     if 
        
    
    

    # # @bot.event
    # async def on_message(self, message: discord.message):
    #     """reaction to the send message of a mod/webhook"""
    #     print(message)
        
    #     for member in message.guild.members:
    #         print(member)
    #         if str(member) == dan1string:
    #             dan1=member
    #         elif str(member)==dan2string:
    #             dan2=member
    #         elif str(member)==chrissistring:
    #             chrissi=member
        

    #     # if 
        
    #     print(type(chrissi))
        
    #     if message.content == "!mute daniel":
    #         response = "> Downiel wird gemutet!"
    #         await message.channel.send(response)
            
    #         await set_to_muted(dan1)
    #         await set_to_muted(dan2)
            
    #         # remove
    #         await set_to_muted(chrissi)
            
    #         print("works!")
    #         await message.channel.send("hello from the other side")
            
    #     elif message.content == "!dc daniel":
    #         response = "> Downiel wird disconnected!"
    #         await message.channel.send(response)
            
    #         await kick(dan1)
    #         await kick(dan2)
    #         await kick(chrissi)
            
            
    #     elif message.content == "!unmute daniel":
    #         # TODO unmute doensÄt work right now
    #         await set_to_unmuted(dan1)
    #         await set_to_unmuted(dan2)
            
    #         await set_to_unmuted(chrissi)
        
    
    
def setup(bot):
    bot.add_cog(Bot(bot))


# if __name__ == "__main__":
#     TOKEN = os.getenv('DISCORD_TOKEN')
#     bot = Bot(command_prefix="!", self_bot=False)
#     bot.run(TOKEN)