from pyrogram import filters, Client
from pyrogram.types import Message
from database.controlls import add_user
"""
    await cmd.reply_text(
                     "🔍 Welcome to our OCR (Optical Character Recognition) Bot! Need help extracting text from images or PDF files? Just send them our way! For a smoother experience, here are a few hints:\n"
                     '1. Ensure your image/PDF is clear and well-lit for best results.\n'
                     '2. Capture text in a single, focused shot for optimal recognition.\n'
                     '3. Simple backgrounds and fonts improve accuracy.\n'
                     '4. Send individual PDF pages for precise extraction.\n'
                     '5. Send one file at a time for efficient processing.\n'
                     "Ready to begin! Share your files, and we'll do the rest.")
"""

@Client.on_message(filters.command(['start', 'help']))
async def start_cmd(bot: Client, cmd: Message):
    add_user(bot, cmd)
    await cmd.reply_text("🔍 𝘞𝘦𝘭𝘤𝘰𝘮𝘦 𝘵𝘰 𝘰𝘶𝘳 𝘖𝘊𝘙 (𝘖𝘱𝘵𝘪𝘤𝘢𝘭 𝘊𝘩𝘢𝘳𝘢𝘤𝘵𝘦𝘳 𝘙𝘦𝘤𝘰𝘨𝘯𝘪𝘵𝘪𝘰𝘯) 𝘉𝘰𝘵! 𝘕𝘦𝘦𝘥 𝘩𝘦𝘭𝘱 𝘦𝘹𝘵𝘳𝘢𝘤𝘵𝘪𝘯𝘨 𝘵𝘦𝘹𝘵 𝘧𝘳𝘰𝘮 𝘪𝘮𝘢𝘨𝘦𝘴 𝘰𝘳 𝘗𝘋𝘍 𝘧𝘪𝘭𝘦𝘴? 𝘑𝘶𝘴𝘵 𝘴𝘦𝘯𝘥 𝘵𝘩𝘦𝘮 𝘰𝘶𝘳 𝘸𝘢𝘺! 𝘍𝘰𝘳 𝘢 𝘴𝘮𝘰𝘰𝘵𝘩𝘦𝘳 𝘦𝘹𝘱𝘦𝘳𝘪𝘦𝘯𝘤𝘦, 𝘩𝘦𝘳𝘦 𝘢𝘳𝘦 𝘢 𝘧𝘦𝘸 𝘩𝘪𝘯𝘵𝘴:\n"
                         '1. 𝘌𝘯𝘴𝘶𝘳𝘦 𝘺𝘰𝘶𝘳 𝘪𝘮𝘢𝘨𝘦/𝘗𝘋𝘍 𝘪𝘴 𝘤𝘭𝘦𝘢𝘳 𝘢𝘯𝘥 𝘸𝘦𝘭𝘭-𝘭𝘪𝘵 𝘧𝘰𝘳 𝘣𝘦𝘴𝘵 𝘳𝘦𝘴𝘶𝘭𝘵𝘴.\n'
                         '2. 𝘊𝘢𝘱𝘵𝘶𝘳𝘦 𝘵𝘦𝘹𝘵 𝘪𝘯 𝘢 𝘴𝘪𝘯𝘨𝘭𝘦, 𝘧𝘰𝘤𝘶𝘴𝘦𝘥 𝘴𝘩𝘰𝘵 𝘧𝘰𝘳 𝘰𝘱𝘵𝘪𝘮𝘢𝘭 𝘳𝘦𝘤𝘰𝘨𝘯𝘪𝘵𝘪𝘰𝘯.\n'
                         '3. 𝘚𝘪𝘮𝘱𝘭𝘦 𝘣𝘢𝘤𝘬𝘨𝘳𝘰𝘶𝘯𝘥𝘴 𝘢𝘯𝘥 𝘧𝘰𝘯𝘵𝘴 𝘪𝘮𝘱𝘳𝘰𝘷𝘦 𝘢𝘤𝘤𝘶𝘳𝘢𝘤𝘺.\n'
                         '4. 𝘚𝘦𝘯𝘥 𝘪𝘯𝘥𝘪𝘷𝘪𝘥𝘶𝘢𝘭 𝘗𝘋𝘍 𝘱𝘢𝘨𝘦𝘴 𝘧𝘰𝘳 𝘱𝘳𝘦𝘤𝘪𝘴𝘦 𝘦𝘹𝘵𝘳𝘢𝘤𝘵𝘪𝘰𝘯.\n'
                         '5. 𝘚𝘦𝘯𝘥 𝘰𝘯𝘦 𝘧𝘪𝘭𝘦 𝘢𝘵 𝘢 𝘵𝘪𝘮𝘦 𝘧𝘰𝘳 𝘦𝘧𝘧𝘪𝘤𝘪𝘦𝘯𝘵 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨.\n'
                         "𝘙𝘦𝘢𝘥𝘺 𝘵𝘰 𝘣𝘦𝘨𝘪𝘯! 𝘚𝘩𝘢𝘳𝘦 𝘺𝘰𝘶𝘳 𝘧𝘪𝘭𝘦𝘴, 𝘢𝘯𝘥 𝘸𝘦'𝘭𝘭 𝘥𝘰 𝘵𝘩𝘦 𝘳𝘦𝘴𝘵."

                         )
