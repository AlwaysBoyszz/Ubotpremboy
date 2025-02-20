import os
from PyroUbot import *
import requests

__MODULE__ = "ᴘʟᴀʏʙᴜᴛᴛᴏɴ"
__HELP__ = """
<b>✮ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ✮</b>
<blockquote><b>
ᴘᴇʀɪɴᴛᴀʜ :
<code>{0}ytgold</code>
untuk membuat gold playbutton youtube

✮<code>{0}ytsilver</code>
卍 untuk membuat silver playbutton youtube

✮ <code>{0}iggold</code>
卍 untuk membuat gold playbutton youtube

✮ <code>{0}igsilver</code>
卍 untuk membuat silver playbutton youtube

✮ <code>{0}fbgold</code>
卍 untuk membuat gold playbutton youtube

✮ <code>{0}fbsilver</code>
卍 untuk membuat silver playbutton youtube

✮ <code>{0}twgold</code>
卍 untuk membuat gold playbutton youtube

✮ <code>{0}twsilver</code>
卍 untuk membuat silver playbutton youtube</b></blockquote>

"""

def tweet(text):
    url = "https://api.botcahx.eu.org/api/ephoto/twtsilverbutton"
    params = {
        "text": text,
        "apikey": "Boyy"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
def tweets(text):
    url = "https://api.botcahx.eu.org/api/ephoto/twtgoldbutton"
    params = {
        "text": text,
        "apikey": "Boyy"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None        
def fb(text):
    url = "https://api.botcahx.eu.org/api/ephoto/fbsilverbutton"
    params = {
        "text": text,
        "apikey": "Boyy"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
def fbs(text):
    url = "https://api.botcahx.eu.org/api/ephoto/fbgoldbutton"
    params = {
        "text": text,
        "apikey": "Boyy"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
def robott(text):
    url = "https://api.botcahx.eu.org/api/ephoto/ytsilverbutton"
    params = {
        "text": text,
        "apikey": "Boyy"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
def robottt(text):
    url = "https://api.botcahx.eu.org/api/ephoto/igsilverbutton"
    params = {
        "text": text,
        "apikey": "Boyy"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
def robotttg(text):
    url = "https://api.botcahx.eu.org/api/ephoto/iggoldbutton"
    params = {
        "text": text,
        "apikey": "Boyy"
    }   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None                    
def horor(text):
    url = "https://api.botcahx.eu.org/api/ephoto/ytgoldbutton"
    params = {
        "text": text,
        "apikey": "Boyy"
    }                       
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None

# YOYTUBE        
@PY.UBOT("ytgold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .ytgold Boyy")
        return

    request_text = args[1]
    await message.reply_text("<emoji id=4943239162758169437>🤩</emoji> sedang memproses, mohon tunggu...")

    image_content = horor(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("<emoji id=5215204871422093648>❌</emoji> apikey sedang bermasalah")
                              
@PY.UBOT("ytsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .ytsilver Boyy")
        return

    request_text = args[1]
    await message.reply_text("<emoji id=4943239162758169437>🤩</emoji> sedang memproses, mohon tunggu...")

    image_content = robott(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("<emoji id=5215204871422093648>❌</emoji> apikey sedang bermasalah")
  
# INSTAGRAM                                
@PY.UBOT("iggold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .iggold Boyy")
        return

    request_text = args[1]
    await message.reply_text("<emoji id=4943239162758169437>🤩</emoji> sedang memproses, mohon tunggu...")

    image_content = robotttg(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("<emoji id=5215204871422093648>❌</emoji>apikey sedang bermasalah")
                                  
@PY.UBOT("igsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .igsilver Boyy")
        return

    request_text = args[1]
    await message.reply_text("<emoji id=4943239162758169437>🤩</emoji>sedang memproses, mohon tunggu...")

    image_content = robottt(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("<emoji id=5215204871422093648>❌</emoji>apikey sedang bermasalah")

# FACEBOOK                                   
@PY.UBOT("fbsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .fbsilver Boyy")
        return

    request_text = args[1]
    await message.reply_text("<emoji id=4943239162758169437>🤩</emoji>sedang memproses, mohon tunggu...")

    image_content = fb(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("<emoji id=5215204871422093648>❌</emoji>apikey sedang bermasalah")

@PY.UBOT("fbgold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .fbgold Boyy")
        return

    request_text = args[1]
    await message.reply_text("<emoji id=4943239162758169437>🤩</emoji>sedang memproses, mohon tunggu...")

    image_content = fbs(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("<emoji id=5215204871422093648>❌</emoji>apikey sedang bermasalah")

# TWITTER
@PY.UBOT("twtsilver")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .twtsilver Boyy")
        return

    request_text = args[1]
    await message.reply_text("<emoji id=4943239162758169437>🤩</emoji>sedang memproses, mohon tunggu...")

    image_content = tweet(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("<emoji id=5215204871422093648>❌</emoji>apikey sedang bermasalah")

@PY.UBOT("twtgold")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .twtgold Boyy")
        return

    request_text = args[1]
    await message.reply_text("<emoji id=4943239162758169437>🤩</emoji>sedang memproses, mohon tunggu...")

    image_content = tweets(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("<emoji id=5215204871422093648>❌</emoji>apikey sedang bermasalah")
 
