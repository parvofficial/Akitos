import discord
from discord.ext import commands


class gw1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Giveaway Commands"""
  
    def help_custom(self):
		      emoji = '<a:RH_GIVEAWAY_PING:1196072059684524033>'
		      label = "Giveaway"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Giveaway__(self, ctx: commands.Context):
        """`giveaway` , `gstart` ,`gcancle` ,`gend` , `greroll`"""