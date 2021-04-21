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
from pyrogram.types import Message
from config import Config

# login to pyrogram client
JEBotZ = Client(
   "URL Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

# start bot
@JEBotZ.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello there, I'm Url Uploader bot!")

# url upload
@JEBotZ.on_message(filters.command("url"))
async def urlupload(client, message: Message):
    url = message.text.split(None, 1)[1]
    sed = await message.reply("Checking Url 🧐")
    if "https://" not in url:
        await sed.edit("Is this a Url 🙄")
    else: 
       try: # url download via wget
          lel = wget.download(url)
          await sed.edit("Uploading File...")
          await message.reply_document(lel)
          await sed.delete()
          os.remove(lel) # remove downloaded file from server
       except Exception: # print error
          await sed.edit("Unsupported Url 😐")

print("JEBotZ Started!")

# run bot
JEBotZ.run()
