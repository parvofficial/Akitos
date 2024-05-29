import discord
from discord.ext import commands


class akito1111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Raidmode commands"""
  
    def help_custom(self):
		      emoji = '<a:sword:1172833336411037706>'
		      label = "Raidmode"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Automod__(self, ctx: commands.Context):
        """`automod` , `antispam on` , `antispam off` , `antilink off` ,  `antilink on`"""