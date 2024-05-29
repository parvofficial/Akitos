import discord
from traceback import format_exception
from discord.ext import commands
from difflib import get_close_matches
import io
import textwrap
import datetime
import sys
from contextlib import suppress
from core import Context
from core.Astroz import Astroz
from core.Cog import Cog
from utils.Tools import getConfig
from itertools import chain
import psutil
import time
import datetime
import platform
import os
import logging
import motor.motor_asyncio
from pymongo import MongoClient
import requests
import motor.motor_asyncio as mongodb
from typing import *
from utils import *
import json
from utils import help as vhelp
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator

from core import Cog, Astroz, Context
from typing import Optional
from discord import app_commands
start_time = time.time()
client = Astroz()


def datetime_to_seconds(thing: datetime.datetime):
    current_time = datetime.datetime.fromtimestamp(time.time())
    return round(
        round(time.time()) +
        (current_time - thing.replace(tzinfo=None)).total_seconds())

client = Astroz()



class HelpCommand(commands.HelpCommand):

  async def on_help_command_error(self, ctx, error):
    serverCount = len(self.client.guilds)
    users = sum(g.member_count for g in self.client.guilds
                    if g.member_count != None)

    total_members = sum(g.member_count for g in self.client.guilds
                            if g.member_count != None)
    LEGEND = [
      commands.CommandOnCooldown, commands.CommandNotFound,
      discord.HTTPException, commands.CommandInvokeError
    ]
    if not type(error) in LEGEND:
      await self.context.reply(f"Unknown Error Occurred\n{error.original}",
                               mention_author=False)
    else:
      if type(error) == commands.CommandOnCooldown:
        return

        return await super().on_help_command_error(ctx, error)

  async def command_not_found(self, string: str) -> None:
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(
        title="<:blacklist:1158791166867812495> Blacklisted",
        description=
        "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/)",
        color=0x00FFCA)
      await self.context.reply(embed=embed, mention_author=False)
    else:

      if string in ("security", "anti", "antinuke"):
        cog = self.context.bot.get_cog("antinuke")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      else:
        msg = f"Command `{string}` is not found...\n"
        piyush = await self.context.bot.fetch_user(1140999483770023977)
        cmds = (str(cmd) for cmd in self.context.bot.walk_commands())
        mtchs = get_close_matches(string, cmds)
        if mtchs:
          for okaay, okay in enumerate(mtchs, start=1):
            msg += f"Did You Mean: \n`[{okaay}]`. `{okay}`\n"
        embed1 = discord.Embed(
          color=0x11100d,
          title=f"Command `{string}` is not found...\n",
          description=f"Did You Mean: \n`[{okaay}]`. `{okay}`\n")

        return None

  async def send_bot_help(self, mapping):
    await self.context.typing()
    with open('ignore.json', 'r') as heck:
      randi = json.load(heck)
    with open('blacklist.json', 'r') as f:
      bled = json.load(f)
    if str(self.context.author.id) in bled["ids"]:
      embed = discord.Embed(
        title="<:blacklist:1158791166867812495> Blacklisted",
        description=
        "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/)",
        color=0x11100d)
      return await self.context.reply(embed=embed, mention_author=False)
    elif str(self.context.channel.id) in randi["ids"]:
      return None
    data = getConfig(self.context.guild.id)
    prefix = data["prefix"]
    perms = discord.Permissions.none()
    perms.read_messages = True
    perms.external_emojis = True
    perms.send_messages = True
    perms.manage_roles = True
    perms.manage_channels = True
    perms.ban_members = True
    perms.kick_members = True
    perms.manage_messages = True
    perms.embed_links = True
    perms.read_message_history = True
    perms.attach_files = True
    perms.add_reactions = True
    perms.administrator = True
    inv = discord.utils.oauth_url(self.context.bot.user.id, permissions=perms)
    filtered = await self.filter_commands(self.context.bot.walk_commands(),
                                          sort=True)
    LEGEND = await self.context.bot.fetch_user(1140999483770023977)
    embed = discord.Embed(
      title="**Help Command Overview **:",
      description=
      f"• **Prefix for this server is** `{prefix}`\n• **Total Commands: ** **{len(set(self.context.bot.walk_commands()))}** | **Usable by you (here): ** **{len(set(filtered))}**\n• **Links ~** [Invite](https://discord.com/api/oauth2/authorize?client_id=1173097825614180463&permissions=8&scope=bot) | [Support](https://discord.gg/)\n• **Type** `{prefix}help <command | module>` for more info.```    <> - Required | [] - Optional``` ",
      color= 0x41eeee)
    embed.set_thumbnail(url=self.context.bot.user.display_avatar.url)

    embed.set_footer(
      text="Made By ~ Akito Devlopment 💝",
      icon_url="https://media.discordapp.net/attachments/1167688002252853250/1173169144418545695/Picsart_23-11-12_10-07-30-575.png?ex=6562f9e8&is=655084e8&hm=48d9c6b2e7d5b41a317b0948d00e9e650ffc20333fe9f3bf0c2efcc0b33c0895&")

    embed.add_field(name="**__Main Modules __**",
                    value="""
<:xD:1172832526314766386> AntiNuke\n<a:RH_GIVEAWAY_PING:1196072059684524033> Giveaway \n<:cmds:1174716762609160263> Logging\n<:nexus_mod:1194635792669216809> Moderation\n<a:moon:1172833540904337458> Utility\n<a:Games:1172833362768052248> Games\n<a:_welcome_:1172833474533654609> Welcome\n<a:sword:1172833336411037706> Raidmode\n<a:Musicz:1172832937444651119> Music""",
                    inline=True)  

    embed.add_field(name="**__Basics Modules __**",
                    value="""<a:server:1173089023997255681> Server  \n<a:Black_Verification:1194495008405999626> Verification\n<a:general:1173088780253679618> General\n<a:AG_SocialMedia:1173088699572027465> Media\n<a:tid:1196082798688215040> Ticket\n<a:awful_pfp:1194313364202074205> Pfp\n<:auto:1196088590183190588> Autoresponder \n<a:voicegoogle:1173088555229270130> Voice\n<:merox_vcroles:1173088468088389723> VcRoles\n<:vanity:1173088377965396059> Vanityroles""",
                    inline=True) 
    #embed.add_field(name="__UPDATES__",
                    #value=f"""MUSIC & VERIFICATION COMMAND DISABLED BECAUSE OF BUG'S AFTER BUGS FIXED COMMANDS WILL ENABLED """,
                   # inline=False)
    embed.set_author(name=self.context.author.name,
                     icon_url=self.context.author.display_avatar.url)
    embed.timestamp = discord.utils.utcnow()

    # Create the invite button
    invite_button = discord.ui.Button(
        style=discord.ButtonStyle.link,
   #     emoji='<a:985:1151531674207789189>',
        label="Invite Me",
        url="https://discord.com/api/oauth2/authorize?client_id=1173097825614180463&permissions=8&scope=bot"
    )
    support_button = discord.ui.Button(
        style=discord.ButtonStyle.link,
   #     emoji='<a:999:1151531721381134377>',
        label="Support Server",
      url="https://discord.gg/"
    )
    Vote_button = discord.ui.Button(
        style=discord.ButtonStyle.link,
   #     emoji='<a:982:1142461636389650542>',
        label="Vote Me",
      url="https://top.gg/bot/"
    )    

    view = vhelp.View(mapping=mapping, ctx=self.context, homeembed=embed, ui=2)
    view.add_item(invite_button)
    view.add_item(support_button)
    view.add_item(Vote_button)    

    await self.context.reply(embed=embed, mention_author=True, view=view)

  async def send_command_help(self, command):
    with open('ignore.json', 'r') as heck:
      randi = json.load(heck)
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(
        title="<a:no:1173190365076017192>  Blacklisted",
        description=
        "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/)",
        color=0x00FFCA)
      await self.context.reply(embed=embed, mention_author=False)
    elif str(self.context.channel.id) in randi["ids"]:
      return None
    else:
      hacker = f">>> {command.help}" if command.help else '>>> No Help Provided...'
      embed = discord.Embed(
        description=
        f"""```yaml\n- [] = optional argument\n- <> = required argument\n- Do NOT Type These When Using Commands !```\n{hacker}""",
        color=0x00FFCA)
      alias = ' | '.join(command.aliases)

      embed.add_field(name="**Aliases**",
                      value=f"{alias}" if command.aliases else "No Aliases",
                      inline=False)
      embed.add_field(name="**Usage**",
                      value=f"`{self.context.prefix}{command.signature}`\n")
      embed.set_author(name=f"{command.cog.qualified_name.title()}",
                       icon_url=self.context.bot.user.display_avatar.url)
      await self.context.reply(embed=embed, mention_author=False)

  def get_command_signature(self, command: commands.Command) -> str:
    parent = command.full_parent_name
    if len(command.aliases) > 0:
      aliases = ' | '.join(command.aliases)
      fmt = f'[{command.name} | {aliases}]'
      if parent:
        fmt = f'{parent}'
      alias = f'[{command.name} | {aliases}]'
    else:
      alias = command.name if not parent else f'{parent} {command.name}'
    return f'{alias} {command.signature}'

  def common_command_formatting(self, embed_like, command):
    embed_like.title = self.get_command_signature(command)
    if command.description:
      embed_like.description = f'{command.description}\n\n{command.help}'
    else:
      embed_like.description = command.help or 'No help found...'

  async def send_group_help(self, group):
    with open('blacklist.json', 'r') as f:
      idk = json.load(f)
    with open('ignore.json', 'r') as heck:
      randi = json.load(heck)
    if str(self.context.author.id) in idk["ids"]:
      embed = discord.Embed(
        title="<a:no:1173190365076017192>  Blacklisted",
        description=
        "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/)",
        color=0x00FFCA)
      await self.context.reply(embed=embed, mention_author=False)
    elif str(self.context.channel.id) in randi["ids"]:
      return None
    else:
      entries = [(
        f"`{self.context.prefix}{cmd.qualified_name}`",
        f"{cmd.short_doc if cmd.short_doc else 'No Description Provided...'}\n\n"
      ) for cmd in group.commands]
    paginator = Paginator(source=FieldPagePaginator(
      entries=entries,
      title=f"{group.qualified_name} Commands",
      description="```yaml\n- [] = optional argument\n- <> = required argument\n- Do NOT Type These When Using Commands !```",
      color=0x00FFCA,
      per_page=10),
                          ctx=self.context)
    await paginator.paginate()

  async def send_cog_help(self, cog):
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    with open('ignore.json', 'r') as heck:
      randi = json.load(heck)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(
        title="<a:no:1173190365076017192>  Blacklisted",
        description=
        "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/)",
        color=0x00FFCA)
      return await self.context.reply(embed=embed, mention_author=False)
    elif str(self.context.channel.id) in randi["ids"]:
      return None
    #await self.context.typing()
    entries = [(
      f"`{self.context.prefix}{cmd.qualified_name}`",
      f"{cmd.short_doc if cmd.short_doc else 'No Description Provided...'}\n\n"
    ) for cmd in cog.get_commands()]
    paginator = Paginator(source=FieldPagePaginator(
      entries=entries,
      title=f"{cog.qualified_name.title()} ({len(cog.get_commands())})",
      description="```yaml\n- [] = optional argument\n- <> = required argument\n- Do NOT Type These When Using Commands !```\n\n",
      color=0x00FFCA,
      per_page=10),
                          ctx=self.context)
    await paginator.paginate()


class Help(Cog, name="help"):

  def __init__(self, client: Astroz):
    self._original_help_command = client.help_command
    attributes = {
      'name':
      "help",
      'aliases': ['h'],
      'cooldown':
      commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.user),
      'help':
      'Shows help about bot, a command or a category'
    }
    client.help_command = HelpCommand(command_attrs=attributes)
    client.help_command.cog = self

  async def cog_unload(self):
    self.help_command = self._original_help_command