import discord
from discord.ext import commands
from core import Cog, Astroz, Context
from utils.Tools import *
from typing import *


class greet(Cog):
    def __init__(self, bot: Astroz):
        self.bot = bot
        
    @Cog.listener()
    async def on_member_join(self, member):
        data = getDB(member.guild.id)
        msg = data["welcome"]["message"]
        chan = list(data["welcome"]["channel"])
        emtog = data["welcome"]["embed"]
        emping = data["welcome"]["ping"]
        emimage = data["welcome"]["image"]
        emthumbnail = data["welcome"]["thumbnail"]
        emautodel = data["welcome"]["autodel"]
        emfooter = data["welcome"]["footer"]
        user = member
        if chan == []:
            return
        else:
            if "<<server.name>>" in msg:
               msg = msg.replace("<<server.name>>", "%s" % (user.guild.name))
            if "<<server.member_count>>" in msg:
              msg = msg.replace("<<server.member_count>>", "%s" % (user.guild.member_count))
            if "<<user.name>>" in msg:
              msg = msg.replace("<<user.name>>", "%s" % (user))
            if "<<user.mention>>" in msg:
              msg = msg.replace("<<user.mention>>", "%s" % (user.mention))
            if "<<user.created_at>>" in msg:
              msg = msg.replace("<<user.created_at>>", f"<t:{int(user.created_at.timestamp())}:F>")
            if "<<user.joined_at>>" in msg:
              msg = msg.replace("<<user.joined_at>>", f"<t:{int(user.joined_at.timestamp())}:F>")
            if msg == "":
              msg = ""
            else:
              msg = msg
            if emping == True:
              emping = f"**Hey {user.mention} Welcome To {user.guild.name}**"
            else:
              emping = ""
            if emautodel == 0:
              emautodel = None
            else:
              emautodel = emautodel
            em = discord.Embed(description=msg, color=0x41eeee)
            em.set_author(name=user, icon_url=member.avatar.url if member.avatar else member.default_avatar.url)
            em.timestamp = discord.utils.utcnow()
            if emimage == "":
                em.set_image(url=None)
            else:
                em.set_image(url=emimage)
            if emthumbnail == "":
                em.set_thumbnail(url=None)
            else:
                em.set_thumbnail(url=emthumbnail)
            if user.guild.icon is not None:
                em.set_footer(text=emfooter, icon_url=user.guild.icon.url)
            if emtog == True:
                for chh in chan:
                    ch = self.bot.get_channel(int(chh))
                    if ch:
                        await ch.send(emping, embed=em, delete_after=emautodel)
            else:
                for chh in chan:
                    ch = self.bot.get_channel(int(chh))
                    if ch and emtog == False:
                        await ch.send(msg, delete_after=emautodel)