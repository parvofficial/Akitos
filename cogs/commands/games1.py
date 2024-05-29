import discord
from discord.ext import commands


class akito1111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Games commands"""
  
    def help_custom(self):
		      emoji = '<a:Games:1172833362768052248>'
		      label = "Games"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Games__(self, ctx: commands.Context):
        """`hangman` , `typerace` , `rps` , `reaction` , `tic-tac-toe` , `wordle` , `2048` , `memory-game` , `number-slider` , `battleship` , `country-guesser`"""