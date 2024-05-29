import discord
from discord.ext import commands


class akito11111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Extra commands"""
  
    def help_custom(self):
		      emoji = '<a:moon:1172833540904337458>'
		      label = "Utility"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Utility__(self, ctx: commands.Context):
        """`botinfo` , `about` , `uptime` , `stats` , `invite` , `vote` , `serverinfo` , `userinfo` , `roleinfo` , `status` , `emoji` , `user` , `role` , `channel` , `boosts`, `steal` , `removeemoji` , `createsticker` , `unbanall` , `joined-at` , `ping` , `yt` , `github` , `vcinfo` , `channelinfo` , `note` , `notes` , `trashnotes` , `badges` , `list boosters` , `list inrole` , `list emojis` , `list bots` , `list admins` , `list invoice` , `list mods` , `list early` , `list activedeveloper` , `list createpos` , `list roles` , `ignore` , `ignore channel` , `ignore channel add` , `ignore channel remove` , `banner user` , `banner server`"""