import discord
from discord.ext import commands
import json

class akito1111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Ticket commands"""  

    def help_custom(self):
		      emoji ='<a:tid:1196082798688215040>'
		      label = "Ticket"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Tickets__(self, ctx: commands.Context):
        """`ticket` , `sendpanel` , `adduser` , `removeuser`"""
       
    

    
   

