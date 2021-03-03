# bot.py
# Author: Christoph Waffler

from operator import truediv
import os
import discord
from discord import message
from discord.ext import commands
from discord.ext.commands import Context


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

        self.daniel_names = ["daniel", "dani", "downiel"]
        self.chriss_names = ["chrissi", "chris"]

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
        if not self.connected:
            await self.connect(ctx)
        
        response = f"> {arg} wird gekickt!"
        await ctx.send(response)
        
        if arg in self.daniel_names:
            await self.kick(self.dan1)
            await self.kick(self.dan2)
        
        elif arg in self.chriss_names:
            await self.kick(self.chrissi)

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
            
        response = f"> {arg} wird gemutet!"
        await ctx.send(response)
        
        # INFO await nicht vergessen
        
        if arg in self.daniel_names:
            await self.set_to_muted(self.dan1)
            await self.set_to_muted(self.dan2)
        
        elif arg in self.chriss_names:
            print("log: ban chris")
            await self.set_to_muted(self.chrissi)

    @commands.command(
        name='unmute',
        description="unmute a person serverwide",
        aliases=['um']
    )
    async def unmute(self, ctx, arg):
        """ unmute a person serverwide """
        if not self.connected:
            await self.connect(ctx)
        
        response = f"> {arg} wird ungemutet!"
        await ctx.send(response)
        
        if arg in self.daniel_names:
            await self.set_to_unmuted(self.dan1)
            await self.set_to_unmuted(self.dan2)
        
        elif arg in self.chriss_names:
            await self.set_to_unmuted(self.chrissi)
        
    
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
        
        self.dan1 = ctx.message.guild.get_member(self.dan1)
        self.dan2 = ctx.message.guild.get_member(self.dan2)
        self.chrissi = ctx.message.guild.get_member(self.chrissi)


        
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
        
        await ctx.send("> Kinderaufsicht eingestaltet!!! 🚨🚨🚨")

    

    async def check_connected(self, context) -> bool:
        voice_state = context.member.voice
        return voice_state is not None

    # @bot.event
    async def on_ready(self):
        print(f"{bot.user.name} has connected to Discord!")


    async def set_to_muted(self, member: discord.Member):
        if member is None: return
        print("log muteee")
        await member.edit(mute=True)

    # @bot.event()
    async def set_to_unmuted(self, member: discord.Member):
        if member is None: return
        
        await member.edit(mute=False)
        
    # @bot.event()
    async def kick(self, member: discord.Member):
        if member is None: return
        
        await member.edit(voice_channel=None)
        
    # # @client.command()
    # # @commands.is_owner()
    # async def shutdown(ctx):
    #     await ctx.bot.logout()


    # @bot.command()
    # async def get_input(ctx, arg):
    #     await ctx.send(arg)
        
    # @bot.command()
    

    # @bot.event
    # async def on_message(message: discord.message):
    #     """reaction to the send message of a mod/webhook"""

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