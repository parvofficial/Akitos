from discord.ext import commands
from discord.ui import View, Button, button
import discord


class CalculatorView(View):
    def __init__(self, author: discord.Member):
        super().__init__()
        self.author = author
        self.value = ""
        self.message = None

    # Button interactions 
    @button(label="1", style=discord.ButtonStyle.grey, row=0)
    async def one(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "1")

    @button(label="2", style=discord.ButtonStyle.grey, row=0)
    async def two(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "2")

    @button(label="3", style=discord.ButtonStyle.grey, row=0)
    async def three(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "3")

    @button(label="4", style=discord.ButtonStyle.grey, row=1)
    async def four(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "4")

    @button(label="5", style=discord.ButtonStyle.grey, row=1)
    async def five(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "5")

    @button(label="6", style=discord.ButtonStyle.grey, row=1)
    async def six(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "6")

    @button(label="7", style=discord.ButtonStyle.grey, row=2)
    async def seven(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "7")

    @button(label="8", style=discord.ButtonStyle.grey, row=2)
    async def eight(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "8")

    @button(label="9", style=discord.ButtonStyle.grey, row=2)
    async def nine(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "9")

    @button(label="0", style=discord.ButtonStyle.grey, row=3)
    async def zero(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "0")

    @button(label="+", style=discord.ButtonStyle.blurple, row=3)
    async def add(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "+")

    @button(label="-", style=discord.ButtonStyle.blurple, row=3)
    async def subtract(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "-")

    @button(label="*", style=discord.ButtonStyle.blurple, row=3)
    async def multiply(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "*")

    @button(label="/", style=discord.ButtonStyle.blurple, row=3)
    async def divide(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "/")
        
    @button(label=".", style=discord.ButtonStyle.blurple, row=4)
    async def dot(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, ".")

    @button(label="=", style=discord.ButtonStyle.green, row=4)
    async def equals(self, interaction: discord.Interaction, button: Button):
        if interaction.user != self.author:
            return await interaction.response.send_message(
                "This is not your embed.", ephemeral=True
            )
        try:
            expression = self.value.strip().replace("\n", "")
            result = str(eval(expression))
            await self.update_embed(interaction, result)
            self.value = result  # Store the result for possible further calculations
        except:
            await self.update_embed(interaction, "Error")

    @button(label="Clear", style=discord.ButtonStyle.red, row=4)
    async def clear(self, interaction: discord.Interaction, button: Button):
        await self.update_value(interaction, "Clear")

    async def update_value(self, interaction: discord.Interaction, value: str):
        # Check if the person interacting is the author of the embed
        if interaction.user != self.author:
            return await interaction.response.send_message(
                "This content does not appear to be part of your embedded materials.", ephemeral=True
            )
        # Append the value or clear if "Clear"
        if value == "Clear":
            self.value = ""
        else:
            self.value += value
        # Update the embed with the new value
        await self.update_embed(interaction, self.value)

    async def update_embed(self, interaction: discord.Interaction, result: str):
        # Prepare the calculator's embed
        embed = discord.Embed(title="Calculator", description=f"```\n{result}\n```", color=discord.Color.blurple())
        
        # Set the embed footer to show who is currently using the calculator
        embed.set_footer(text=f"Calculations made by {self.author.display_name}", icon_url=self.author.avatar.url)
        
        # Edit the original message with the new embed
        await interaction.response.edit_message(embed=embed, view=self)
        
        # Store the updated message to avoid message loss
        self.message = interaction.message

class calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='calculator', help='Starts a calculator session', aliases=['calc', 'calculate', 'math'])
    async def calculator(self, ctx):
        """Starts a new calculator session."""
        # Ensure we pass the author to the view so it knows who triggered it
        view = CalculatorView(author=ctx.author)
        # We store the message so we know what to edit and update later
        view.message = await ctx.send('Calculator', mention_author=True, view=view)

# Add the cog to the bot
def setup(bot):
    bot.add_cog(calculator(bot))


