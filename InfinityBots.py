#    Copyright (c) 2021 Infinity BOTs <https://t.me/Infinity_BOTs>
 
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.

import os
import wget
from pyrogram import filters, Client
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

# login to pyrogram client
JEBotZ = Client(
   "URL Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

# start message
@JEBotZ.on_message(filters.command("start") & ~filters.edited)
async def start(client, message):
    await message.reply("Hello There, I'm **Url Uploader Bot** 😉\n\nJust Send Me A Url. Do /help for more details 🧐",
                        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Source", url="https://github.com/ImJanindu/UrlUploaderBot"),
                                        InlineKeyboardButton(
                                            "Dev", url="https://t.me/Infinity_BOTs")
                                    ]]
                            ),)

# help message
@JEBotZ.on_message(filters.command("help") & ~filters.edited)
async def help(client, message: Message):
    await message.reply("**Just send me a Url** to upload it as a file.\n\n**NOTE** - Some Urls not supported due to algorithm changes. Make sure your Url not contain charactors like `%`, `@`, etc... and have file extention at the end of Url (better)\n\nEg: `https://telegra.ph/file/28f9af96b75ed6d513fc9.jpg`") 

# url upload
@JEBotZ.on_message(filters.regex(pattern=".*http.*") & ~filters.edited)
async def urlupload(bot, message: Message):
    if Config.UPDATE_CHANNEL:
        try:
            user = await bot.get_chat_member(Config.UPDATE_CHANNEL, update.chat.id)
            if user.status == "kicked":
              thik = await message.reply("You are banned 😕")
              return
        except UserNotParticipant:
            await thik.edit("Join our channel to use me 😉", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Join Channel", url=f"https://t.me/{Config.UPDATE_CHANNEL}")]]))
            return
        except Exception:
            await thik.edit("Something went wrong 😐")
            return
            sed = await message.reply("Trying To Download Url 🧐")
            url = message.text
            cap = "@JEBotZ"
            thurl = "https://telegra.ph/file/a23b8f38fde1914a4bbe9.jpg"
            try: # url download via wget to server
                lel = wget.download(url)
                thumb = wget.download(thurl)
                pak = "a23b8f38fde1914a4bbe9.jpg"
                await sed.edit("Uploading File 🚶‍♂")
                await message.reply_document(lel, caption=cap, thumb=pak) # upload downloaded file
                await sed.delete()
                os.remove(lel) # remove downloaded file from server
                os.remove(thumb) # remove thumbnail file from server
            except Exception:
                await sed.edit("Unsupported Url 😐") # print error


print("JEBotZ Started!")

# run bot
JEBotZ.run()
