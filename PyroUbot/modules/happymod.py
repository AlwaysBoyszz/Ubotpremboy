from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ʜᴀᴘᴘʏᴍᴏᴅ"
__HELP__ = """
<b>✮ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʜᴀᴘᴘʏᴍᴏᴅ ✮</b>

<blockquote><b>perintah :
<code>{0}apmod</code> [ɴᴀᴍᴀ ᴀᴘᴋ]
ᴍᴇɴᴄᴀʀɪ ᴀᴘʟɪᴋᴀsɪ ᴍᴏᴅ ᴀɴᴅʀᴏɪᴅ</b></blockquote>
"""

@PY.UBOT("apmod")
async def _(client, message):
    args = message.text.split(" ", 1)

    if len(args) < 2:
        await message.reply_text("<blockquote><b><emoji id=5215204871422093648>❌</emoji> Harap gunakan format:\n`.apmod <nama_aplikasi>`</b></blockquote>", quote=True)
        return

    query = args[1]
    api_url = f"https://api.botcahx.eu.org/api/search/happymod?query={query}&apikey=Boyy"

    try:
        response = requests.get(api_url)
        data = response.json()

        if not data.get("status") or "result" not in data:
            await message.reply_text("<blockquote><b><emoji id=5215204871422093648>❌</emoji> Tidak ditemukan hasil untuk pencarian ini.</b></blockquote>", quote=True)
            return

        results = data["result"][:5]
        response_text = "<blockquote><b><emoji id=4943239162758169437>🤩</emoji> **Hasil Pencarian HappyMod:**\n\n</b></blockquote>"

        for item in results:
            title = item["title"]
            icon = item["icon"]
            rating = item["rating"]
            link = item["link"]

            response_text += (
                f"""
<blockquote><b>**__📌 {title}
<emoji id=5219827798125846744>👑</emoji> ʀᴀᴛɪɴɢ ᴀᴘᴋ: {rating}
<emoji id=5271604874419647061>🔗</emoji> [ᴜɴᴅᴜʜ ᴅɪ ʜᴀᴘᴘʏᴍᴏᴅ]({link})__**</b></blockquote>"""
            )

        await message.reply_text(response_text, disable_web_page_preview=True, quote=True)
    except Exception as e:
        await message.reply_text(f"<blockquote><b><emoji id=5215204871422093648>❌</emoji> Terjadi kesalahan:\n`{str(e)}`</b></blockquote>", quote=True)
