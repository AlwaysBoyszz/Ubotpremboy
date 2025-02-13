from PyroUbot import *
import requests

__MODULE__ = "ʏᴛᴍᴘ4"
__HELP__ = """
<blockquote> <b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛɪᴋᴛᴏᴋ

ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ytmp4</code> vidio atau music <b>[link nya]</b>
ᴘᴇɴᴊᴇʟᴀsᴀɴ : ᴅᴏᴡɴʟᴏᴀᴅ ᴠᴛ ɴᴏ ᴡᴍ , ᴠɪᴅɪᴏ ᴜɴᴛᴜᴋ ᴠɪᴅᴇᴏ ᴍᴜsɪᴄ ᴜɴᴛᴜᴋ ᴍᴜsɪᴋ.</b></blockquote>

"""

@PY.UBOT("ytmp4")
@PY.TOP_CMD
async def tiktok_handler(client, message):
    if len(message.command) < 2:
        await message.reply("linknya mana?")
        return

    url = message.command[1]
    proses_message = await message.reply("```\nprosess...```")

    try:
        response = requests.get(f"https://api.botcahx.eu.org/api/dowloader/yt?url={url}&apikey=Boyy")
        data = response.json()

        if "images" in data["result"]:
            for img_url in data["result"]["images"]:
                await client.send_photo(message.chat.id, img_url)
        else:
            video_url = data["result"]["mp4"]
            video_caption = data["result"]["title"]
            await client.send_video(message.chat.id, video_url, caption=f"```\ndone bay gua```")

        await proses_message.delete()

    except Exception as e:
        await proses_message.delete()
        await message.reply(f"Error \n{e}")
