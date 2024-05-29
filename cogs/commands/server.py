import discord
from discord.ext import commands

class akito11111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Welcome commands"""
  
    def help_custom(self):
		      emoji = '<a:server:1173089023997255681>'
		      label = "Server"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Server__(self, ctx: commands.Context):
        """`setup` , `setup staff` , `setup girl` , `setup friend` , `setup vip` , `setup guest` , `setup owner` , `setup coowner` , `setup headadmin` , `setup admin` , `setup girladmin` , `setup headmod` , `setup mod` , `setup girlmod` , `setup config` , `staff` , `girl` , `friend` , `vip` , `guest` , `owner` , `coowner` , `headadmin` , `admin` , `girladmin ` , `headmod` , `mod` , `girlmod` , `remove staff` , `remove girl` , `remove friend` , `remove vip` , `remove guest` , `remove owner` , `remove coowner` , `remove headadmin` , `remove admin` , `remove girladmin` , `remove headmod` , `remove mod` , `remove girlmod`  """

