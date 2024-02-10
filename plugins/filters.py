# Import necessary modules
from pyrogram import filters, Client
from pyrogram.types import Message
import os
import shutil
import zipfile
from configparser import ConfigParser
from plugins.pdf import extract_images_from_pdf, ocr_image_single, process_images_in_folder

config = ConfigParser()
config.read('config.ini')
api_key = config['GOOGLE']['VISION_KEY']


# Command handler for OCR command
@Client.on_message((filters.document | filters.photo) & (filters.group | filters.private))
async def ocr_command(client, message):
    status = await message.reply_text("<b>⎚ `Processing...`</b>")
    if message.document:
        if message.document.file_name.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
            await status.edit_text("<b>⎚ `Processing image...`</b>")
            download = await client.download_media(message.document)
            recognized_text = ocr_image_single(
                image_path=download, api_key=api_key)
            await status.edit_text(f"{recognized_text}")
            os.remove(download)
        elif message.document.file_name.endswith('.pdf'):
            output_folder = 'pdf'
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            images_output = 'images_from_pdf'
            if not os.path.exists(images_output):
                os.makedirs(images_output)
            await status.edit_text('<b>⎚ `Pdf Proccessing...`</b>')
            download = await client.download_media(message.document)
            # extract images
            extract_images_from_pdf(download, output_folder)
            process_images_in_folder(
                api_key=api_key, output_folder=images_output, input_folder=output_folder)
            # zip file
            output_zip = "pdf_images.zip"
            zip_output(output_zip, output_folder)
            # Upload the zip file to Telegram
            with open(output_zip, "rb") as zip_file:
                await client.send_document(
                    chat_id=message.chat.id,
                    document=zip_file,
                    caption="pdf_images"
                )
            os.remove(output_zip)
            output_zip = "pdf_images_text.zip"
            zip_output(output_zip, images_output)
            # Upload the zip file to Telegram
            with open(output_zip, "rb") as zip_file:
                await client.send_document(
                    chat_id=message.chat.id,
                    document=zip_file,
                    caption="pdf_images_text"
                )
            shutil.rmtree(output_folder)
            shutil.rmtree(images_output)
            os.remove(output_zip)
            os.remove(download)
            await status.delete()
        else:
            await status.edit_text('<b>`Please Provide Photos and Pdf Not file or Any Document`</b>')
    elif message.photo:
        await status.edit_text("<b>⎚ `Processing image...`</b>")
        download = await client.download_media(message.photo)
        recognized_text = ocr_image_single(
            image_path=download, api_key=api_key)
        await status.edit_text(f"{recognized_text}")
        os.remove(download)

    else:
        await status.edit_text('<b>`Please Provide Photos and Pdf Not file or Any Document`</b>')
        return


# Function to create a zip file with text files
def zip_output(zip_file_name, source_dir):
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(
                    os.path.join(root, file), source_dir))