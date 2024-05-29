from __future__ import annotations
from discord.ext import commands
from utils.Tools import *
from discord import *
from utils.config import OWNER_IDS, No_Prefix
import json, discord
import typing
import os
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator
#from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator
#from PIL import Image, ImageFont, ImageDraw, ImageChops
#os.system("pip install Pillow")
from typing import Optional


#Cyg90MAh7a0
class Owner(commands.Cog):

    def __init__(self, client):
        self.client = client
        #self.color = 0x2f3136
    
    #@commands.command(name="pft")
    @commands.is_owner()
    async def pft(self, ctx, member: Union[discord.Member, discord.User]=None):
        if not member:
            member = ctx.author
        
        name = str(member)
        member = discord.utils.get(self.client.users, id=member.id)
        profile_base = Image.open("Profile-base.png").convert("RGBA")
        pfp = member.avatar_url_as(sizs=256)
        BIOD = BytesIO(await pfp.read())
        pfp = Image.open(BIOD).convert("RGBA")
    
 #   pfp = Image.open(BIOD).convert("RGBA")

    

        name = f"{name[:15]}..." if len(name)>15 else name

    

        draw = ImageDraw.Draw(BIOD)

        pfp = circle(pfp,(215,215))

        font = ImageFont.truetype("Nunito-Regular.ttf", 38)

        subufont = ImageFont.truetype("Nunito-Regular.ttf", 27)
        subbfont = ImageFont.truetype("Nunito-Regular.ttf", 44)
        with BytesIO() as a:
            a.seek(0)
            await ctx.send(file=discord.File(a, "profile.png"))



    @commands.command(name="slist")
    @commands.is_owner()
    async def _slist(self, ctx):
        hasanop = ([hasan for hasan in self.client.guilds])
        hasanop = sorted(hasanop,
                         key=lambda hasan: hasan.member_count,
                         reverse=True)
        entries = [
            f"`[{i}]` | [{g.name}](https://discord.com/channels/{g.id}) - {g.member_count}"
            for i, g in enumerate(hasanop, start=1)
        ]
        paginator = Paginator(source=DescriptionEmbedPaginator(
            entries=entries,
            description="",
            title=f"Server List of  Akito - {len(self.client.guilds)}",
            color=0x2f3136,
            per_page=10),
                              ctx=ctx)
        await paginator.paginate()



    @commands.command(name="restart", help="Restarts the client.")
    @commands.is_owner()
    async def _restart(self, ctx: Context):
        await ctx.reply("Restarting! <a:cx_tick:1173190431295676416> Pls Wait It Takes 5-6 Second")
        restart_program()

    @commands.command(name="shutdown", help="Shutdown the client.")
    @commands.is_owner()
    async def _shutdown(self, ctx: Context):
        await ctx.reply("shuting down")
        ctx.bot.logout()

    @commands.command(name="sync", help="Syncs all database.")
    @commands.is_owner()
    async def _sync(self, ctx):
        await ctx.reply("Syncing...", mention_author=False)
        with open('anti.json', 'r') as f:
            data = json.load(f)
        for guild in self.client.guilds:
            if str(guild.id) not in data['guild']:
                data['guilds'][str(guild.id)] = 'on'
                with open('anti.json', 'w') as f:
                    json.dump(data, f, indent=4)
            else:
                pass
        with open('config.json', 'r') as f:
            data = json.load(f)
        for op in data["guilds"]:
            g = self.client.get_guild(int(op))
            if not g:
                data["guilds"].pop(str(op))
                with open('config.json', 'w') as f:
                    json.dump(data, f, indent=4)

    @commands.group(name="blacklist",
                    help="let's you add someone in blacklist",
                    aliases=["bl"])
    @commands.is_owner()
    async def blacklist(self, ctx):
        if ctx.invoked_subcommand is None:
            with open("blacklist.json") as file:
                blacklist = json.load(file)
                entries = [
                    f"`[{no}]` | <@!{mem}> (ID: {mem})"
                    for no, mem in enumerate(blacklist['ids'], start=1)
                ]
                paginator = Paginator(source=DescriptionEmbedPaginator(
                    entries=entries,
                    title=
                    f"List of Blacklisted users of  Akito - {len(blacklist['ids'])}",
                    description="",
                    per_page=10,
                    color=0x00FFCA),
                                      ctx=ctx)
                await paginator.paginate()

    @blacklist.command(name="add")
    @commands.is_owner()
    async def blacklist_add(self, ctx: Context, member: discord.Member):
        try:
            with open('blacklist.json', 'r') as bl:
                blacklist = json.load(bl)
                if str(member.id) in blacklist["ids"]:
                    embed = discord.Embed(
                        title="Error!",
                        description=f"{member.name} is already blacklisted",
                        color=discord.Colour(0x00FFCA))
                    await ctx.reply(embed=embed, mention_author=False)
                else:
                    add_user_to_blacklist(member.id)
                    embed = discord.Embed(
                        title="Blacklisted",
                        description=f"Successfully Blacklisted {member.name}",
                        color=discord.Colour(0x00FFCA))
                    with open("blacklist.json") as file:
                        blacklist = json.load(file)
                        embed.set_footer(
                            text=
                            f"There are now {len(blacklist['ids'])} users in the blacklist"
                        )
                        await ctx.reply(embed=embed, mention_author=False)
                        webhook = discord.Webhook.from_url(url="https://discord.com/api/webhooks/1187354720956862547/fSNW", session=session)
                        embed = discord.Embed(
                            title="Blacklist Added",
                            description=f"**Action By:** {ctx.author} ({ctx.author.id})\n**User:** {user} ({user.id})\n**Time:** <t:{time}:R> (<t:{time}:D>)\n**Reason:**\n```\n{reason}```",
                            color=config.color
                        )
            await webhook.send(embed=embed)
        except Exception as e: # Better practice to catch specific exceptions rather than using a generic except
            embed = discord.Embed(
                 title="Error!",
                 description="An Error Occurred",
                color=discord.Colour(0x41eeee)
            )
            await ctx.reply(embed=embed, mention_author=False)

    @blacklist.command(name="remove")
    @commands.is_owner()
    async def blacklist_remove(self, ctx, member: discord.Member = None):
        try:
            remove_user_from_blacklist(member.id)
            embed = discord.Embed(
                title="User removed from blacklist",
                description=
                f"<a:cx_tick:1173190431295676416> | **{member.name}** has been successfully removed from the blacklist",
                color=0x00FFCA)
            with open("blacklist.json") as file:
                blacklist = json.load(file)
                embed.set_footer(
                    text=
                    f"There are now {len(blacklist['ids'])} users in the blacklist"
                )
                await ctx.reply(embed=embed, mention_author=False)
        except:
            embed = discord.Embed(
                title="Error!",
                description=f"**{member.name}** is not in the blacklist.",
                color=0x00FFCA)
            embed.set_thumbnail(url=f"{self.client.user.display_avatar.url}")
            await ctx.reply(embed=embed, mention_author=False)


    @commands.group(name="bdg", help="Allows owner to add badges for a user")
    @commands.is_owner()
    async def _badge(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @_badge.command(name="add",
                    aliases=["give"],
                    help="Add some badges to a user.")
    @commands.is_owner()
    async def badge_add(self, ctx, member: discord.Member, *, badge: str):
        ok = getbadges(member.id)
        if badge.lower() in ["own", "owner", "king"]:
            idk = "*<a:crown_1:1086509313050296393> Owner*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed2 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Added `Owner` Badge To {member}**",
                color=0x2f3136)
            await ctx.reply(embed=embed2)
        elif badge.lower() in ["staff", "support staff"]:
            idk = "*<a:staff:1077029180304273479> Staff*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed3 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Added `Staff` Badge To {member}**",
                color=0x2f3136)
            await ctx.reply(embed=embed3)
        elif badge.lower() in ["partner"]:
            idk = "*<a:partner:1077029011198328843> Partner*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed4 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Added `Partner` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed4)
        elif badge.lower() in ["sponsor"]:
            idk = "*<:astroz_spo:1086510196337152000> Sponsor*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed5 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Added `Sponsor` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed5)
        elif badge.lower() in [
                "friend", "friends", "homies", "owner's friend"
        ]:
            idk = "*<a:Friends:1086510370811822150> Owner`s Friends*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed1 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Added `Owner's Friend` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed1)
        elif badge.lower() in ["early", "supporter", "support"]:
            idk = "*<a:earlysup:1091708550469918741> Early Supporter*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed6 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Added `Early Supporter` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed6)

        elif badge.lower() in ["vip"]:
            idk = "*<a:zDV_vip:1086510832374001694> Vip*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed7 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Added `VIP` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed7)

        elif badge.lower() in ["Family", "Homies"]:
            idk = "*<:Bug_Hunter_level2:1086510981095637003> Family*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed8 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Added `Family Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed8)
        elif badge.lower() in ["all"]:
            idk = "*<a:crown_1:1086509313050296393> Owner\n<a:staff:1077029180304273479> Staff\n<a:partner:1077029011198328843> Partner\n<:astroz_spo:1086510196337152000> Sponsor\n<a:Friends:1086510370811822150> Owner`s Friends\n<a:earlysup:1091708550469918741> Early Supporter\n<a:zDV_vip:1086510832374001694> Vip\n<:Bug_Hunter_level2:1086510981095637003> Family*"
            ok.append(idk)
            makebadges(member.id, ok)
            embedall = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Added `All` Badges To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embedall)
        else:
            hacker = discord.Embed(
                                   description="**Invalid Badge**",
                                   color=0x2f3136)
            
            await ctx.reply(embed=hacker)

    @_badge.command(name="remove",
                    help="Remove badges from a user.",
                    aliases=["re"])
    @commands.is_owner()
    async def badge_remove(self, ctx, member: discord.Member, *, badge: str):
        ok = getbadges(member.id)
        if badge.lower() in ["own", "owner", "king"]:
            idk = "*<a:crown_1:1086509313050296393> Owner*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed2 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Removed `Owner` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed2)

        elif badge.lower() in ["staff", "support staff"]:
            idk = "*<a:staff:1077029180304273479> Staff*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed3 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Removed `Staff` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed3)

        elif badge.lower() in ["partner"]:
            idk = "*<a:partner:1077029011198328843> Partner*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed4 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Removed `Partner` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed4)

        elif badge.lower() in ["sponsor"]:
            idk = "*<:astroz_spo:1086510196337152000> Sponsor*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed5 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Removed `Sponsor` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed5)

        elif badge.lower() in [
                "friend", "friends", "homies", "owner's friend"
        ]:
            idk = "*<a:Friends:1086510370811822150> Owner's Friend*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed1 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Removed `Owner's Friend` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed1)

        elif badge.lower() in ["early", "supporter", "support"]:
            idk = "*<a:earlysup:1091708550469918741> Early Supporter*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed6 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Removed `Early Supporter` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed6)

        elif badge.lower() in ["vip"]:
            idk = "*<a:zDV_vip:1086510832374001694> Vip*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed7 = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Removed `VIP` Badge To {member}**",
                color=0x2f3136)
           
            await ctx.reply(embed=embed7)

        elif badge.lower() in ["bug", "hunter"]:
            idk = "*<:Bug_Hunter_level2:1086510981095637003> Bug Hunter*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed8 = discord.Embed(
                
                description=
                f"**Successfully Removed `Bug Hunter` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed8)
        elif badge.lower() in ["all"]:
            idk = "*<a:crown_1:1086509313050296393> Owner\n<a:staff:1077029180304273479> Staff\n<a:partner:1077029011198328843> Partner\n<:astroz_spo:1086510196337152000> Sponsor\n<a:Friends:1086510370811822150> Owner`s Friends\n<a:earlysup:1091708550469918741> Early Supporter\n<a:zDV_vip:1086510832374001694> Vip\n<:Bug_Hunter_level2:1086510981095637003> Bug Hunter*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embedall = discord.Embed(
                
                description=
                f"<a:cx_tick:1173190431295676416>  | **Successfully Removed `All` Badges From {member}**",
                color=0x2f3136)
            await ctx.reply(embed=embedall)
        else:
            hacker = discord.Embed(
                                   description="**Invalid Badge**",
                                   color=0x2f3136)
            await ctx.reply(embed=hacker)

    @commands.command()
    @commands.is_owner()
    async def dm(self, ctx, user: discord.User, *, message: str):
        """ DM the user of your choice """
        try:
            await user.send(message)
            await ctx.send(f"<a:cx_tick:1173190431295676416> | Successfully Sent a DM to **{user}**")
        except discord.Forbidden:
            await ctx.send("This user might be having DMs blocked or it's a bot account...")           



    @commands.group()
    @commands.is_owner()
    async def change(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))


    @change.command(name="nickname")
    @commands.is_owner()
    async def change_nickname(self, ctx, *, name: str = None):
        """ Change nickname. """
        try:
            await ctx.guild.me.edit(nick=name)
            if name:
                await ctx.send(f"<a:cx_tick:1173190431295676416> | Successfully changed nickname to **{name}**")
            else:
                await ctx.send("<a:cx_tick:1173190431295676416> | Successfully cleared nickname")
        except Exception as err:
            await ctx.send(err)



    @commands.command()
    @commands.is_owner()
    async def globalban(self, ctx, *, user: discord.User = None):
        if user is None:
            return await ctx.send(
                "You need to define the user"
            )
        for guild in self.client.guilds:
            for member in guild.members:
                if member == user:
                    await user.ban(reason="...")

@commands.command(help="Make the bot say something in a given channel.")
@commands.is_owner()
async def say(self, ctx: commands.Context, channel_id: int, *, message):
    channel = self.bot.get_channel(channel_id)
    guild = channel.guild
    target_channel = await ctx.message.author.create_dm()
    await ctx.send(f"Sending message to **{guild}** <#{channel.id}>\n> {message}")
    await target_channel.send(message)



    @commands.command(name="owners")
    @commands.is_owner()
    async def own_list(self, ctx):
        with open("info.json") as f:
            np = json.load(f)
            nplist = np["OWNER_IDS"]
            npl = ([await self.client.fetch_user(nplu) for nplu in nplist])
            npl = sorted(npl, key=lambda nop: nop.created_at)
            entries = [
                f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) (ID: {mem.id})"
                for no, mem in enumerate(npl, start=1)
            ]
            paginator = Paginator(source=DescriptionEmbedPaginator(
                entries=entries,
                title=f"Owner list of Akito - {len(nplist)}",
                description="",
                per_page=10,
                color=0x2f3136),
                                  ctx=ctx)
            await paginator.paginate()
            
  #  @commands.commond(name="leave guild")
    @commands.is_owner()

    async def leave(self, ctx, guild_id: int):

      guild_id = self.get_guild(guild_id)

      await guild_id.leave()

      await ctx.send("I Leaved the guild")