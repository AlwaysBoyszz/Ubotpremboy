from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴇɴᴄ ᴄᴏᴅᴇ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Enc Code Base 64

perintah : <code>{0}enc</code>
untuk enkripsi code contoh <code>{0}enc</code> (code)</b></blockquote>
"""

@PY.UBOT("enc")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .enc mana code nya"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5267365664389089624>📺</emoji>proccessing....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/tools/base?encode={a}&type=base64&apikey=Boyy')

            try:
                if "result" in data and "encode" in data["result"]:
                x = data["result"]["encode"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
