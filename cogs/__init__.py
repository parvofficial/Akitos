from __future__ import annotations
from core import Astroz



#____________ Commands ___________

#####################3
from .commands.help import Help
from .commands.general import General
from .commands.music import Music
from .commands.moderation import Moderation
from .commands.mod import mod
from .commands.anti import Security
from .commands.raidmode import Automod
from .commands.welcome import Welcomer
from .commands.fun import Fun
from .commands.Games import Games
from .commands.extra import Utility
from .commands.owner import Owner
from .commands.owner1 import owner1
from .commands.vcroles import Voice
from .commands.role import Server
from .commands.ignore import Ignore
from .commands.vanityroles import Vanityroles
from .commands.Logging import Logging
from .commands.pfps import pfps
from .commands.Verification import Verification
from .commands.media import Media
from .commands.Afk import afk
from .commands.giveaway import Giveaways
from .commands.ticket import Ticket
#from .commands.boost import boost
from .commands.youtube import Youtube
#from .commands.embed import Embed
from .commands.about import About
from .commands.calculator import calculator 
from .commands.zestar import Zestar
from .commands.serverinfo import Info
from .commands.List import list 
#from .commands.ytnotification import ytnotification 

#____________ Events _____________
from .events.antiban import antiban
from .events.antichannel import antichannel
from .events.antiguild import antiguild
from .events.antirole import antirole
from .events.antibot import antibot
from .events.antikick import antikick
from .events.antiprune import antiprune
from .events.antiwebhook import antiwebhook
from .events.antiping import antipinginv
from .events.antiemostick import antiemostick
from .events.antintegration import antintegration
from .events.antispam import AntiSpam
from .events.autoblacklist import AutoBlacklist
from .events.antiemojid import antiemojid
from .events.antiemojiu import antiemojiu
from .events.Errors import Errors
from .events.on_guild import Guild
from .events.autorole import Autorole2
from .events.greet2 import greet
from .events.voiceupdate import Vcroles2
from .events.join import Join
# from .events.boost2 import bst
# from .events.boost3 import Boost3



##############33cogs#############
from .commands.anti1 import akito1
from .commands.logging1 import akito111111
from .commands.mod2 import akito111111111
from .commands.extra1 import akito11111111111
from .commands.games1 import akito1111111111
from .commands.welcome1 import akito11111
from .commands.raidmode1 import akito1111
from .commands.music1 import akito111
from .commands.server import akito11111111
from .commands.verification1 import akito22
from .commands.general1 import akito11
from .commands.media1 import akito222
from .commands.pfps1 import pfps1
from .commands.voice import akito111111111111
from .commands.vcrole1 import akito2
from .commands.vanityroles1 import akito11111111111111
from .commands.giveaway1 import gw1
from .commands.ticket1 import akito1111111
from .commands.autoresponder import akito2222
# from .commands.boost1 import velo1






async def setup(bot: Astroz):
  await bot.add_cog(Help(bot))
  await bot.add_cog(General(bot))
  await bot.add_cog(Music(bot))
  await bot.add_cog(Moderation(bot))
  await bot.add_cog(Security(bot))
  await bot.add_cog(Automod(bot))
  await bot.add_cog(Welcomer(bot))
  await bot.add_cog(Fun(bot))
  await bot.add_cog(Games(bot))
  await bot.add_cog(Utility(bot))
  await bot.add_cog(Voice(bot))
  await bot.add_cog(Owner(bot))
  await bot.add_cog(owner1(bot))
  await bot.add_cog(Server(bot))
  await bot.add_cog(Vanityroles(bot))
  await bot.add_cog(Ignore(bot))
  await bot.add_cog(Logging(bot))
  await bot.add_cog(pfps(bot))
  await bot.add_cog(Verification(bot))
  await bot.add_cog(Media(bot))
  await bot.add_cog(afk(bot))
  await bot.add_cog(Giveaways(bot))
  await bot.add_cog(Ticket(bot))
 # await bot.add_cog(boost(bot))
  await bot.add_cog(Youtube(bot))
 # await bot.add_cog(Embed(bot))
  await bot.add_cog(About(bot))
  await bot.add_cog(calculator(bot))
  await bot.add_cog(Zestar(bot)) 
  await bot.add_cog(mod(bot))
  await bot.add_cog(Info(bot))
  await bot.add_cog(list(bot))
 # await bot.add_cog(ytnotification(bot))
    
####################



  await bot.add_cog(akito1(bot))
  await bot.add_cog(gw1(bot))
  await bot.add_cog(akito111111(bot))
  await bot.add_cog(akito111111111(bot))
  await bot.add_cog(akito11111111111(bot))
  await bot.add_cog(akito1111111111(bot))
  #await bot.add_cog(velo1(bot))
  await bot.add_cog(akito11111(bot))
  await bot.add_cog(akito1111(bot))
  await bot.add_cog(akito111(bot))
  await bot.add_cog(akito11111111(bot))
  await bot.add_cog(akito22(bot)) 
  await bot.add_cog(akito11(bot)) 
  await bot.add_cog(akito222(bot))
  await bot.add_cog(akito1111111(bot))
  await bot.add_cog(pfps1(bot))
  await bot.add_cog(akito2222(bot))
  await bot.add_cog(akito111111111111(bot))
  await bot.add_cog(akito2(bot))
  await bot.add_cog(akito11111111111111(bot))
    

    
###########################events################3
  
  await bot.add_cog(antiban(bot))
  await bot.add_cog(antichannel(bot))
  await bot.add_cog(antiguild(bot))
  await bot.add_cog(antirole(bot))
  await bot.add_cog(antibot(bot))
  await bot.add_cog(antikick(bot))
  await bot.add_cog(antiprune(bot))
  await bot.add_cog(antiwebhook(bot))
  await bot.add_cog(antipinginv(bot))
  await bot.add_cog(antiemostick(bot))
  await bot.add_cog(antintegration(bot))  
  await bot.add_cog(AntiSpam(bot))
  await bot.add_cog(AutoBlacklist(bot))
  await bot.add_cog(antiemojid(bot))
  await bot.add_cog(antiemojiu(bot))
  await bot.add_cog(Guild(bot))
  await bot.add_cog(Errors(bot))
  await bot.add_cog(Autorole2(bot))
  await bot.add_cog(greet(bot))
  await bot.add_cog(Vcroles2(bot))
  await bot.add_cog(Join(bot))
 # await bot.add_cog(bst(bot))
 # await bot.add_cog(Boost3(bot))