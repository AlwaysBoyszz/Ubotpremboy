import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "5496456993").split()))

API_ID = int(os.getenv("API_ID", "25732274"))

API_HASH = os.getenv("API_HASH", "10ffdb71c5bdf5fb98ab2199bdd620f7")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7496381843:AAHtWV16t3yfNwAyWF2B7xCwUrr_LDaz_j4")

OWNER_ID = int(os.getenv("OWNER_ID", "5496456993"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002163862717").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://niehh@cluster0.2dvbh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "  -1002163862717"))
