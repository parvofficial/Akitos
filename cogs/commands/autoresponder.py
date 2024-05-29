import discord
from discord.ext import commands


class akito2222(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  """Autoresponder commands"""

  def help_custom(self):
    emoji = '<:auto:1196088590183190588>'
    label = "Autoresponder"
    description = ""
    return emoji, label, description

  @commands.group()
  async def __Autoresponder__(self, ctx: commands.Context):
    """`ar` , `ar create` , `ar delete` , `ar edit` , `ar list` , `ar config`"""