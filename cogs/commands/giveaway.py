import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.errors import CommandInvokeError
import random
import datetime
import json
import pymongo 
from pymongo import MongoClient
import os 
import traceback
import asyncio
import time
from discord.ui import Button, View
from discord import app_commands
from core import *
from utils.Tools import *
from core.Astroz import Astroz
import json

GIVEAWAYS_FILE_PATH = "database/giveaways.json"


alias = {
    "s":1,
    "m":60,
    "h":3600,
    "d":86400,
}

def convert(timestamp):
    try:
        value = int(timestamp[:-1])
        unit = timestamp[-1]
        if unit == 's':
            return value
        elif unit == 'm':
            return value * 60
        elif unit == 'h':
            return value * 3600
        elif unit == 'd':
            return value * 86400
    except ValueError:
        pass
    return -1


class Giveaways(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    def convert(self, time):
        unit = time[-1]
        if unit not in alias.keys():
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2
        return val * alias[unit]

    @commands.command(name="giveaway",aliases=["gway"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def _giveaway(self,ctx):
        """
        Shows the giveaway commands
        It shows how to use giveaway commands
        """
        em = discord.Embed(title="Giveaway Commands",color=0x41eeee)
        em.add_field(name="gstart <time> <winners> <message/prize>",value="Starts a giveaway for the specified amount of time.",inline=False)
        em.add_field(name="greroll <message_id>",value="Re rolls the winners of the giveaway.",inline=False)
        em.add_field(name="gend <message_id>",value="Ends the specified giveaway",inline=False)
        em.add_field(name="gcancle <message_id>", value="Canceled the giveaway", inline=False)
        await ctx.send(embed=em)

    @commands.command(name="gstart",aliases=["giveawaystart","gcreate"])
    @commands.cooldown(1, 1, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def _gstart(self,ctx,timee:str,winners:str,*,message):
        """
        Starts the giveaway
        """
        try:
            winners = int(winners.replace("w", ""))
            winners = int(winners)
        except ValueError:
            await ctx.send("The winners argument must be a number followed by 'w'. For example: '3w' for 3 winners.")
            return
        time = self.convert(timee)
        if time == -1:
            await ctx.send("Time entered incorrectly. It needs to be suffixed with s, m, h, or d for seconds, minutes, hours, or days, respectively. Example: '30s' for 30 seconds.")
            return
        end_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
        giveaway_info = {
            'host': ctx.author.id,
            'guild_id': ctx.guild.id,  # Including the guild ID in the giveaway info
            'time': timee,
            'winners_count': winners,
            'message': message,
            'end_time': end_time.timestamp()
        }
        try:
            with open(GIVEAWAYS_FILE_PATH, 'r') as giveaways_file:
                giveaways = json.load(giveaways_file)
        except FileNotFoundError:
            giveaways = []
        if not isinstance(giveaways, list):
            giveaways = [giveaways]
        giveaways.append(giveaway_info)
        with open(GIVEAWAYS_FILE_PATH, 'w') as giveaways_file:
            json.dump(giveaways, giveaways_file, indent=4)
        formatted_end_time = f"<t:{int(end_time.timestamp())}:R>"




        end_formatted_time = (end_time + datetime.timedelta(hours=5, minutes=30)).strftime('%B %d, %Y | %H:%M:%S')
        em = discord.Embed(title=f"{message}",description=f"<:Adisu_dot:1169954130337484820> Ends at: {formatted_end_time}\n<:Adisu_dot:1169954130337484820> Hosted by: {ctx.author.mention}\n",color=0x41eeee)
        em.description += "\n<:Adisu_dot:1169954130337484820> React with <a:giveaway:1128596785326194789> to participate"
        #end  = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
        em.set_footer(text=f"{winners} Winner(s) | Ends on • {end_formatted_time}")
        # if requirement.lower() != "none":
        #     role = discord.utils.get(ctx.guild.roles,id=int(requirement))
        # else:
        #     role = None
        await ctx.message.delete()
        msg = await ctx.send("<:Adisu_gw:1169954125077807167> **GIVEAWAY** <:Adisu_gw:1169954125077807167>",embed=em)
        #print(msg)
        gchannel = ctx.channel
        await msg.add_reaction("<a:giveaway:1128596785326194789>")
        await asyncio.sleep(time)
        cache_msg = await gchannel.fetch_message(msg.id)
        if "ended" not in cache_msg.content.lower():
            await self.gend(msg,em,winners,message,gchannel,end)

    @commands.has_permissions(manage_messages=True)
    async def gend(self,msg,em,winners,message,gchannel,end):
        cache_msg = await gchannel.fetch_message(msg.id)
        if cache_msg.author.id != self.bot.user.id:
            return await gchannel.send("Invalid Message ID.")
        for reaction in cache_msg.reactions:
            if str(reaction.emoji) == "<a:giveaway:1128596785326194789>":
                users = [user async for user in reaction.users()]
                #print(reaction.users())
                if len(users) == 1:
                    await msg.edit(content="<:Adisu_gw:1169954125077807167> **GIVEAWAY ENDED** <:Adisu_gw:1169954125077807167>")
                    return await gchannel.send(f"No one won the **{message}** giveaway!")

        try:
            winners2 = random.sample([user for user in users if not user.bot], k=winners)
        except ValueError:
            em.add_field(name="<:Adisu_dot:1169954130337484820> Winners",value="Not enough participants")
            #em.description += "\n**Winners:** "
            em.set_footer(text=f"{winners} Winners | Ended at • {end}")
            await msg.edit(content="<:Adisu_gw:1169954125077807167> **GIVEAWAY ENDED** <:Adisu_gw:1169954125077807167>")
            await msg.edit(embed=em)
            return await gchannel.send("Not enough participants")
        else:
            y = ", ".join(winner.mention for winner in winners2)
            x = ", ".join(winner.mention for winner in winners2)
            x = f"Hello, {y}! Congratulations on winning **{message}**. Well done!"
            em.add_field(name="<:Adisu_dot:1169954130337484820> Winners",value=f"{y}")
            #em.description += f"\n<:Adisu_dot:1169954130337484820> **&Reroll {msg.id}**"
            em.set_footer(text=f"{winners} Winner(s) | Ended at • {end}")
            em.color = 0x41eeee
            #
            await msg.edit(embed=em)
            await msg.edit(content="<:Adisu_gw:1169954125077807167> **GIVEAWAY ENDED** <:Adisu_gw:1169954125077807167>")
            view = View()
            view.add_item(Button(label="Jump to Giveaway",url=f"https://discord.com/channels/{msg.guild.id}/{msg.channel.id}/{msg.id}"))
            embed = discord.Embed(description="<a:a_Invite:1092183817931984996> [Click Here To Invite Akito To Your Server](https://discord.com/oauth2/authorize?client_id=1091588572777291856&permissions=8&scope=applications.commands%20bot)",color=0x41eeee)
            await gchannel.send(x,embed=embed, view=view)

    @commands.command(name="reroll",aliases=["re","greroll"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def _reroll(self,ctx,msg_id):
        """
        Get new winners for the giveaway
        Rerolls the winners again to choose new winners
        """
        reroll = await ctx.fetch_message(msg_id)
        if reroll.author.id != self.bot.user.id:
            return await ctx.send("Invalid Message ID.")
        em = reroll.embeds[0]
        message = em.title
        for reaction in reroll.reactions:
            if str(reaction.emoji) == "<a:giveaway:1128596785326194789>":
                users = [user async for user in reaction.users()]
                #print(reaction.users())
                if len(users) == 1:
                    await reroll.edit(content="<:Adisu_gw:1169954125077807167> **GIVEAWAY ENDED** <:Adisu_gw:1169954125077807167>")
                    return await ctx.send(f"A winner could not be decided for **{message}**!")
        em = reroll.embeds[0]
        message = em.title
        winners = em.footer.text[0]
        winners = int(winners)
        users = []
        async for user in reroll.reactions[0].users():
            users.append(user)
        users.pop(users.index(self.bot.user))
        winners2 = random.sample([user for user in users if not user.bot], k=winners)
        y = ", ".join(winner.mention for winner in winners2)
        em.set_field_at(0,name="<:Adisu_dot:1169954130337484820> Winners",value=f"{y}")
        await reroll.edit(embed=em)
        view = View()
        view.add_item(Button(label="Jump to Giveaway", url=f"https://discord.com/channels/{reroll.guild.id}/{reroll.channel.id}/{reroll.id}"))
        embedreroll = discord.Embed(description="<a:a_Invite:1092183817931984996> [Click Here To Invite Akito To Your Server](https://discord.com/oauth2/authorize?client_id=1091588572777291856&permissions=8&scope=applications.commands%20bot)",color=0x41eeee)
        await ctx.send(f"New winner(s): {y}! Congratulations, You won **{message}**!",embed=embedreroll, view=view)



    @commands.command(name="gend",aliases=["giveawayend","end"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def _end(self,ctx,msg_id):
        """
        Ends the giveaway before time
        """
        msg = await ctx.fetch_message(msg_id)
        if msg.author.id != self.bot.user.id:
            return await ctx.send("Invalid Message ID.")
        if "ended" in msg.content.lower():
            return await ctx.send("This giveaway has already ended.")
        else:
            em = msg.embeds[0]
            winners = em.footer.text[0]
            winners = int(winners)
            message = em.title
            gchannel = ctx.channel
            x = em.description.split("\n")
            x = x[1]
            x = x.split(":")
            x = x[1]
            x = x.replace("*","")
            time = self.convert(x)
            end  = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
            end = datetime.datetime.strftime(end,"%d %b %Y")
            await self.gend(msg,em,winners,message,gchannel,end)

    @commands.command(name="gcancle", aliases=["giveawaycancle"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def _gcancle(self, ctx, msg_id: int):
        """
        Cancle the giveaway
        """
        try:
            msg = await ctx.channel.fetch_message(msg_id)
        except (discord.NotFound, discord.Forbidden, discord.HTTPException) as e:
            return await ctx.send(f"Could not fetch the message: {e}")

        if msg.author.id != self.bot.user.id:
            return await ctx.send("Invalid Message ID.")

        if "ended" in msg.content.lower():
            return await ctx.send("This giveaway has already ended.")

      # Here we cancel the giveaway
        with open(GIVEAWAYS_FILE_PATH, 'r') as giveaways_file:
            giveaways = json.load(giveaways_file)

      # Filtering out the giveaway to be canceled
        giveaways = [giveaway for giveaway in giveaways if str(giveaway.get('message')) != str(msg.embeds[0].title) or int(giveaway.get('host')) != ctx.author.id]

        with open(GIVEAWAYS_FILE_PATH, 'w') as giveaways_file:
            json.dump(giveaways, giveaways_file, indent=4)

      # Editing the message to reflect that the giveaway has been canceled
        em = msg.embeds[0]
        em.set_footer(text="This giveaway has been canceled.")
        await msg.edit(content=":x: **GIVEAWAY CANCELED** :x:", embed=em)
        for reaction in msg.reactions:
            if str(reaction.emoji) == '<a:giveaway:1128596785326194789>':
                await reaction.clear()
        await ctx.send("Giveaway canceled.")
      
def setup(bot):
    bot.add_cog(Giveaways(bot))