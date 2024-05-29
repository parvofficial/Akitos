import discord
from discord.ext import commands


class akito22(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Verification Commands"""
  
    def help_custom(self):
		      emoji = '<a:Black_Verification:1194495008405999626>'
		      label = "Verification"
		      description = "Shows You Verification Commands"
		      return emoji, label, description

    @commands.group()
    async def __Verification__(self, ctx: commands.Context):
        """`verification enable` , `verification disable` , `verification config`"""