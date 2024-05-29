import discord
from discord.ext import commands


class akito2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Voice commands"""
  
    def help_custom(self):
		      emoji = '<:merox_vcroles:1173088468088389723>'
		      label = "VcRoles"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __VcRoles__(self, ctx: commands.Context):
        """`vcrole bots add` , `vcrole bots remove` , `vcrole bots` , `vcrole config` , `vcrole humans add` , `vcrole humans remove` , `vcrole humans` , `vcrole reset` , `vcrole`"""