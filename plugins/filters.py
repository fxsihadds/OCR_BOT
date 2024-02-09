# Import necessary modules
from pyrogram import filters, Client
from pyrogram.types import Message
import os
import requests
import base64
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
api_key = config['GOOGLE']['VISION_KEY']

# This func for Local Single Photos
def ocr_image_single(image_path, api_key):
    endpoint = "https://vision.googleapis.com/v1/images:annotate"
    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip",
        "User-Agent": "FirebaseML_[DEFAULT] Google-API-Java-Client Google-HTTP-Java-Client/1.25.0-SNAPSHOT (gzip)",
        "x-android-package": "com.inverseai.image_to_text_OCR_scannes",
        "x-android-cert": "C9E5C6094C5B966C4DD3C8E65B144622E21AC254"
    }
    params = {
        "key": api_key
    }

    with open(image_path, "rb") as image_file:
        image_content = base64.b64encode(image_file.read()).decode("utf-8")

    request_body = {
        "requests": [{
            "image": {"content": image_content},
            "features": [{"type": "TEXT_DETECTION"}]
        }]
    }

    response = requests.post(
        endpoint,
        headers=headers,
        params=params,
        json=request_body
    )

    if response.status_code == 200:
        result = response.json()
        if "textAnnotations" in result["responses"][0]:
            text = result["responses"][0]["textAnnotations"][0]["description"]
            return text
        else:
            return "No Text Tound, Please Provide Photos."
    else:
        return "Error: {}".format(response.status_code)

# Command handler for OCR command
@Client.on_message(filters.document | filters.photo)
async def ocr_command(client, message):
    status = await message.reply_text("<b>⎚ `Processing image...`</b>")
    download = await client.download_media(message.photo or message.document)
    recognized_text = ocr_image_single(image_path=download, api_key=api_key)
    await status.edit_text(f"""{recognized_text}""")        
    os.remove(download)






