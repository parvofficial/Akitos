import discord
from discord.ext import commands


class pfps1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Pfp Commands"""
  
    def help_custom(self):
		      emoji = '<a:awful_pfp:1194313364202074205>'
		      label = "Pfp"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Pfp__(self, ctx: commands.Context):
        """`pic`, `boys` , `girls`, `couples`, `anime`"""