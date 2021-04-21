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
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

# login to pyrogram client
JEBotZ = Client(
   "URL Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

# start bot
@JEBotZ.on_message(filters.command("start") & ~filters.edited)
async def start(client, message):
    await message.reply("Hello there, I'm Url Uploader bot!",
                        reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton("Source", url="https://github.com/ImJanindu/UrlUploaderBot"),
                                      InlineKeyboardButton("Dev", url="https://t.me/ImJanindu)]])
                       
# url upload
@JEBotZ.on_message(filters.regex(pattern=".*http.*") & ~filters.edited)
async def urlupload(client, message: Message):
    sed = await message.reply("Checking Url 🧐")
    url = message.text
    try: # url download via wget to server
       lel = wget.download(url)
       await sed.edit("Uploading File 📤")
       await message.reply_document(lel) # upload downloaded file
       await sed.delete()
       os.remove(lel) # remove downloaded file from server
    except Exception:
       await sed.edit("Unsupported Url 😐") # print error


print("JEBotZ Started!")

# run bot
JEBotZ.run()
