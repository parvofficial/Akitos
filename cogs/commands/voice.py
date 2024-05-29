import discord
from discord.ext import commands


class akito111111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Voice commands"""
  
    def help_custom(self):
		      emoji = '<a:voicegoogle:1173088555229270130>'
		      label = "Voice"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Voice__(self, ctx: commands.Context):
        """`voice` , `voice kick` , `voice kickall` , `voice mute` , `voice muteall` , `voice unmute` , `voice unmuteall` , `voice deafen` , `voice deafenall` , `voice undeafen` , `voice undeafenall` , `voice moveall`"""






