import discord, wavelink, asyncio
from discord.ext import commands, tasks
from discord.ui import Button, View,button
#from core import Assault, Cog
import random
import os
import datetime
import datetime as dt
from wavelink.ext import spotify
#import azapi

OPTIONS = {
  
    "1️⃣": 1,
    "2️⃣": 2,
    "3️⃣": 3,
    "4️⃣": 4,
    "5️⃣": 5,
}

autoplay = False

class MusicView(discord.ui.View):
  def __init__(self, player, ctx, length,lasts,now):
    self.length = length
    self.player = player
    self.ctx = ctx
    self.last_song = lasts
    self.now = None
    self.vc = self.ctx.voice_client.channel
    self.paused = False
    super().__init__(timeout=int(length))

  async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id not in [i.id for i in self.vc.members]:
            await interaction.response.send_message(
                "You and me must be in same voice channel to this controller.",
                ephemeral=True,
            )
            return False
        return True

  @button(custom_id="PAUSE_RESUME", emoji="⏯️", row=1)
  async def _idklol(self, interaction, button):
    vc = self.ctx.voice_client
    if not self.paused:
      await vc.pause()
      self.paused = True
      x = "paused"
    else:
      await vc.resume()
      self.paused = False
      x = "resumed"
    await interaction.response.send_message(x, ephemeral=True)
            
  @button(custom_id="SKIP_MUSIC", emoji="⏭️",row=1)
  async def _skip(self, interaction, button):
    global autoplay
    if autoplay:
      vc = self.ctx.voice_client
      await vc.stop()
      return await interaction.response.send_message("<a:cx_tick:1173190431295676416> | Song skipped.", ephemeral=True)
    vc = self.ctx.voice_client
    try:
      song = vc.queue.get()
      if song == None:
        await vc.stop()
    except:
      await vc.stop()
      return await interaction.response.send_message("<a:cx_tick:1173190431295676416> | Song skipped.", ephemeral=True)
    else:
      ctx = vc.ctx
      await vc.play(song_dki)
      await ctx.send(embed=discord.Embed(description="<a:cx_tick:1173190431295676416> | Skiped the track.", color=0x2f3136))
      embed=discord.Embed(title="Now Playing", description=f"{song_dki.title}", color=0x2f3136)
      embed.add_field(name="<a:a_dj:1195717009179152455> Song By",

                               value=f"`{song_dki.author}`")

      embed.add_field(name="<a:hx_time:1173459120850997368> Duration",

                               value=f"`❯ { round(song_dki.duration / 60, 2)}`")

      embed.set_author(name="NOW PLAYING",

                                icon_url=f"{ctx.author.avatar}")

      embed.set_footer(text=f"Requested By {ctx.author}",

                                icon_url=f"{ctx.author.avatar}")

      embed.timestamp = discord.utils.utcnow()
      view = MusicView(vc,ctx,song_dki.length,self.last_song,song_dki)

      view.add_item(Dropdown())
    await ctx.send(embed=embed, view=view)
    await interaction.response.send_message("<a:cx_tick:1173190431295676416>| Song skipped.", ephemeral=True)

  @button(custom_id="STOP_SONG", emoji="<:musicstop_icons:1115019940387360858>",style=discord.ButtonStyle.danger,row=1)
  async def _STOPsong(self, interaction, button):
    vc = self.ctx.voice_client
    if not vc.is_playing():
      return
    if not vc:
      return
    await vc.stop()
    await interaction.response.send_message("Stopped Music",ephemeral=True)

  @button(custom_id="LOOP_SONG", emoji="🔁",row=1)
  async def _loop_song(self, interaction, button):
    vc = self.ctx.voice_client
    try:
      loop = getattr(vc, "loop")
    except:
      loop = False
    if not vc.is_playing():
      return
    if not vc:
      return
    if loop:
      setattr(vc, "loop", False)
      await interaction.response.send_message("Looping is disabled.", ephemeral=True)
    vc = self.ctx.voice_client
    if not vc.is_playing():
      return
    if not vc:
      return
    setattr(vc, "loop", True)
    await interaction.response.send_message("Loop is now set to current song.", ephemeral=True)

  @button(custom_id="SHUFFLE_SONG", emoji="🔀",row=1)
  async def _shuffle_song(self, interaction, button):
    if self.player.queue.is_empty:
      return await interaction.response.send_message("Add more songs to the queue before shuffling.", ephemeral=True)
    vc = self.ctx.voice_client
    queue = vc.queue
    xr=random.shuffle(queue)
    vc.queue = xr
    await interaction.response.send_message("Shuffled the queue", ephemeral=True)

  @button(custom_id="down_vol_SONG", emoji="🔉",row=2)
  async def hmmm(self, interaction, button):
    vc = self.ctx.voice_client
    if not vc or not vc.is_playing():
      return
    vc.volume
    idk = int(vc.volume)-10
    if idk > 500 or idk < 1:
      return await interaction.response.send_message("Volume must be between 500% - 1%", ephemeral=True)
    await vc.set_volume(idk)
    return await interaction.response.send_message(f"volume set  {idk}%",ephemeral=True)

  @button(custom_id="condomlxd", emoji="📜",row=2)
  async def _shuffle_song_____(self, interaction, button):
    if self.now:
      title = self.now.title
      ap = azapi.AZlyrics("google",accuracy=0.5)
      ap.title = title
      lyrics = ap.getLyrics()
      embed = discord.Embed(title="Lyrics", description=lyrics)
      await interaction.response.send_message(embed=embed,ephmeral=True)
    else:
      print("yo")

  @button(custom_id="condom", emoji="🤍",row=2)
  async def _shuffle_song___(self, interaction, button):
    await interaction.response.send_message("You found a premium feature.", ephmeral=True)

  @button(custom_id="🗑️", emoji="🗑️",row=2)
  async def _shuffle_song____(self, interaction, button):
    vc = self.ctx.voice_client
    if not vc or not vc.is_playing():
      return
    que = vc.queue.clear()
    await interaction.response.send_message("You found a premium feature.",ephemeral=True)

  @button(custom_id="VOLUME_UP", emoji="🔊",row=2)
  async def hmmmm(self, interaction, button):
    vc = self.ctx.voice_client
    if not vc or not vc.is_playing():
      return
    vc.volume
    idk = int(vc.volume)+10
    if idk > 500 or idk < 1:
      return await interaction.response.send_message("Volume must be between 500% - 1%", ephemeral=True)
    await vc.set_volume(idk)
    return await interaction.response.send_message(f"volume set {idk}%",ephemeral=True)

  def disable_all(self) -> None:
        for buttonn in self.children:
            if isinstance(buttonn, discord.ui.button):
                button.disabled = True

  async def on_timeout(self) -> None:
        self.disable_all()
        if hasattr(self, "message"):
            await self.message.edit(view=self)
            
class Dropdown(discord.ui.Select):

  def __init__(self):
    options =[
      discord.SelectOption(label="Reset",
                           description="Clears all Filter",
                           emoji="<a:red_diamond:1194836383110545408>"),
      discord.SelectOption(label="Slowed",
                           description="Enables Slowed Filter",
                           emoji="<a:diamond:1106118913894387712>"),
      discord.SelectOption(label="Chipmunk",
                           description="Enables Chipmunk Filter",
                           emoji="<a:diamond:1106118913894387712>"),
      discord.SelectOption(label="Nightcore",
                           description="Enables Nightcore Filter",
                           emoji="<a:diamond:1106118913894387712>"),
      discord.SelectOption(label="Lofi",
                           description="Enables Lofi Filter",
                           emoji="<a:diamond:1106118913894387712>"),
      discord.SelectOption(label="8D",
                           description="Enables 8D Filter",
                           emoji="<a:diamond:1106118913894387712>"),
      discord.SelectOption(label="Karaoke",
                           description="Enables Karaoke Filter",
                           emoji="<a:diamond:1106118913894387712>"),
      discord.SelectOption(label="DeepBass",
                           description="Enables Deep Bass Filter",
                           emoji="<a:diamond:1106118913894387712>")
    ]
    super().__init__(placeholder="Select Filter",
                     options=options,
                     min_values=1,
                     max_values=1)

  async def callback(self, interaction: discord.Interaction):
    selected_filter = self.values[0]
    if selected_filter == "Reset":
      vc = interaction.guild.voice_client
      await vc.set_filter(wavelink.Filter(equalizer=wavelink.Equalizer.flat()),
                          seek=False)
                          
    elif selected_filter == "Slowed":
      vc = interaction.guild.voice_client
      await vc.set_filter(
        wavelink.Filter(timescale=wavelink.Timescale(rate=0.9)), seek=False)

    elif selected_filter == "Chipmunk":
      vc = interaction.guild.voice_client
      await vc.set_filter(
        wavelink.Filter(timescale=wavelink.Timescale(rate=1.3)), seek=False)

    elif selected_filter == "Nightcore":
      vc = interaction.guild.voice_client
      await vc.set_filter(
        wavelink.Filter(timescale=wavelink.Timescale(speed=1.25, pitch=1.3)),
        seek=False)

    elif selected_filter == "Lofi":
      vc = interaction.guild.voice_client
      await vc.set_filter(
        wavelink.Filter(timescale=wavelink.Timescale(rate=0.8)), seek=False)

    elif selected_filter == "8D":
      vc = interaction.guild.voice_client
      await vc.set_filter(
        wavelink.Filter(rotation=wavelink.Rotation(speed=0.15)), seek=False)

    elif selected_filter == "Karaoke":
      vc = interaction.guild.voice_client
      await vc.set_filter(wavelink.Filter(karaoke=wavelink.Karaoke(
        level=0.9, mono_level=0.9, filter_band=220.0, filter_width=110.0)),
                          seek=False)

    elif selected_filter == "DeepBass":
      vc = interaction.guild.voice_client
      bands = [(0, 0.3), (1, 0.2), (2, 0.1), (3, 0.05), (4, -0.05), (5, -0.1),
               (6, -0.1), (7, -0.1), (8, -0.1), (9, -0.1), (10, -0.1),
               (11, -0.1), (12, -0.1), (13, -0.1), (14, -0.1)]
      await vc.set_filter(
        wavelink.Filter(
          equalizer=wavelink.Equalizer(name="Deepbass", bands=bands)))

    embed = discord.Embed(
      description=f"`{selected_filter}` **filter will be applied soon...**")
    await interaction.response.send_message(embed=embed, ephemeral=True)


class DropdownView(discord.ui.View):

  def __init__(self):
    super().__init__()
    self.add_item(Dropdown())

class Music(commands.Cog):
    emoji = "🥀"
    def __init__(self, client: commands.Bot):
        self.mlist = []
        self.client = client
        self.last_track = None
        self.asongs = []
        self.last_song = None
        self.autoplay = False

        self.client.loop.create_task(self.connect_nodes())
    
    @commands.hybrid_command(name="autoplay")
    async def _autoplay(self, ctx):
      global autoplay
      if not self.autoplay:
        self.autoplay = True
        autoplay = True
        await ctx.send("<a:cx_tick:1173190431295676416> | Successfully enabled autoplay mode.")
      else:
        self.autoplay = False
        autoplay = True
      #await ctx.reply(f"Successfully Set Autoplay to {self.autoplay}")
        await ctx.send("<a:cx_tick:1173190431295676416> | Successfully disabled autoplay mode, If you wanna activate it you have to re-use the command.")

    
    @commands.Cog.listener()
    async def on_ready(self):
      songs = ["t series latest songs", "Punjabi songs latest", "hindi songs latest"]
      choice = random.choice(songs)
      songs=await wavelink.YouTubeTrack.search(choice)
      self.asongs = songs
      await self.setsongs.start()

    
    @tasks.loop(seconds=10)
    async def setsongs(self):
      if not self.autoplay:
        return
      songs = ["t series latest songs", "Punjabi songs latest", "hindi songs latest"]
      choice = random.choice(songs)
      songs=await wavelink.YouTubeTrack.search(choice)
      self.asongs = songs



      
  
    async def connect_nodes(self):
        await self.client.wait_until_ready()
        try:
          await wavelink.NodePool.create_node(bot=self.client,host="lavalink4.alfari.id",port=80, password="catfein", https=False,spotify_client=spotify.SpotifyClient(
                client_id="a48224141ca649079fbc5f443a6396ab",
                client_secret="a4008dc4c4994dab932e30a7e9ae16f3"))
       
          print("Node Created!")
        except Exception as e:
          print(e)
    
    async def choose_one(self, ctx, tracks):
        what = 0
        view = View()
        btn1 = Button(label="", style=discord.ButtonStyle.gray, emoji="1️⃣",row=1)
        btn2 = Button(label="", style=discord.ButtonStyle.gray, emoji="2️⃣",row=1)
        btn3 = Button(label="", style=discord.ButtonStyle.gray, emoji="3️⃣",row=1)
        btn4 = Button(label="", style=discord.ButtonStyle.gray, emoji="4️⃣",row=1)
        btn5 = Button(label="", style=discord.ButtonStyle.gray, emoji="5️⃣",row=1)
        async def btn1_(interaction: discord.Interaction):
          what = 0
        async def btn2_(interaction: discord.Interaction):
          what = 1
        async def btn3_(interaction: discord.Interaction):
          what = 2
        async def btn4_(interaction: discord.Interaction):
          what = 3
        async def btn5_(interaction: discord.Interaction):
          what = 5
        btn1.callback = btn1_
        btn2.callback = btn2_
        btn3.callback = btn3_
        btn4.callback = btn4_
        btn5.callback = btn5_
        view.add_item(btn1)
        view.add_item(btn2)
        view.add_item(btn3)
        view.add_item(btn4)
        view.add_item(btn5)

        def _check(r, u):
            return (
                r.emoji in OPTIONS.keys()
                and u == ctx.author
                and r.message.id == msg.id
            )

        embed = discord.Embed(
            title="Multiple tracks found. Please choose one of the following",
            description=(
                "\n".join(f"{i+1}- | {t.title}" for i, t in enumerate(tracks[:5]))
            ),
            color=0x2f3136
        )
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        msg = await ctx.send(embed=embed, view=view)
        return tracks[what]

    @commands.command(name="volume", usage="vol", description="Sets the volume of the player")
    @commands.cooldown(1,2,commands.BucketType.user)
    async def _allahisone(self, ctx, volume: int):
      embed = discord.Embed(color=0x2f3136)
      if volume < 1 or volume > 500:
        embed.description = "<a:cx_tick:1173190431295676416> | Choose the volume limit between 1 to 500"
        return await ctx.reply(embed=embed)
      if ctx.voice_client == None:
        return await ctx.send("You are not connected to any voice channel.")
      chnl: wavelink.Player = ctx.voice_client
      if not chnl.is_playing():
        embed.description ="<a:no:1173190365076017192> | Play the music to use volume command"
        return await ctx.reply(embed=embed)
      await chnl.set_volume(volume / 500)
      embed.description = f"<a:cx_tick:1173190431295676416> | The volume level has been set to {volume}%"
      await ctx.send(embed=embed)

    @commands.command(name="connect", aliases=["join","j","jvc"], usage="connect <channel>")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def connect(self, ctx: commands.Context, *, channel: discord.VoiceChannel=None):
        """Connects to a voice channel"""
        if not getattr(ctx.author, "voice", None):
            await ctx.send("You are not connected to any voice channel.")
            return
        if channel is None:
            channel = ctx.author.voice.channel
        elif ctx.voice_client:
            av = discord.Embed(description=f"<a:cx_tick:1173190431295676416> | I am already connected to a voice channel.", color=0x2f3136)
            await ctx.send(embed=av)
            return
        vc: wavelink.Player = await channel.connect(cls=wavelink.Player)
        await ctx.send(f"<a:no:1173190365076017192>| Successfully Joined {channel.mention}.", delete_after=10)
    
    @commands.command(name="disconnect", aliases=['leave','dc'], usage="[disconnect|leave] <channel>")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def disconnect(self, ctx: commands.Context, *, channel: discord.VoiceChannel=None):
        """Disconnects from a voice channel"""
        if not getattr(ctx.author, "voice", None):
          await ctx.send("You are not connected to any voice channel.")
          return
        if channel == None:
          channel = ctx.author.voice.channel
        elif not ctx.voice_client:
            await ctx.send("I am not in any voice channel.")
            return
        elif ctx.author.voice.channel != ctx.voice_client.channel:
            svc = discord.Embed(description=f"<a:cx_tick:1173190431295676416>| You should be in the same voice channel that I'm in.", color=0x2f3136)
            await ctx.send(embed=svc)
            return
        vc: wavelink.Player = ctx.voice_client
        await vc.disconnect()
        await ctx.message.add_reaction("👋")
    
    @commands.command(name="play", aliases=['p'], usage="[play|p] [query]", description="Play songs in your voice channel")
    async def play(self, ctx: commands.Context, *, query: str):
        """Listen to lag-free music."""
        try:
          if ctx.voice_client.channel.id != ctx.author.voice.channel.id: 
            vc = ctx.voice_client
            await vc.disconnect()
        except:
          pass
        if not getattr(ctx.author, "voice", None):
            nvc = discord.Embed(description=f"<a:no:1173190365076017192> | You are not connected to a voice channel.", color=0x2f3136)
            await ctx.send(embed=nvc)
            return
        elif not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
            await ctx.send(f"<a:cx_tick:1173190431295676416> | Successfully Joined {ctx.author.voice.channel.mention}", delete_after=10)
        else:
            vc: wavelink.Player = ctx.voice_client
        
        tracks = await wavelink.YouTubeTrack.search(query)
      
        self.mlist = tracks
        btn1 = Button(label="", style=discord.ButtonStyle.gray, emoji="1️⃣",row=1)
        btn2 = Button(label="", style=discord.ButtonStyle.gray, emoji="2️⃣",row=1)
        btn3 = Button(label="", style=discord.ButtonStyle.gray, emoji="3️⃣",row=1)
        btn4 = Button(label="", style=discord.ButtonStyle.gray, emoji="4️⃣",row=1)
        btn5 = Button(label="", style=discord.ButtonStyle.gray, emoji="5️⃣",row=1)
        btn6 = Button(label="", style=discord.ButtonStyle.gray, emoji="⏹️",row=2)
        async def btn1_(interaction: discord.Interaction):
          await self.damn(vc=vc, index=0, tracks=tracks, ctx=ctx)
          btn1.disabled = True
          
        async def btn2_(interaction: discord.Interaction):
          await self.damn(vc=vc, index=1, tracks=tracks, ctx=ctx)
          btn2.disabled = True
        async def btn3_(interaction: discord.Interaction):
          await self.damn(vc=vc, index=2, tracks=tracks, ctx=ctx)
          btn3.disabled = True
        async def btn4_(interaction: discord.Interaction):
          await self.damn(vc=vc, index=3, tracks=tracks, ctx=ctx)
          btn4.disabled = True
        async def btn5_(interaction: discord.Interaction):
          await self.damn(vc=vc, index=4, tracks=tracks, ctx=ctx)
          btn5.disabled = True
        async def btn6_(interaction: discord.Interaction):
          await vc.smex.delete()
        btn1.callback = btn1_
        btn2.callback = btn2_
        btn3.callback = btn3_
        btn4.callback = btn4_
        btn5.callback = btn5_
        btn6.callback = btn6_
        view = View()
        view.add_item(btn1)
        view.add_item(btn2)
        view.add_item(btn3)
        view.add_item(btn4)
        view.add_item(btn5)
        view.add_item(btn6)
        embed = discord.Embed(
            title="Multiple tracks found. Please choose one of the following",
            description=(
                "\n".join(f"**`[{i+1}]` | {t.title}**" for i, t in enumerate(tracks[:5]))
            ),
            color=0x2f3136
        )
        embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar)
        smex = await ctx.send(embed=embed, view=view)
        vc.smex = smex
    async def damn(self, vc: wavelink.Player, index: int, tracks, ctx):
      idk:wavelink.abc.Playable = tracks[index]
      if not vc.is_playing():
        await vc.play(idk)
        #await vc.set_volume(100)
        self.last_s = {"t": idk, "search": tracks}
        setattr(vc,"ctx",ctx)
        view = MusicView(vc,ctx,idk.length,self.last_song,idk)
        view.add_item(Dropdown())
        embed = discord.Embed(title="**Now playing:**", description=f"• <a:a_dj:1195717009179152455>{idk.title}", color=0xff0000)
        embed.add_field(name="<:stage:1173459161745457212> Song By",

                               value=f"`{idk.author}`")

        embed.add_field(name="<a:hx_time:1173459120850997368> Duration",

                               value=f"`❯ { round(idk.duration / 60, 2)}`")

        embed.set_author(name="NOW PLAYING",

                                icon_url=f"{ctx.author.avatar}")

        embed.set_footer(text=f"Requested By {ctx.author}",

                                icon_url=f"{ctx.author.avatar}")

        embed.timestamp = discord.utils.utcnow()
        if getattr(idk, "uri", None) is not None:
          print(idk.uri)
          embed.set_image(url=idk.thumbnail)
        await vc.smex.edit(embed=embed, view=view)
      else:
        await vc.queue.put_wait(idk)
        await vc.smex.edit(embed=discord.Embed(title="Music Queue", description=f"Added {idk.title} to queue.", color=0x2f3136), view=None)
        setattr(vc,"ctx",ctx)
        setattr(vc, "loop", False)
    
    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: wavelink.Player, track: wavelink.tracks, reason):
        ctx = player.ctx
        vc: player = ctx.voice_client
        
        if self.autoplay:
          if vc.is_playing():
            return
          autplay = random.choice(self.asongs)
          view = MusicView(vc,ctx,autplay.length,self.last_song,autplay)
          view.add_item(Dropdown())
          await vc.play(autplay)
          embed=discord.Embed(title="**Now playing:**", description=f"• <a:a_dj:1195717009179152455>{autplay.title}", color=0xff0000)
          embed.add_field(name="<:stage:1173459161745457212> Song By",

                               value=f"`{autplay.author}`")

          embed.add_field(name="<a:hx_time:1173459120850997368> Duration",

                               value=f"`❯ { round(autplay.duration / 60, 2)}`")

          embed.set_author(name="NOW PLAYING",

                                icon_url=f"{ctx.author.avatar}")

          embed.set_footer(text="Autoplay made by: Saurabh")

          embed.timestamp = discord.utils.utcnow()
          #embed.set_footer(text="Autoplay made by: Auth#1337")
          if getattr(autplay, "uri", None) is not None:
            embed.set_image(url=autplay.thumbnail)
            await ctx.send(embed=embed,view=view)

        if player.loop:
            view = MusicView(vc,ctx,lopi.length,self.last_song,lopi)
            view.add_item(Dropdown())
            await player.play(lopi)
            embed=discord.Embed(title="**Now playing:**", description=f"• <a:a_dj:1195717009179152455>{lopi.title}", color=0xff0000)
            embed.add_field(name="<:stage:1173459161745457212> Song By",

                               value=f"`{lopi.author}`")

            embed.add_field(name="<a:hx_time:1173459120850997368> Duration",

                               value=f"`❯ { round(lopi.duration / 60, 2)}`")

            embed.set_author(name="NOW PLAYING",

                                icon_url=f"{ctx.author.avatar}")

            embed.set_footer(text=f"Requested By {ctx.author}",

                                icon_url=f"{ctx.author.avatar}")

            embed.timestamp = discord.utils.utcnow()
            if getattr(lopi, "uri", None) is not None:
              embed.set_image(url=lopi.thumbnail)
            await ctx.send(embed=embed,view=view)
        
        if not player.queue.is_empty:
            next_track = await vc.queue.get_wait()
            await vc.play(next_track)
            #await vc.set_volume(100)
            embed=discord.Embed(title="**Now playing:**", description=f"• <a:a_dj:1195717009179152455>{next_track.title}", color=0xff0000)
            embed.add_field(name="<:stage:1173459161745457212> Song By",

                               value=f"`{next_track.author}`")

            embed.add_field(name="<a:hx_time:1173459120850997368> Duration",

                               value=f"`❯ { round(next_track.duration / 60, 2)}`")

            embed.set_author(name="NOW PLAYING",

                                icon_url=f"{ctx.author.avatar}")

            embed.set_footer(text=f"Requested By {ctx.author}",

                                icon_url=f"{ctx.author.avatar}")

            embed.timestamp = discord.utils.utcnow()
            if getattr(next_track, "uri", None) is not None:
              embed.set_image(url=next_track.thumbnail)
            await ctx.send(embed=embed, view=view)

    @commands.command(name="loop", usage="loop", description="Toggle looping your currently playing track")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def loop(self, ctx: commands.Context):
        if not ctx.voice_client:
            svc = discord.Embed(description=f"<a:no:1173190365076017192> | I am not connected to a voice channel.", color=0x2f3136)
            await ctx.send(embed=svc)
            return
        elif not getattr(ctx.author, "voice", None):
            nvc = discord.Embed(description=f"<a:no:1173190365076017192> | You are not connected to a voice channel to do this.", color=0x2f3136)
            await ctx.send(embed=nvc)
            return
        else:
            vc: wavelink.Player = ctx.voice_client
        if not vc.is_playing():
            bvc = discord.Embed(description=f"<a:no:1173190365076017192> | I am not playing anything.", color=0x2f3136)
            await ctx.send(embed=bvc)
            return
        vc.loop = True if not vc.loop else False
        mvc = discord.Embed(description=f"<a:cx_tick:1173190431295676416> | Looping set to {'**True**.' if vc.loop else '**False**.'}", color=0x2f3136)
        await ctx.send(embed=mvc)
    
    @commands.command(name="stop", usage="stop", description='Stop the player & clear the whole queue')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stop(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description=f"<a:no:1173190365076017192> | I am not connected to a voice channel.", color=0x2f3136))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | You are not connected to a voice channel to do this.", color=0x2f3136))
            return
        else:
            vc: wavelink.Player = ctx.voice_client
        if vc.is_playing() is False:
            await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | I am not playing anything.", color=0x2f3136))
            return

        await vc.stop()
        vc.queue.clear()
        await ctx.send(embed=discord.Embed(description=f"<a:cx_tick:1173190431295676416> | Destroyed the player.", color=0x2f3136))
    
    @commands.group(name="queue", usage="queue", description="Display the queue ln this server")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def queue(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            if not ctx.voice_client:
                await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | There is nothing playing yet.", color=0x2f3136))
            elif not getattr(ctx.author.voice, "channel", None):
                await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | You are not connected to a voice channel to do this.", color=0x2f3136))
            else:
                vc: wavelink.Player = ctx.voice_client
            
            if vc.queue.is_empty:
                return await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | There are no more tracks in the queue.", color=0x2f3136))
            
            embed = discord.Embed(title="Music Queue", color=0x2f3136)
            queue = vc.queue.copy()
            description = ""
            for num, track in enumerate(queue):
                description += f"`[{num + 1}]` | " + f"{track.title}" + "\n"
            embed.description = description
            await ctx.send(embed=embed)

    @queue.command(name="clear", usage="queue clear", description='Clears the queue of the server')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def clear(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | I am not connected to a voice channel.", color=0x2f3136))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | You are not connected to a voice channel to do this.", color=0x2f3136))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        vc.queue.clear()
        await ctx.send(embed=discord.Embed(description="Cleared the queue.", color=0x2f3136))
    
    @commands.command(name="pause", usage="pause", description="Pause the player")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def pause(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | I am not connected to a voice channel.", color=0x2f3136))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | You are not connected to a voice channel to do this.", color=0x2f3136))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            return await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | There is nothing playing yet.", color=0x2f3136))
        await vc.pause()
        await ctx.send(embed=discord.Embed(description="Paused the player.", color=0x2f3136))
    
    @commands.command(name="resume", usage="resume", description="Resume the current paused song")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def resume(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | I am not connected to a voice channel.", color=0x2f3136))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | You are not connected to a voice channel to do this.", color=0x2f3136))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            return await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | There is nothing playing yet.", color=0x2f3136))
        await vc.resume()
        await ctx.send(embed=discord.Embed(description="<a:cx_tick:1173190431295676416> | Resumed the player.", color=0x2f3136))
        
    @commands.command(name="nowplaying", usage="nowplaying")
    async def playing(self, ctx):
        if not ctx.voice_client:
            hacker = discord.Embed(
                description=
                "<a:no:1173190365076017192> | Not connected to a voice channel.",
                color=0x00FFED)
            hacker.set_footer(text=f"Requested By {ctx.author}",
                              icon_url=f"{ctx.author.avatar}")
            hacker.set_thumbnail(url=f"{ctx.author.avatar}")
            
            return await ctx.send(embed=hacker)
        elif not getattr(ctx.author.voice, "channel", None):
            hacker1 = discord.Embed(
                description=
                "<a:no:1173190365076017192> | You are not connected to a voice channel.",
                color=0x00FFED)
            hacker1.set_footer(text=f"Requested By {ctx.author}",
                               icon_url=f"{ctx.author.avatar}")
            hacker1.set_thumbnail(url=f"{ctx.author.avatar}")
            hacker1.timestamp = discord.utils.utcnow()
            return await ctx.send(embed=hacker1)
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            hacker1 = discord.Embed(
                description=
                "<a:no:1173190365076017192> | I am not playing anything .",
                color=0x00FFED)
            hacker1.set_footer(text=f"Requested By {ctx.author}",
                               icon_url=f"{ctx.author.avatar}")
            hacker1.set_thumbnail(url=f"{ctx.author.avatar}")
            hacker1.timestamp = discord.utils.utcnow()
            return await ctx.send(embed=hacker1)

        em = discord.Embed(
            description=f"[{vc.track}](https://discord.gg/)",
            color=0x00FFED)

        em.add_field(name="<:stage:1173459161745457212> Song By",
                     value=f"`{vc.track.author}`")
        em.add_field(
            name="<a:hx_time:1173459120850997368> Duration",
            value=f"`❯ {datetime.timedelta(seconds=vc.track.length)}`")
        em.set_footer(text=f"Requested By {ctx.author}",
                      icon_url=f"{ctx.author.avatar}")
        em.set_author(name="NOW PLAYING", icon_url=f"{ctx.author.avatar}")
        em.set_thumbnail(url=f"{ctx.author.avatar}")
        em.timestamp = discord.utils.utcnow()
        return await ctx.send(embed=em)
      
   
    @commands.command(name="skip", usage="skip", description="Skip the current playing track")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def skip(self, ctx: commands.Context):
        try:
          if self.autoplay:
            vc = self.ctx.voice_client
            await vc.stop()
            return await ctx.reply("<a:cx_tick:1173190431295676416> | Song skipped.")
        except:
          pass
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | I am not connected to a voice channel.", color=0x2f3136))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | You are not connected to a voice channel to do this.", color=0x2f3136))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            await ctx.send(embed=discord.Embed(description="<a:no:1173190365076017192> | There is nothing playing yet.", color=0x2f3136))
            return
        try:
          track_ski = await vc.queue.get_wait()
          if track_ski is None:
            return await ctx.send("byeeeeeeeeee ")
        except:
          await vc.stop()
          return await ctx.send("skipped")
        view = MusicView(vc=vc, ctx=ctx,length=track_ski.length,lasts=self.last_track,now=track_ski)
        await vc.play(track_ski)
        await ctx.send(embed=discord.Embed(description="<a:cx_tick:1173190431295676416> | Skiped the track.", color=0x2f3136))
        embed=discord.Embed(title="Now Playing", description=f"{track_ski.title}", color=0x2f3136)
        embed.add_field(name="<:stage:1173459161745457212> Song By",

                               value=f"`{track_ski.author}`")

        embed.add_field(name="<a:hx_time:1173459120850997368> Duration",

                               value=f"`❯ { round(track_ski.duration / 60, 2)}`")

        embed.set_author(name="NOW PLAYING",

                                icon_url=f"{ctx.author.avatar}")

        embed.set_footer(text=f"Requested By {ctx.author}",

                                icon_url=f"{ctx.author.avatar}")

        embed.timestamp = discord.utils.utcnow()
        embed.set_image(url=track_ski.thumbnail)
        view = MusicView(vc,ctx,lopi.length,self.last_song,lopi)

        view.add_item(Dropdown())
        await ctx.send(embed=embed, view=view)


async def setup(bot):
  await bot.add_cogs(music (bot))