"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
MADE BY @LEGENDX22 dont kang this plugin
CREDITS = @LEGENDX22 @PROBOY22 @alain_champion
Special thanks @alain_champion for this modified version
if you kang then keep credits
"""
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PHOTTO = Var.ALIVE_PHOTTO
if ALIVE_PHOTTO is None:
  ALIVE_PHOTTO = "https://telegra.ph/file/0e36b02061064b7229e3b.jpg"


DEFAULTUSER = bot.me.first_name

global randi
BOT = "ULTROID X"        
#make by LEGEND X bht mehnat lag gayi yrr but banhi gaya 😅           
#@command(outgoing=True, pattern="^.awake$")
@ultroi_cmd(pattern="awake")
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   tag = borg.uid
   ALIVE_MESSAGE= f" ⚡️ {BOT} ⚡️  IS ON 🔥 FIRE 🔥"
   ALIVE_MESSAGE += "\n\n"
   ALIVE_MESSAGE += "💟 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂 💟\n\n"
   ALIVE_MESSAGE += "☎️ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ☎️ : 6.0.9\n\n"
   ALIVE_MESSAGE += "🔶 𝙻𝙴𝙶𝙴𝙽𝙳 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 🔶 :   2.8\n\n"
   ALIVE_MESSAGE += f"💠 𝙼𝚈 𝙱𝙾𝚂𝚂 💠: [{DEFAULTUSER}](tg://user?id={tag})\n\n"
   ALIVE_MESSAGE += "🔰 𝙶𝚁𝙾𝚄𝙿 🔰 : [SUPPORT](https://t.me/LEGEND_USERBOT_SUPPORT)\n\n"
   ALIVE_MESSAGE += f"💠 [𝙳𝙴𝙿𝙻𝙾𝚈](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2FLEGEN-BOT&template=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2FLEGEND-ROBOT) 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙾𝙿 [{BOT}](http://github.com/legendxop/legend-bot)  💠\n"   
   await awake.delete() 
   await borg.send_file(awake.chat_id, ALIVE_PHOTTO,caption=ALIVE_MESSAGE)

