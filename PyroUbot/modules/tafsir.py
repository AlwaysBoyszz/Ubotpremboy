import random
import requests
from PyroUbot import *

__MODULE__ = "ᴛᴀғsɪʀ"
__HELP__ = """
<blockquote><b>Bantuan Untuk tafsir

Perintah : <code>{0}tafsir</code>
    Tafsir adalah ilmu yang menjelaskan makna Al-Qur'an, hukum-hukumnya, dan petunjuk-petunjuknya.</b></blockquote>
"""

@PY.UBOT("tafsir")
async def _(client, message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format yang benar.\nContoh: <code>.tafsir Nabi Muhammad</code>"
            )
            return

        prs = await message.reply_text("<emoji id=5319230516929502602>🔍</emoji> Menjawab...")
        query = message.text.split(' ', 1)[1]
        response = requests.get(f'https://api.botcahx.eu.org/api/islamic/tafsirsurah?text={query}&apikey=Boyy')

        try:
            data = response.json()

            if "result" in data and "surah" in data["result"]:
                x = data["result"]["surah"]
                y = data["result"]["tafsir"]
                await prs.edit(f"<blockquote>SURAH: {x}                                 TAFSIR: {y}</blockquote>")
            else:
                await prs.edit("❌ Respons API tidak memiliki data yang diharapkan.")
        except Exception as err:
            await prs.edit(f"⚠️ Terjadi kesalahan saat memproses respons API: {err}")

    except Exception as e:
        await message.reply_text(f"⚠️ Terjadi kesalahan: {e}")
