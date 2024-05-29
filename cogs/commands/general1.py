import discord
from discord.ext import commands


class akito11(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""
  
    def help_custom(self):
		      emoji = '<a:general:1173088780253679618>'
		      label = "General"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __General__(self, ctx: commands.Context):
        """`afk` , `avatar` , `banner` , `servericon` , `membercount` , `poll` , `hack` , `token` , `users` , `italicize` , `strike` , `quote` , `code` , `bold` , `censor` , `underline` , `gender` , `wizz` , `shorten` , `urban` , `rickroll` , `hash` , `snipe` , `roleall` ,`jail`"""