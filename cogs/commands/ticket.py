import discord
from discord.ext import commands
from discord.ui import Button, View
import asyncio


class close(Button):
    def __init__(self):
        super().__init__(label=f'Close', emoji='🔒', style=discord.ButtonStyle.grey, custom_id="close")
        self.callback = self.button_callback
    
    async def button_callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Closing this ticket in 5 seconds.', ephemeral=True)
        await asyncio.sleep(5)
        await interaction.channel.delete()

class closeTicket(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(close())

class create(Button):
    def __init__(self):
        super().__init__(label='Create ticket', style=discord.ButtonStyle.grey, custom_id=f'create', emoji='🎫')
        self.callback = self.button_callback
    
    async def button_callback(self, interaction: discord.Interaction):
        categ = discord.utils.get(interaction.guild.categories, name='Ticket-category')
        
        for ch in categ.channels:
            if ch.topic == str(interaction.user):
                await interaction.response.send_message("**Warning:** Ticket limit reached. You already have 1 ticket of the allowed.", ephemeral=True)
                return
        
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True),
            discord.utils.get(interaction.guild.roles, name="Ticket Support"): discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        
        channel = await categ.create_text_channel(f"ticket-{interaction.user.name}", overwrites=overwrites, topic=str(interaction.user))
        await interaction.response.send_message(f"Ticket created {channel.mention}", ephemeral=True)
        
        embed = discord.Embed(
            description=f'{interaction.user.mention} your ticket has been created! We will help you as soon as possible.',
            color=0x2f3136
        )
        embed.set_footer(text=f'Akito')
        
        await channel.send(f'{discord.utils.get(interaction.guild.roles, name="Ticket Support").mention} Welcome {interaction.user.mention}', embed=embed, view=closeTicket())


class createTicket(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(create())

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="Ticket", description="Ticket Setup")
    async def ticket(self, ctx: commands.Context):
        ...
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def sendpanel(self, ctx: commands.Context):
        guild = ctx.guild
        
        role = await guild.create_role(name="Ticket Support")

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            role: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        # Create the ticket category and set permissions for the role in each channel
        category = await guild.create_category_channel(name="Ticket-category")
        for channel in category.channels:
            await channel.set_permissions(role, overwrite=overwrites)
        
        # Create the embed for the ticket creation message
        embed = discord.Embed(title='Ticket Creation', description='Click the button below to open a ticket.', color=0x2f3136)
        #embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text=f'{self.bot.user.name} - Ticket By akito')
        
        await ctx.send(embed=embed, view=createTicket())

    @commands.command()
    async def close(self, ctx: commands.Context):
        channel = ctx.channel
        if "ticket" not in channel.name.lower():
            embed = discord.Embed(description="This channel is not a ticket. Please use this command in a ticket channel.", color=0x2f3136)
            await ctx.send(embed=embed)
            return
        
        await ctx.send("Closing this ticket in 5 seconds.")
        await asyncio.sleep(5)
        await channel.delete()