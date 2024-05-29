import discord
from discord.ext import commands


class akito11111111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Vanityroles"""
  
    def help_custom(self):
		      emoji = '<:vanity:1173088377965396059>'
		      label = "VanityRoles"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __VanityRoles__(self, ctx: commands.Context):
        """`vanityroles setup` , `vanityroles show` , `vanityroles reset`"""