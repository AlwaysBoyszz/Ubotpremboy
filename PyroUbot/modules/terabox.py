from PyroUbot import *
import requests

__MODULE__ = "ᴛᴇʀᴀʙᴏx"
__HELP__ = """
<blockquote> <b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇʀᴀʙᴏx

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}terabox</code> terabox <b>[link nya]</b>
ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ᴛᴇʀᴀʙᴏx.</b></blockquote>

"""

@PY.UBOT("terabox")
@PY.TOP_CMD
async def tiktok_handler(client, message):
    if len(message.command) < 2:
        await message.reply("linknya mana?")
        return

    url = message.command[1]
    proses_message = await message.reply("```\nProsess Kingz...```")

    try:
        response = requests.get(f"https://api.botcahx.eu.org/api/download/terabox?url={url}&apikey=Boyy")
        data = response.json()

        if "result" in data["result"]:
            for img_url in data["result"]["result"]:
                await client.send_photo(message.chat.id, img_url)
        else:
            video_url = data["result"]["url"]
            video_caption = data["result"]["name"]
            await client.send_video(message.chat.id, video_url, caption=f"```\nDONE KINGZ```")

        await proses_message.delete()

    except Exception as e:
        await proses_message.delete()
        await message.reply(f"Error \n{e}")
        
