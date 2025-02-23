import random
from pyrogram import *
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴄᴇᴋ ᴀɢᴀᴍᴀ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Cek Agama</b>

Perintah:
<code>{0}cekagama [nama]</code> → DETEKSI AGAMA DARI NAMA  

Sumber: Random generator berdasarkan nama.</blockquote></b>
"""

AGAMA_LIST = [
    "HINDU","ATEIS (GAK PUNYA AGAMA","ISLAM","KRISTEN","BUDHA","KATOLIK","KRISTEN PROTESTAN","ISLAM KTP","KONGHUCU",
]

@PY.UBOT("cekagama")
@PY.TOP_CMD
async def cek_agama(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.reply_text("⚠️ Gunakan format: .cekagama [nama]")

await message.reply_text(f"<b><i>PROSES MENDETEKSI AGAMANYA '{nama}'</i></b>")

    nama = args[1]
    khodam = random.choice(AGAMA_LIST)
    caption = f'''
    HASIL DETEKSI AGAMA DARI {nama}
    ╭───────────────────────
    ├ ɴᴀᴍᴀ : '{nama}'
    ├ ᴀɢᴀᴍᴀ: '{agama}'
    ├ sᴇʟᴀᴍᴀᴛ ʏᴀ ᴀɢᴀᴍᴀ ɴʏᴀ ᴄᴏᴄᴏᴋ ᴋᴏᴋ
    ╰────────────────────────
    ɴᴏᴛᴇ ᴍᴀᴀғ ʏᴀ {nama} ᴄᴜᴍᴀ ʙᴇᴄᴀɴᴅᴀ ᴋᴏᴋ 😁
    
    '''
    if len(caption) > 1024:
            caption = caption[:1000] + '...'

        await client.send_photo(
            message.chat.id,
            photo= f"https://files.catbox.moe/94ii8p.jpg",
            caption=caption
        )
        
    await message.reply_text(caption)
