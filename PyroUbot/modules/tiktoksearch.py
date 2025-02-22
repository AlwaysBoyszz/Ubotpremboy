from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ᴛɪᴋᴛᴏᴋ sᴇᴀʀᴄʜ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛɪᴋᴛᴏᴋ sᴇᴀʀᴄʜ</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ttsearch</code> 
   <i>penjelasan:</b> untuk mencari vt yang di perintahkan.</i></blockquote>
"""

API_KEY = "Boyy"

@PY.UBOT("tiktoksearch|tts|ttsearch")
async def tiktok_search(client, message):
    if len(message.command) < 2:
        return await message.reply("Gunakan: `.tiktoksearch query`")

    query = " ".join(message.command[1:])
    proses_msg = await message.reply("🔍 **Sedang mencari video TikTok...**")

    url = f"https://api.botcahx.eu.org/api/search/tiktoks?query={query}&apikey={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return await proses_msg.edit("❌ **Gagal mengambil data dari API.**")

    data = response.json()
    if not data.get("status") or not data.get("result", {}).get("data"):
        return await proses_msg.edit("❌ **Tidak ditemukan video untuk query tersebut.**")

    video = data["result"]["data"][0]
    caption = (
        f"🎬 **Judul:** {video['title']}\n"
        f"🌍 **Wilayah:** {video['region']}\n"
        f"🎵 **Musik:** {video['music_info']['title']} - {video['music_info']['author']}\n"
        f"▶ **Jumlah Putar:** {video['play_count']}\n"
        f"❤️ **Like:** {video['digg_count']}\n"
        f"💬 **Komentar:** {video['comment_count']}\n"
        f"🔗 [Tonton di TikTok]({video['play']})"
    )

    await proses_msg.edit("📥 **Mengunduh video...**")

    await message.reply_video(video["play"], caption=caption)

    await proses_msg.delete()
