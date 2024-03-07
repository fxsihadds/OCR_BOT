from pyrogram import Client, filters
from pyrogram.types import Message
import os
from exefile.helpers_ocr import sub_images



@Client.on_message(filters.command('vocr'))
async def video_ocr(bot:Client, cmd:Message):
    ocr_images_store = 'ocrdict'
    status = await cmd.reply_text('Hardsub Extracting...')
    if cmd.reply_to_message:
        if cmd.reply_to_message.video and cmd.reply_to_message.video.file_name.endswith(('mp4', 'mkv')):
            download = await bot.download_media(cmd.reply_to_message.video)
            await sub_images(bot, status,video_path=download, tmp_dir=ocr_images_store)
            os.remove(download)
        elif cmd.reply_to_message.document and cmd.reply_to_message.document.file_name.endswith(('mp4', 'mkv')):
            download = await bot.download_media(cmd.reply_to_message.document)
            os.remove(download)
            await sub_images(bot, status,video_path=download, tmp_dir=ocr_images_store)
        else:
            await status.edit_text('Please Reply With Mp4 and Mkv Other format Not Support at this moment')
            return
    else:
        await status.edit_text('Please reply with hardsub Video!')
        return
