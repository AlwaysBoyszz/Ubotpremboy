import requests
import qrcode
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ǫʀɪs ɢᴇɴᴇʀᴀᴛᴇ"
__HELP__ = """
<blockquote><b>Bantuan Untuk QRIS Generator</b>

Perintah:
<code>{0}qris [nominal]</code> → Membuat QRIS sesuai nominal yang dimasukkan (Hanya untuk Owner)

Sumber: API OkeConnect.</blockquote></b>
"""

# Data dari OrderKuota
MERCHANT_ID = "OK1174104"
API_KEY = "513021717379960191174104OKCT8B1C2E06B64BACA29A563DF92055DFB1"
CODE_QR = "00020101021126670016COM.NOBUBANK.WWW01189360050300000879140214615534398557520303UMI51440014ID.CO.QRIS.WWW0215ID20232690040570303UMI5204481253033605802ID5920BOYS STORE OK11741046007SUMENEP61056941262070703A016304FC48"

# API QRIS OkeConnect
API_URL = f"https://gateway.okeconnect.com/api/mutasi/qris/{MERCHANT_ID}/{API_KEY}"

# Hanya bisa digunakan oleh Owner
OWNER_ID = [5496456993]  # Ganti dengan ID Telegram Owner

@PY.BOT("qris")
@filters.user(OWNER_ID)
async def _(client, message):
    msg = await message.reply("⏳ Sedang memproses QRIS...")

    # Ambil nominal dari pesan
    args = message.text.split()
    if len(args) < 2 or not args[1].isdigit():
        return await msg.edit("❌ Format salah! Gunakan: <code>.qris [nominal]</code>")

    NOMINAL = int(args[1])

    # Kirim request ke API
    payload = {
        "merchant_id": MERCHANT_ID,
        "api_key": API_KEY,
        "code_qr": CODE_QR,
        "amount": NOMINAL
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            qris_data = response.json()
            qris_code = qris_data.get("qris_code")

            # Generate QR Code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qris_code)
            qr.make(fit=True)

            # Simpan QR ke file
            qr_filename = f"qris_{NOMINAL}.png"
            img = qr.make_image(fill="black", back_color="white")
            img.save(qr_filename)

            await message.reply_document(qr_filename, caption=f"✅ QRIS Rp{NOMINAL} berhasil dibuat!")

        else:
            await msg.edit("❌ Gagal membuat QRIS: " + response.text)

    except Exception as e:
        await msg.edit(f"❌ Error: {str(e)}")