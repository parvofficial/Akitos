from __future__ import annotations
from discord.ext import commands
import discord
import aiohttp
import colorama
from colorama import Fore
import json
import jishaku, time
import asyncio
import aiosqlite
import typing
from utils.config import OWNER_IDS, EXTENSIONS, No_Prefix
from utils import getConfig, updateConfig, DotEnv
from .Context import Context
from discord.ext import commands, tasks


class Astroz(commands.AutoShardedBot):

    def __init__(self, *arg, **kwargs):
        self.topgg_headers = {
            "Authorization":
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEwMTI2MjcwODgyMzIxNjUzNzYiLCJib3QiOnRydWUsImlhdCI6MTY3MDU4MzE3NH0.WULUuUMpTCqzHt0nPk3MqnpeJHF3YNgBo8"
        }
        intents = discord.Intents.all()
        intents.presences = False
        intents.members = True
        super().__init__(command_prefix=self.get_prefix,
                         case_insensitive=True,
                         intents=intents,
                         status=discord.Status.dnd,
                         strip_after_prefix=True,
                         owner_ids = OWNER_IDS ,
                         allowed_mentions=discord.AllowedMentions(
                             everyone=False, replied_user=False, roles=False),
                         sync_commands_debug=True,
                         sync_commands=True,
                         shard_count=4)

    async def on_ready(self):
        print(Fore.RED+"Connected as {}".format(self.user))


    async def setup_hook(self):

        self.db = await aiosqlite.connect("main.db")
        self.cd = commands.CooldownMapping.from_cooldown(1, 10, commands.BucketType.user)
        cur = await self.db.cursor()
        
        await cur.execute("CREATE table if not exists guildpremium(guild_id TEXT NOT NULL, end_time TEXT, activator TEXT, tier TEXT)")
        await cur.execute("CREATE table if not exists Userpremium(user_id TEXT NOT NULL, end_time TEXT, prime_count TEXT, tier TEXT)")
        await cur.execute("create table if not exists badge(user_id TEXT, badge TEXT)")

    async def on_connect(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.streaming,name=f".help",
                                                                                           url="https://www.twitch.tv/#"))




        
        async with aiohttp.ClientSession(
                headers=self.topgg_headers) as session:
            async with session.post(
                    "https://top.gg/api/bots/10/stats",
                    json={
                        "server_count": len(self.guilds),
                        "shard_count": len(self.shards)
                    }) as r:
                print(Fore.LIGHTBLUE_EX+"Posted Data On Top GG")


                        

    async def send_raw(self, channel_id: int, content: str,
                       **kwargs) -> typing.Optional[discord.Message]:
        await self.http.send_message(channel_id, content, **kwargs)

                           

    async def invoke_help_command(self, ctx: Context) -> None:
        """Invoke the help command or default help command if help extensions is not loaded."""
        return await ctx.send_help(ctx.command)

        

    async def fetch_message_by_channel(
            self, channel: discord.TextChannel,
            messageID: int) -> typing.Optional[discord.Message]:
        async for msg in channel.history(
                limit=1,
                before=discord.Object(messageID + 1),
                after=discord.Object(messageID - 1),
        ):
            return msg


            

    async def get_prefix(self, message: discord.Message):
        with open('info.json', 'r') as f:
            p = json.load(f)
        if message.author.id in p["np"]:
            return commands.when_mentioned_or('.', '')(self, message)
        else:
            if message.guild and message.guild != '.':  # Add condition to check if guild prefix is not '&'
                data = getConfig(message.guild.id)
                prefix = data["prefix"]
                return commands.when_mentioned_or(prefix, '.')(self, message)
            else:
                return commands.when_mentioned_or('.')(self, message)



                

    async def on_message_edit(self, before, after):
        ctx: Context = await self.get_context(after, cls=Context)
        if before.content != after.content:
            if after.guild is None or after.author.bot:
                return
            if ctx.command is None:
                return
            if type(ctx.channel) == "public_thread":
                return
            await self.invoke(ctx)
        else:
            return
