import os
os.system("pip install tasksio && pip install httpx")
os.system("pip install discord.py[speed] && pip install psutil && pip install pynacl")   
from asyncore import loop
import datetime
import random
#os.system("python3 -m pip install git+https://github.com/PranoyMajumdar/dispie")
#os.system("$ pip install discord.py dispie")
#import dispie-main
from dispie import EmbedCreator
import time
from core.Astroz import Astroz
import colorama
from colorama import Fore
import asyncio, json
import jishaku, cogs
from discord.ext import commands, tasks
from utils.config import OWNER_IDS, No_Prefix
import discord
from discord import app_commands
import aiohttp
import traceback
from discord.ext.commands import Context
import openai
from discord import Embed
from keep_alive import keep_alive
keep_alive()
from typing import Literal, Optional
#from cogs.commands.ticket import createTicket, closeTicket
#from googletrans import Translator
# Example of how to install a package from a Git repository:


os.environ["JISHAKU_NO_DM_TRACEBACK"] = "False"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

client = Astroz()
tree = client.tree
clr = 0x41eeee
TOKEN = "MTE3MzA5NzgyNTYxNDE4MDQ2Mw.GfyWUA.e6IVF59iOaVi-XjODL20N9itIZjqrooPmKQCAY"


async def Akito_stats():
  while True:
    servers = len(client.guilds)
    users = sum(g.member_count for g in client.guilds
                if g.member_count != None)
    sv_ch = client.get_channel(1220280938165043322)
    users_ch = client.get_channel(1220280943118389298)
    await asyncio.sleep(600)
    await sv_ch.edit(name="『Servers : {}』".format(servers))
    await users_ch.edit(name="『Users : {}』".format(users))


#@client.command(aliases=['tadduser', 'ticketadduser'])
#@commands.has_permissions(administrator=True)
#async def adduser(ctx, member: discord.Member, channel=None):
  #channel = channel or ctx.channel
  #guild = ctx.guild
  #overwrite = channel.overwrites_for(member)
  #overwrite.view_channel = True
 # await ctx.channel.set_permissions(member, overwrite=overwrite)
  #await ctx.reply(f"Successfully added {member.mention} to {channel}", mention_author=False)

#@adduser.error
#async def adduser_error(ctx, error):
  #if isinstance(error, commands.MissingRequiredArgument):
   # await ctx.reply(f"Wrong Usage!\n`adduser <member id/mention>`", mention_author=False)
   # if isinstance(error, commands.MissingPermissions):
     #   await ctx.reply("You are missing Administrator permission(s) to run this command.", mention_author=False)


#@client.command(aliases=['tremoveuser', 'ticketremoveuser'])
#@commands.has_permissions(administrator=True)
#async def removeuser(ctx, member: discord.Member, channel=None):
   # channel = channel or ctx.channel
   # overwrite = channel.overwrites_for(member)
   # overwrite.view_channel = False
   # await channel.set_permissions(member, overwrite=overwrite)
   # await ctx.reply(f"Successfully removed {member.mention}'s access from {channel}.", mention_author=False)

#@removeuser.error
#async def removeuser_error(ctx, error):
   # if isinstance(error, commands.MissingRequiredArgument):
       # await ctx.reply(f"Wrong Usage!\n`removeuser <member id/mention>`", mention_author=False)
  #  if isinstance(error, commands.MissingPermissions):
       # await ctx.reply("You are missing Administrator permission(s) to run this command.", mention_author=False)

#@client.command(aliases=['closeticket', 'tclose'])
#@commands.has_permissions(administrator=True)
#async def close_ticket(ctx):
   # if isinstance(ctx.channel, discord.TextChannel) and ctx.channel.name.startswith('ticket-'):
       # await ctx.send("Closing this ticket in 5 seconds.")
        #await asyncio.sleep(5)
       # await ctx.channel.delete()
   # else:
       # await ctx.send("This command can only be used in a ticket channel.")

#@client.command(aliases=['rename', 'rn', 'trename'])
#@commands.has_permissions(administrator=True)
#async def rename_ticket(ctx, new_name):
    #  await ctx.channel.edit(name=new_name)
     # await ctx.send(f"Channel name changed to '{new_name}'")

#@rename_ticket.error
#async def rename_ticket_error(ctx, error):
   # if isinstance(error, commands.MissingRequiredArgument):
      #  await ctx.reply(f"Wrong Usage!\n`Rename <new_name>`", mention_author=False)
  #  if isinstance(error, commands.MissingPermissions):
      #  await ctx.reply("You are missing Administrator permission(s) to run this command.", mention_author=False)

class Hacker(discord.ui.Modal, title='Embed Configuration'):
  tit = discord.ui.TextInput(
    label='Embed Title',
    placeholder='Embed title here',
  )

  description = discord.ui.TextInput(
    label='Embed Description',
    style=discord.TextStyle.long,
    placeholder='Embed description optional',
    required=False,
    max_length=4000,
  )

  thumbnail = discord.ui.TextInput(
    label='Embed Thumbnail',
    placeholder='Embed thumbnail here optional',
    required=False,
  )

  img = discord.ui.TextInput(
    label='Embed Image',
    placeholder='Embed image here optional',
    required=False,
  )

  footer = discord.ui.TextInput(
    label='Embed footer',
    placeholder='Embed footer here optional',
    required=False,
  )

  async def on_submit(self, interaction: discord.Interaction):
    embed = discord.Embed(title=self.tit.value,
                          description=self.description.value,
                          color=0x00FFED)
    if not self.thumbnail.value is None:
      embed.set_thumbnail(url=self.thumbnail.value)
    if not self.img.value is None:
      embed.set_image(url=self.img.value)
    if not self.footer.value is None:
      embed.set_footer(text=self.footer.value)
    await interaction.response.send_message(embed=embed)

  async def on_error(self, interaction: discord.Interaction,
                     error: Exception) -> None:
    await interaction.response.send_message('Oops! Something went wrong.',
                                            ephemeral=True)

    traceback.print_tb(error.__traceback__)


@tree.command(name="embed", description="Create A Embed Using Akito")
async def _embed(interaction: discord.Interaction) -> None:
  await interaction.response.send_modal(Hacker())
        
#####################################


@client.listen("on_guild_join")
async def dexterbalak(guild):
  with open('roles.json', 'r') as f:
    pp = json.load(f)
  if guild:
    if not str(guild.id) in pp:
      pp[str(guild.id)] = {"humanautoroles": [], "botautoroles": []}
      with open('role.json', 'w') as f:
        json.dump(pp, f, indent=4)


@client.listen("on_member_join")
async def autorolessacks(member):
  if member.id == client.user.id:
    return
  else:
    gd = member.guild
    with open('roles.json') as f:
      idk = json.load(f)
    g_ = idk.get(str(member.guild.id))
    human_autoroles = g_['humanautoroles']
    bot_autoroles = g_['botautoroles']
    if human_autoroles == []:
      pass
    else:
      for role in human_autoroles:
        rl = gd.get_role(int(role))
        if not member.bot:
          await member.add_roles(rl, reason="Akito Autoroles")
    if bot_autoroles == []:
      pass
    else:
      for rol in bot_autoroles:
        rml = gd.get_role(int(rol))
        if member.bot:
          await member.add_roles(rml, reason="Akito Autoroles")

#create_ticket_view = createTicket()
#close_ticket_view = closeTicket()


#@client.command()
async def sync(ctx):
    num = await bot.tree.sync()
    await ctx.send(f'{len(num)} command synced')

#@client.command()
async def sync(ctx):
    await ctx.send('Synchronizing commands...')
    await hybrid_commands.sync_commands()
    await ctx.send('Commands synchronized successfully!')
    
#@client.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

@client.event
async def on_ready():
    print(Fore.RED + "MADE FOR All 💖")
    print(Fore.RED + "Loaded & Online!")
    print(Fore.BLUE + f"Logged in as: {client.user}")
    print(Fore.MAGENTA + f"Connected to: {len(client.guilds)} guilds")
    print(Fore.YELLOW + f"Connected to: {len(client.users)} users")
    await client.loop.create_task(Akito_stats())
   # try:
        #synced = await client.tree.sync()
        #inchannel = client.get_channel(1170018557111828704)
        #await inchannel.send(f"Loaded & Online! \nLogged is as: {client.user} \nConnected to: {len(client.guilds)} guilds \nConnected to: {len(client.users)} users \nSynced {len(synced)} commands")
    #except Exception as e:
        #print(e)


@client.event
async def on_command_completion(context: Context) -> None:
  full_command_name = context.command.qualified_name
  split = full_command_name.split("\n")
  executed_command = str(split[0])
  akito = client.get_channel(1196117705997164614)
  if context.guild is not None:
    try:
      embed = discord.Embed(color=0x2f3136)
      embed.set_author(
        name=f"Executed {executed_command} Command By : {context.author}",
        icon_url=f"{context.author.avatar}")
      embed.set_thumbnail(url=f"{context.author.avatar}")
      embed.add_field(name="<a:im_arrowr:1173268300789194803> Command Name :",
                      value=f"{executed_command}",
                      inline=False)
      embed.add_field(
        name="<a:im_arrowr:1173268300789194803> Command Executed By :",
        value=
        f"{context.author} | ID: [{context.author.id}](https://discord.com/users/{context.author.id})",
        inline=False)
      embed.add_field(
        name="<a:im_arrowr:1173268300789194803> Command Executed In :",
        value=
        f"{context.guild.name}  | ID: [{context.guild.id}](https://discord.com/users/{context.author.id})",
        inline=False)
      embed.add_field(
        name="<a:im_arrowr:1173268300789194803> Command Executed In Channel :",
        value=
        f"{context.channel.name}  | ID: [{context.channel.id}](https://discord.com/channel/{context.author.id}/{context.channel.id})",
        inline=False)
      embed.set_footer(text="Akito is BEST",
                       icon_url=client.user.display_avatar.url)
      await hacker.send(embed=embed)
    except:
      print('command failed')
  else:
    try:

      embed1 = discord.Embed(color=0x2f3136)
      embed1.set_author(
        name=f"Executed {executed_command} Command By : {context.author}",
        icon_url=f"{context.author.avatar}")
      embed1.set_thumbnail(url=f"{context.author.avatar}")
      embed1.add_field(name="<a:im_arrowr:1173268300789194803> Command Name :",
                       value=f"{executed_command}",
                       inline=False)
      embed1.add_field(
        name="<a:im_arrowr:1173268300789194803> Command Executed By :",
        value=
        f"{context.author} | ID: [{context.author.id}](https://discord.com/users/{context.author.id})",
        inline=False)
      embed1.set_footer(text="Powered By Akito", 
                        icon_url=client.user.display_avatar.url)
      await hacker.send(embed=embed1)
    except:
      print("command failed")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Missing Permissions",
            description=f"{ctx.author.mention} You do not have enough permissions to use the {ctx.command} command.",
            color=0xff0000
        )
        embed.add_field(name="Permission Required", value=error.missing_perms)
        await ctx.send(embed=embed)

        if ctx.guild and ctx.guild.owner:
            owner = ctx.guild.owner
            embed_owner = discord.Embed(
                title="Permission Issue",
                description=f"Hi {owner.mention}, It looks like there was a missing permission issue in your server. Please consider fixing it for a better experience!",
                color=0xff0000
            )
            await owner.send(embed=embed_owner)

    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        hacker = discord.SyncWebhook.from_url("https://discord.com/api/webhooks/1233435542960472157/kHmhxfDDmz-PBGFl_3HKO2hB5llbUWm33b9dBOGNB7EsANwh0cfCHfn_TXHP_Alhg7ok")
        embed = discord.Embed(
            title="Command Error",
            description=f"An error occurred while executing command: {str(error)} in {ctx.guild.name} server.",
            color=0xff0000
        )
        embed.add_field(name="Requester", value=f"{ctx.author.name} - ID: {ctx.author.id}")
        embed.add_field(name="Command", value=f"{ctx.command}")
        embed.add_field(name="How to Fix", value="Please fix the command to prevent this error in the future.")
        await hacker.send(embed=embed)
        



  
@client.command(aliases=['wh'])
@commands.is_owner()
@commands.has_permissions(administrator=True)
async def create_hook(ctx, name=None):
  if not name:
    await ctx.send("Please specify a name for the webhook.")
    return
  webhook = await ctx.channel.create_webhook(name=name)
  embed = discord.Embed(
    title=
    f"**<a:cx_tick:1173190431295676416> | Webhook __{webhook.name}__ created successfully **",
    color=discord.Color.blue())
  try:
    await ctx.author.send(f"||{webhook.url}||")
    await ctx.author.send(embed=embed)
    await ctx.send(
      f"**<a:cx_tick:1173190431295676416>| Webhook :- __{webhook.name}__ created successfully.**\n** Check your DMs for the URL.\n {ctx.author.mention} **"
    )
  except discord.Forbidden:
    await ctx.send(
      f"**<a:cx_tick:1173190431295676416>|Webhook:- __{webhook.name}__ ||{webhook.url}|| (Unable to DM user) ** \n {ctx.author.mention}"
    )


@client.command()
@commands.is_owner()
@commands.has_permissions(administrator=True)
async def delete_hook(ctx, webhook_id):
  try:
    webhook = await discord.Webhook.from_url(
      webhook_id, adapter=discord.RequestsWebhookAdapter())
    await webhook.delete()
    await ctx.send("Webhook deleted successfully.")
  except discord.NotFound:
    await ctx.send("Webhook not found.")


@client.command(aliases=['all_hooks'])
@commands.is_owner()
async def list_hooks(ctx):
  webhooks = await ctx.channel.webhooks()
  if not webhooks:
    await ctx.send("No webhooks found in this channel.")
    return
  embed = discord.Embed(title="List of Webhooks", color=discord.Color.blue())
  for webhook in webhooks:
    embed.add_field(
      name="__Name__",
      value=f"**<a:cx_tick:1173190431295676416> | {webhook.name} **")
    embed.add_field(name="__ID__", value=webhook.id)
    embed.add_field(name="\u200b", value="\u200b")
  await ctx.send(
    f"{ctx.author.mention}, Here are the webhooks in this channel",
    embed=embed)


@client.command()
async def spotify(ctx, user: discord.Member = None):
  if user == None:
    user = ctx.author
    pass
  if user.activities:
    for activity in user.activities:
      if isinstance(activity, Spotify):
        nemo = discord.Embed(title=f"{user.name}'s Spotify",
                             description="Listening to {}".format(
                               activity.title),
                             color=0x11100d)
        nemo.set_thumbnail(url=activity.album_cover_url)
        nemo.add_field(name="Artist", value=activity.artist)
        nemo.add_field(name="Album", value=activity.album)
        nemo.set_footer(text="Song started at {}".format(
          activity.created_at.strftime("%H:%M")))
        await ctx.send(embed=nemo)
          

#@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def gpt(ctx: commands.Context, *, prompt: str):
    async with aiohttp.ClientSession() as session:
        payload = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 500,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "best_of": 1
        }
        headers = {
            "Authorization": "Bearer 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"  # Replace YOUR_API_KEY with your actual API key
        }
        async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
            response = await resp.json()
            try:
                respo = response["choices"][0]["text"]
                hacker5 = discord.Embed(description=f"```py\n{respo}\n```", color=0x2f3136)
                hacker5.set_author(name="ChatGPT", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
                hacker5.timestamp = discord.utils.utcnow()
                hacker5.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
                await ctx.reply(embed=hacker5)
            except KeyError as e:
                print(f"Error: {e}. Unable to retrieve response from the API")

bot = client
@bot.command()
async def say(ctx, *, message=None):
    if message is None:
        await ctx.send("**Please provide a message to say.**")
        return
    await ctx.message.delete()
    await ctx.send(message)



#@client.command()
@commands.has_permissions(administrator=True)
async def embed(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send('Waiting for a title')
    title = await client.wait_for('message', check=check)

    await ctx.send('Waiting for a description')
    desc = await client.wait_for('message', check=check)

    embed = discord.Embed(title=title.content,
                          description=desc.content,
                          color=0x2f3136)
    await ctx.send(embed=embed)


#@client.command()
async def math(ctx, *, expression: str):
    calculation = eval(expression)
    await ctx.send('Expression: {}\nAnswer: {}'.format(expression,
                                                       calculation))
  
#@client.command()
#async def timer(ctx, seconds: int):
    #await ctx.send(f'Timer started for {seconds} seconds.')
    #await asyncio.sleep(seconds)
   # await ctx.send(f'Timer ended after {seconds} seconds.')

truth_msg = [
  "How would you rate your looks on a scale from 1-10?",
  "What is one thing that brings a smile to your face, no matter the time of day?",
  "What’s is one thing that you’re proud of?",
  "Have you ever broken anything of someone else's and not told the person?",
  "Who is your boyfriend/girlfriend/partner?",
  "When was the last time you lied?", "When was the last time you cried?",
  "What's your biggest fear?", "What's your biggest fantasy?",
  "Do you have any fetishes?",
  "What's something you're glad your mum doesn't know about you?",
  "Have you ever cheated on someone?",
  "What was the most embarrassing thing you’ve ever done on a date?",
  "Have you ever accidentally hit something (or someone!) with your car?",
  "Name someone you’ve pretended to like but actually couldn’t stand.",
  "What’s your most bizarre nickname?",
  "What’s been your most physically painful experience?",
  "What bridges are you glad that you burned?",
  "What’s the craziest thing you’ve done on public transportation?",
  "If you met a genie, what would your three wishes be?",
  "If you could write anyone on Earth in for President of the United States, who would it be and why?",
  "What’s the meanest thing you’ve ever said to someone else?",
  "Who was your worst kiss ever?",
  "What’s one thing you’d do if you knew there no consequences?",
  "What’s the craziest thing you’ve done in front of a mirror?",
  "What’s the meanest thing you’ve ever said about someone else?",
  "What’s something you love to do with your friends that you’d never do in front of your partner?",
  "Who are you most jealous of?", "What do your favorite pajamas look like?",
  "Have you ever faked sick to get out of a party?",
  "Who’s the oldest person you’ve dated?",
  "How many selfies do you take a day?",
  "How many times a week do you wear the same pants?",
  "Would you date your high school crush today?", "Where are you ticklish?",
  "Do you believe in any superstitions? If so, which ones?",
  "What’s one movie you’re embarrassed to admit you enjoy?",
  "What’s your most embarrassing grooming habit?",
  "When’s the last time you apologized? What for?",
  "How do you really feel about the Twilight saga?",
  "Where do most of your embarrassing odors come from?",
  "Have you ever considered cheating on a partner?", "Boxers or briefs?",
  "Have you ever peed in a pool?",
  "What’s the weirdest place you’ve ever grown hair?",
  "If you were guaranteed to never get caught, who on Earth would you murder?",
  "What’s the cheapest gift you’ve ever gotten for someone else?",
  "What app do you waste the most time on?",
  "What’s the weirdest thing you’ve done on a plane?",
  "Have you ever been nude in public?",
  "How many gossip blogs do you read a day?",
  "What is the youngest age partner you’d date?",
  "Have you ever lied about your age?", "Have you ever used a fake ID?",
  "Who’s your hall pass?", "What is your greatest fear in a relationship?",
  "Have you ever lied to your boss?", "Who would you hate to see naked?",
  "Have you ever regifted a present?",
  "Have you ever had a crush on a coworker?",
  "Have you ever ghosted a friend?", "Have you ever ghosted a partner?",
  "What’s the most scandalous photo in your cloud?",
  "When’s the last time you dumped someone?",
  "What’s one useless skill you’d love to learn anyway?",
  "If I went through your cabinets, what’s the weirdest thing I’d find?",
  "Have you ever farted and blamed it on someone else?","Are you a hard-working student?",
"Are you into any sports?",
"Are you scared of any animals?",
"Are you scared of dying? Why?",
"Are you scared of ghosts?",
"Are you still a virgin?",
"Can you lick your elbow?",
"Can you see yourself being married to the creepiest kid a your school someday?",
"Can you speak a different language?",
"Can you touch your tongue to your nose?",
"Can you use a pogo stick?",
"Could you go a week without junk food?",
"Could you go two months without talking to your friends?",
"Describe the weirdest dream you've ever had?",
"Describe the weirdest dream you’ve ever had?",
"Describe your most recent dream that you recall.",
"Describe your most recent romantic encounter.",
"Describe your worst kiss ever.",
"Do you believe in love at all?",
"Do you believe in love at first sight?",
"Do you ever talk to yourself in the mirror?",
"Do you have a hidden talent? What is it?",
"Do you have a job? If so, what is your favourite thing about it?",
"Do you have an imaginary friend?",
"Do you have any phobias?",
"Do you have any unusual talents?",
"Do you know how to cook?",
"Do you know how to dance?",
"Do you like doing chores?",
"Do you like to exercise?",
"Do you message people during your classes?",
"Do you prefer apple or android?",
"Do you sing in the shower? What song did you sing the last time?",
"Do you think you will marry your bf/gf? If not, why not?",
"Explain to the person you like least in this group why you like them the least.",
"Have you been in any fights while in school?",
"Have you ever been kissed yet? If so, who was your best kiss?",
"Have you ever bitten a toenail?",
"Have you ever blamed a fart on an animal?",
"Have you ever blamed something that you have done on one of your siblings?",
"Have you ever cheated on a test?",
"Have you ever cheated or been cheated on?",
"Have you ever climbed a tree?",
"Have you ever crapped your pants since you were a child?",
"Have you ever eaten food that you've dropped on the ground? If so, how long was it on the ground?",
"Have you ever fallen asleep during a class?",
"Have you ever had a crush on a teacher?",
"Have you ever had a crush on someone that your best friend has dated?",
"Have you ever had someone write an assignment or a work for you?",
"Have you ever kissed an animal?",
"Have you ever let someone take the blame for something you did?",
"Have you ever lied to your best friend?",
"Have you ever lied to your parents about if you were in classes or not?",
"Have you ever lied to your parents about what you were doing after school?",
"Have you ever peed in a pool?",
"Have you ever picked your nose in public?",
"Have you ever posted something on the internet/social media that you regret?",
"Have you ever pulled a prank on one of your teachers?",
"Have you ever received a love letter?",
"Have you ever ridden the bus without paying the fare?",
"Have you ever stolen something of value worth more than $10?",
"Have you ever stolen something?",
"Have you ever taken money from your roommate?",
"Have you ever taken money that didn't belong to you?",
"Have you ever thrown a party at your house?",
"Have you ever told a lie during a game of Truth or Dare? What was it and why?",
"Have you ever told one of your best friend's secrets, even if you said you wouldn't?",
"Have you ever used someone else's password?",
"Have you ever watched an adult film without your parents knowing?",
"Have you ever worn the same clothes for more than three days?",
"How do you feel about end pieces of a loaf of bread?",
"How do you feel about social media?",
"How far would you go to land the guy or girl of your dreams?",
"How many boyfriends (or girlfriends) have you had?",
"How many days could you go without your partner?",
"How many kids would you like to have?",
"How many siblings do you have?",
"How many times have you skipped class for no reason?",
"How old were you when your parents sat you down for 'the talk' and what did they say (or not say) about 'the birds and the bees'?",
"How soon did you realize that you were in love with your partner?",
"How soon did/do you want start a family?",
"How was your first kiss?",
"If there was no such thing as money, what would you do with your life?",
"If you could be a superhero; what would your power be?",
"If you could be any animal, which one would you be?",
"If you could be any dinosaur; which would it be?",
"If you could be any super villain; who would you be?",
"If you could change one thing on your body, what would it be?",
"If you could dye your hair any colour, what colour would you pick?",
"If you could erase one past experience, what would it be?",
"If you could go anywhere in the world, where would you go?",
"If you could make one wish right this second, what would it be?",
"If you could only hear one song for the rest of your life, what would it be?",
"If you could own your own business one day, what would it be?",
"If you could own your own business one day; what would it be?",
"If you could switch lives with any celebrity for a day, who would it be?",
"If you could take away one bad thing in the world, what would it be?",
"If you could, what would you change about your life?",
"If you had never met your partner, where do you think you would be?",
"If you had the choice to live on your own right now, would you do it?",
"If you have ever cheated, why did you do it?",
"If you suddenly had a million dollars; what would you do with all of your money?",
"If you were a billionaire, what would you spend your time doing?",
"If you were rescuing everyone here from a burning building, but you had to leave one behind, who would it be?",
"If you were to be stuck on a deserted island, which friend would you want with you?",
"If you were to be trapped on an island for 3 days, what would you take with you?"
]


@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def truth(ctx):
  embed = Embed(
    title=f"{ctx.author.name}'s Truth",
    description=f"{random.choice(truth_msg)}",
    color=0x2f3136
  )
  await ctx.send(embed=embed)


dare_msg = [
  "Let the person on your right take an ugly picture of you and your double chin and post it on IG with the caption", "I don’t leave the house without my double chin",
  " Eat a raw potato",
  "Order a pizza and pay the delivery guy in all small coins",
  "Open the window and scream to the top of our lungs how much you love your mother",
  "Kiss the person who is sitting beside you",
  "Beg for a cent on the streets",
  "Go into the other room, take your clothes off and put them on backward",
  "Show everyone your search history for the past week",
  "Set your crush’s picture as your FB profile picture",
  "Take a walk down the street alone and talk to yourself",
  "Do whatever someone wants for the rest of the day",
  " Continuously talk for 3 minutes without stopping",
  " Draw something on the face with a permanent marker",
  " Peel a banana with your feet",
  " Lay on the floor for the rest of the game",
  " Drink 3 big cups of water without stopping",
  "Go back and forth under the table until it’s your turn again",
  " Close your mouth and your nose: try to pronounce the letter ‘“A” for 10 seconds",
  "Ask someone random for a hug",
  "Call one of your parents and then tell them they are grounded for a week",
  "Have everyone here list something they like about you",
  "Wear a clothing item often associated with a different gender tomorrow",
  "Prank call your crush",
  "Tweet 'insert popular band name here fans are the worst' and don't reply to any of the angry comments.",
  "List everyone as the kind on animal you see them as.",
  "Talk in an accent for the next 3 rounds",
  "Let someone here do your makeup.", "Spin around for 30 seconds",
  "Share your phone's wallpaper",
  "Ask the first person in your DMs to marry you.",
  "Show the last DM you sent without context",
  "Show everyone here your screen time.", "Try to lick your elbow",
  "Tie your shoe strings together and try to walk to the door and back",
  "Everything you say for the next 5 rounds has to rhyme.",
  "Text your crush about how much you like them, but don't reply to them after that.",
  "Ask a friend for their mom's phone number",
  "Tell the last person you texted that you're pregnant/got someone pregnant.",
  "Do an impression of your favorite celebrity",
  "Show everyone the last YouTube video you watched.",
  "Ask someone in this server out on a date.",
  "Kiss the player you think looks the cutest.","Act like a monkey and record a video of it.",
"Act like you do not understand human language until your next turn (come up with your own language).",
"Act like your favourite Disney character for the rest of the game.",
"Close your eyes and send a blind text to a random person.",
"Compose a poem on the spot based on something the group comes up with.",
"Everything you say for the next 5 minutes has to rhyme.",
"Everything you say for the next 5 minutes must not contain the words: 'but', 'a', 'the', 'or'",
"Make a freestyle rap song about each person in the group",
"Make a poem using the words 'orange' and 'moose'.",
"Make a poem using the words 'pineapple' and 'apple'.",
"Make a poem using the words 'goose' and 'peanuts'.",
"Make up a poem about the colour blue.",
"Make up a story about a random person in the group.",
"Post 'I love English!' on a social media.",
"Record a video of you dancing, but without music.",
"Record a video of you playing the air drums to a song of your choice.",
"Record a video of you playing the air guitar to a song of your choice.",
"Record an impression of your favourite celebrity.",
"Record an impression of your favourite animal.",
"Record your best evil laugh; as loud as you can.",
"Record your best president impression.",
"Record yourself saying the alphabet backwards.",
"Record yourself singing 'Twinkle Twinkle, Little Star' while beat boxing.",
"Record yourself singing the alphabet without moving your mouth.",
"Record yourself talking about your favourite food in a russian accent.",
"Say 'ya heard meh' after everything you say for the next 5 minutes.",
"Say 'you know what am sayin' after everything you say for the next 5 minutes.",
"Text someone asking them if they believe in aliens, send a screenshot of the conversation.",
"Send an email to one of your teachers, telling them about how your day is going and take a screenshot.",
"Send an unsolicited text message to one of your friends, telling them about how your day is going and take a screenshot.",
"Send the last photo you took with your phone camera.",
"Send the last screenshot you took on your phone.",
"Send the most embarrassing photo on your phone.",
"Send the oldest selfie on your phone.",
"Send a screenshot of your most recent google search history.",
"Send a selfie of you making a funny face.",
"Set your phone language to Chinese for the next 10 minutes.",
"Show the last three people you texted and what the messages said.",
"Text your crush and tell them how much you like them.",
"Use the letters of the name of another player to describe them (ex. SAM : S = Silly ; A = Attractive ; M = Merry)",
"Yell out the first word that comes to your mind, and record it."
]


@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def dare(ctx):
  embed = Embed(
    title=f"{ctx.author.name}'s Dare",
    description=f"{random.choice(dare_msg)}",
    color=0x2f3136
  )
  await ctx.send(embed=embed)


@client.command()
async def coinflip(ctx):
  embed = Embed(
    title="Coin Flip",
    description=f"{random.choice(['Heads', 'Tails'])}",
    color=0x2f3136
  )
  await ctx.send(embed=embed)

@client.command()
async def translate(ctx, lang, *, text):
    translator = Translator()
    translated_text = translator.translate(text, dest=lang)
    embed = Embed(
        title="Translating",
        description=f"{translated_text.text}",
        color=0x2f3136
    )
    await ctx.send(embed=embed)

#@translate.error
async def translate_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f"Wrong usage\n`translate [language] [text]`\n\nlanguage = `Hindi` , `English` , `Urdu` , `Arabic` , `Afrikaans` , `Albanian` , `etc`", mention_author=False)

@client.command(name='invites', help='Displays the number of invites a member has.')
async def invites(self, ctx, member: commands.MemberConverter=None):
    member = member or ctx.author  # if no member is provided, use the one who typed the command
    total_invites = 0
    for i in await ctx.guild.invites():
        if i.inviter == member:
            total_invites += i.uses
    await ctx.send(f'{member.mention} has invited {total_invites} member(s)!')

@client.command()
async def embedcreate(interaction: discord.Interaction):
  view = EmbedCreator()
  await interaction.response.send_message(embed=view.get_defualt_embed, view=view)
    

@client.command(name="leaveguild", help="Make the bot leave a guild by ID")

@commands.is_owner()
async def leave_guild(ctx, guild_id: int):

    guild = client.get_guild(guild_id)

    if guild:

        await guild.leave()

        await ctx.send(f"Successfully left the guild with ID: {guild_id}")

    else:

        await ctx.send("Unable to find a guild with that ID")
 

@client.command()
@commands.is_owner()
async def create_invite(ctx, guild_id: int):

    guild = client.get_guild(guild_id)

    if guild is not None:

        invite = await guild.text_channels[0].create_invite(max_uses=1)

        await ctx.send(f"Here's the invite link for the server: {invite}")

    else:

        await ctx.send("The specified server does not exist.")
        





   
 
  
async def main():
  async with client:
    os.system("clear")
    await client.load_extension("cogs")
    await client.load_extension("jishaku")
    await client.start(TOKEN)


if __name__ == "__main__":
  asyncio.run(main())
