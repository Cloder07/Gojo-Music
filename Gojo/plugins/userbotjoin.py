
import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Gojo import *
from Gojo.status import *



@Gojo.on(events.NewMessage(pattern="^[!?/]join ?(.*)"))
@Gojo.on(events.NewMessage(pattern="^[!?/]userbotjoin ?(.*)"))
@is_admin
async def _(e, perm):
    chat_id = e.chat_id
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n/ᴊᴏɪɴ <ɢʀᴏᴜᴘ ʟɪɴᴋ/ᴜsᴇʀɴᴀᴍᴇ> ɪғ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪs ᴘʀɪᴠᴀᴛᴇ ᴛʜᴇɴ ᴜsᴇ !ᴘᴊᴏɪɴ <ᴄʜᴀᴛ ʟɪɴᴋ>"
    if e.is_group:
        umm = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = umm[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("sᴜᴄᴄᴇsғᴜʟʟʏ ᴊᴏɪɴᴇᴅ ɪғ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴜsᴇ !ᴘᴊᴏɪɴ ᴀɴᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʟɪɴᴋ")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@Gojo.on(events.NewMessage(pattern="^[!?/]pjoin ?(.*)"))
@is_admin        
async def _(e, perm):
    chat_id = e.chat_id
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n!ᴘᴊᴏɪɴ <ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ's ᴀᴄᴄᴇss ʜᴀsʜ>\n\nExample :\nLink = https://t.me/joinchat/EIIwbORt4v8wOTVl#\n\n!pjoin EIIwbORt4v8wOTVl"
    if e.is_group:
        umm = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            invitelink = umm[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await client(ImportChatInviteRequest(invitelink))
                await event.edit("sᴜᴄᴄᴇsғᴜʟʟʏ ᴊᴏɪɴᴇᴅ")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
    
