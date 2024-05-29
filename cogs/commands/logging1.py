import discord
from discord.ext import commands


class akito111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Logging Commands"""
  
    def help_custom(self):
		      emoji = '<:cmds:1174716762609160263>'
		      label = "Logging"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Logging__(self, ctx: commands.Context):
        """`logall disable`, `logall enable`"""