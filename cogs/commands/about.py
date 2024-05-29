import discord
from discord.ext import commands
from discord.ui import Button, View

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user in message.mentions and ('about' in message.content.lower() or '.about' in message.content.lower()):
            ctx = await self.bot.get_context(message)
            await self.bot.invoke(ctx)

    @commands.command(name='about')
    async def about(self, ctx):
        embed = discord.Embed(title='About Akito', color=0x11100d)

        embed.add_field(name='', value='Akito is the Best bot with over 400+ commands. It protects your server and provides various features.', inline=False)
        embed.add_field(name='Commands', value='You can use `.help` to see a list of available commands.', inline=False)      
        embed.add_field(name='**<:clyde:1220213564812427327>・DEVELOPER**', value='[Akito Devlopment 💝](https://discord.com/invite/GZNYym6pfc) ', inline=False)

        embed.set_author(name="About Akito",icon_url=self.bot.user.display_avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=self.bot.user.avatar.url)

  #check server


        invite_link = 'https://discord.com/api/oauth2/authorize?client_id=1173097825614180463&permissions=8&scope=bot'
        support_server_link = 'https://discord.com/invite/GZNYym6pfc'
      

        buttons = [
            Button(style=discord.ButtonStyle.link, label='Invite Akito', url=invite_link),
            Button(style=discord.ButtonStyle.link, label='Join Support Server', url=support_server_link)
        ]

        view = View()
        view.add_item(buttons[0])
        view.add_item(buttons[1])

        await ctx.send(embed=embed, view=view)