import discord
from discord.ext import commands


class akito11111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Fun commands"""
  
    def help_custom(self):
		      emoji = '<:s_fun:1077940661275328553>'
		      label = "Fun"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Fun__(self, ctx: commands.Context):
        """` tickle` , `kiss` , `hug` , `slap` , `pat` , `feed` , `pet` , `howgay` , `slots` , ` penis` , `meme` , `cat` , `iplookup`"""