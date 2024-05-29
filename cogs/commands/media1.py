import discord
from discord.ext import commands


class akito222(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Media commands"""
  
    def help_custom(self):
		      emoji = '<a:AG_SocialMedia:1173088699572027465>'
		      label = "Media"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Media__(self, ctx: commands.Context):
        """`media` , `media setup <channel>` , `media remove <channel>`, `media config`"""