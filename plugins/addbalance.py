from pyrogram import filters, Client
from pyrogram.types import Message
from database.utilitis import Admin
from database.controlls import balance_add


@Client.on_message(filters.user(Admin.owner_id) & filters.command(['addbalance', 'abl']))
async def addbl(bot:Client, cmd:Message):
    _, id, bl = cmd.text.split()
    if id and bl:
        data = balance_add(bot, cmd, id, bl)
        if data:
            await cmd.reply_text("Add Successfull!")
        else:
            await cmd.reply_text("User Not Found")
    else:
        await cmd.reply_text('Something Went Worng!')
