# bot.py
# author: Christoph Waffler
import os
import discord
from discord.ext import commands
from discord.ext.commands.core import command
from namesloader import NamesLoader

class Bot(commands.Cog):

    def __init__(self, bot, *command_prefix, **self_bot):
        self.bot = bot
        
        self.connected = False
        
        # load name's list
        self.name_to_tags, self.tag_to_names = NamesLoader().load_file("names.txt")
        
        with open("admin.txt") as f:
            content = f.readlines()
        
        self.admins = [x.strip() for x in content]

    @commands.command(
        name="kicken",
        description="disconnect a person from the voice channel",
        aliases=['k']
    )
    async def kicken(self, ctx, arg):
        """ disconnect a person from the voice channel """                
        arg = arg.lower()
        
        if arg == "all":
            if str(ctx.author) in self.admins:
                members = await self.get_members_voice_channel(ctx)
                for m in members:
                    if m.id != ctx.author.id: 
                        await self.kick(m, ctx)
            else:
                await ctx.send("> HAHAHAHA")
            
        if arg in self.name_to_member:
            for m in self.name_to_member[arg]:
                await self.kick(m, ctx)
                
        else: await ctx.send(f"> name {arg} not recognized")

    @commands.command(
        name='mute',
        description="mute a person serverwide",
        aliases=['m']
    )
    async def mute(self, ctx, arg):
        """ mute a person serverwide """
        arg = arg.lower()
        
        if arg == "all":
            if str(ctx.author) in self.admins:
                members = await self.get_members_voice_channel(ctx)
                for m in members:
                    if m.id != ctx.author.id: 
                        await self.set_to_muted(m, ctx)
            else:
                await ctx.send("> HAHAHAHA")

        elif arg in self.name_to_member:
            for m in self.name_to_member[arg]:
                await self.set_to_muted(m, ctx)
                
        else: await ctx.send(f"> name {arg} not recognized")

    @commands.command(
        name='unmute',
        description="unmute a person serverwide",
        aliases=['um']
    )
    async def unmute(self, ctx, arg):
        """ unmute a person serverwide """
        arg = arg.lower()
        
        if arg == "all":
            if str(ctx.author) in self.admins:
                members = await self.get_members_voice_channel(ctx)
                for m in members:
                    if m.id != ctx.author.id: 
                        await self.set_to_unmuted(m, ctx)
            else:
                await ctx.send("> HAHAHAHA")
        
        elif arg in self.name_to_member:
            for m in self.name_to_member[arg]:
                await self.set_to_unmuted(m, ctx)
        
        else: await ctx.send(f"> name {arg} not recognized")

            
    @commands.command(
        name='silence',
        description="mute and deaf a person",
        aliases=["si"]
    )
    async def silence(self, ctx, arg):
        """ mute and deafe a person serverwide """
        arg = arg.lower()
        
        if arg == "all":
            if str(ctx.author) in self.admins:
                members = await self.get_members_voice_channel(ctx)
                for m in members:
                    if m.id != ctx.author.id: 
                        await self.set_to_muted(m, ctx)
                        await self.set_to_deafen(m, ctx)
            else:
                await ctx.send("> HAHAHAHA")
        
        elif arg in self.name_to_member:
            for m in self.name_to_member[arg]:
                await self.set_to_muted(m, ctx)
                await self.set_to_deafen(m, ctx)
            
        else: await ctx.send(f"> name {arg} not recognized")


    @commands.command(
        name="connect",
        description="status of the bot",
        aliases=['c']
    )
    async def connect(self, ctx):
        """ status of the bot """
        members = ctx.guild.members        
        print(f"> the bot has been awaken")
        
        self.name_to_member = dict()
        
        print(f"[INFO] load members")
        for m in members:
            m_str = str(m)
            m_str = ''.join(m_str.split())
            if m_str in self.tag_to_names:
                for name in self.tag_to_names[m_str]:
                    try:
                        self.name_to_member[name].append(m)
                    except KeyError as e:
                        self.name_to_member[name] = [m]
        
        for name in self.name_to_member:
            print(f"name: {name} -> {self.name_to_member[name]}")

        self.connected = True        
        await ctx.send("> Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")
        await ctx.send("> Kinderaufsicht eingestaltet!!! 🚨🚨🚨")


    async def check_connected(self, context) -> bool:
        voice_state = context.member.voice
        return voice_state is not None

    async def on_ready(self):
        print(f"{bot.user.name} has connected to Discord!")

    async def set_to_muted(self, member: discord.Member, ctx):
        if member is None: return
        
        response = f"> {member} wird gemutet!"
        await ctx.send(response)
        
        await member.edit(mute=True)

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
    
    async def kick(self, member: discord.Member, ctx):
        if member is None: return
        response = f"> {member} wird gekickt!"
        await ctx.send(response)
        await member.edit(voice_channel=None)
    
    async def get_members_voice_channel(self, ctx):
        """ get all members of a voice channel the author of the message is currently in """
        voice_channel_id = ctx.author.voice.channel.id
        channel = ctx.guild.get_channel(voice_channel_id)
        members = channel.members
        return members
    
    
def setup(bot):
    bot.add_cog(Bot(bot))
