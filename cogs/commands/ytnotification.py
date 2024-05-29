import discord
from discord.ext import commands
from discord.ui import Button, View
import json
import os

SETTINGS_FILE = 'ytnotification.json'

# Load settings from a JSON file
def load_settings():
    if os.path.isfile(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    return {'notifications_enabled': {}, 'youtube_channel_links': {}, 'guild_channel_map': {}}

# Save settings to a JSON file
def save_settings(data):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Cog for YouTube Notification
class ytnotification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        settings = load_settings()
        # Load settings for notifications, YouTube channel links, and guild channel mappings
        self.notifications_enabled = settings.get('notifications_enabled', {})
        self.youtube_channel_links = settings.get('youtube_channel_links', {})
        self.guild_channel_map = settings.get('guild_channel_map', {})

    @commands.hybrid_command(name='setchannel')
    async def set_channel(self, ctx: commands.Context, channel_id: int):
        # Command to set the notification channel
        self.guild_channel_map[ctx.guild.id] = channel_id
        await ctx.send(f'Notification channel set to <#{channel_id}>')
        save_settings({
            'notifications_enabled': self.notifications_enabled,
            'youtube_channel_links': self.youtube_channel_links,
            'guild_channel_map': self.guild_channel_map
        })

    @commands.hybrid_command(name='setytlink')
    async def set_yt_link(self, ctx: commands.Context, yt_link: str):
        # Command to set the YouTube channel link
        self.youtube_channel_links[ctx.guild.id] = yt_link
        await ctx.send(f'YouTube channel link set to {yt_link}')

    async def enable_button(self, interaction: discord.Interaction, button: Button):
        # Method to handle enabling notifications from the button
        guild_id = interaction.guild.id
        if self.youtube_channel_links.get(guild_id):
            self.notifications_enabled[guild_id] = True
            await interaction.response.send_message('YouTube notifications enabled. Make sure to set the YouTube channel link first with /setytlink command if you haven\'t already.')
        else:
            await interaction.response.send_message('YouTube channel link is not set. Please set it first with /setytlink command.')
        # Save updated settings
        save_settings({
            'notifications_enabled': self.notifications_enabled,
            'youtube_channel_links': self.youtube_channel_links,
            'guild_channel_map': self.guild_channel_map
        })

    async def disable_button(self, interaction: discord.Interaction, button: Button):
        # Method to handle disabling notifications from the button
        guild_id = interaction.guild.id
        self.notifications_enabled[guild_id] = False
        await interaction.response.send_message('YouTube notifications disabled.')
        # Save updated settings
        save_settings({
            'notifications_enabled': self.notifications_enabled,
            'youtube_channel_links': self.youtube_channel_links,
            'guild_channel_map': self.guild_channel_map
        })

    async def send_notification(self, guild_id, video_info):
        # Send a YouTube video notification to the set channel
        if self.notifications_enabled.get(guild_id):
            channel_id = self.guild_channel_map.get(guild_id)
            if channel_id:
                channel = self.bot.get_channel(channel_id)
                if channel:
                    # Create an embed object for the YouTube video notification
                    embed = discord.Embed(
                        title=video_info['title'],
                        url=video_info['url'],
                        description=video_info['description'],
                        colour=discord.Colour.red()
                    )
                    embed.set_author(name=video_info['channel_name'])
                    embed.set_thumbnail(url=video_info['thumbnail_url'])
                    embed.set_footer(text='YouTube Notification')
                    # Send the embed to the specified channel
                    await channel.send(embed=embed)

class YTNotificationView(View):
    def __init__(self, cog: ytnotification):
        super().__init__()
        self.add_item(Button(label='Enable', style=discord.ButtonStyle.success, custom_id="persistent_view:enable"))
        self.add_item(Button(label='Disable', style=discord.ButtonStyle.danger, custom_id="persistent_view:disable"))
        self.cog = cog

    @discord.ui.button(label="Enable", style=discord.ButtonStyle.success, custom_id="persistent_view:enable")
    async def enable_button(self, interaction: discord.Interaction, button: Button):
        await self.cog.enable_button(interaction, button)

    @discord.ui.button(label="Disable", style=discord.ButtonStyle.danger, custom_id="persistent_view:disable")
    async def disable_button(self, interaction: discord.Interaction, button: Button):
        await self.cog.disable_button(interaction, button)

def setup(bot):
    yt_notification_cog = ytnotification(bot)
    bot.add_cog(yt_notification_cog)
    bot.add_view(YTNotificationView(yt_notification_cog))
    save_settings({
        'notifications_enabled': yt_notification_cog.notifications_enabled,
        'youtube_channel_links': yt_notification_cog.youtube_channel_links,
        'guild_channel_map': yt_notification_cog.guild_channel_map
    })