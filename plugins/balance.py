from pyrogram import Client, filters
from pyrogram.types import Message
from database.controlls import find_one
from datetime import datetime


@Client.on_message(filters.command(['balance', 'bl']))
async def userbalance(bot: Client, cmd: Message):
    data = find_one(bot, cmd)
    print(data)
    if data is not None:
        _id = data['_id']
        fname = data['fname']
        lname = data['lname']
        is_trial = data['is_trial']
        Status = data['Status']
        remaining = data['remaining']
        dates = datetime.fromisoformat(str(data['date']))
        message_text = f"""
🌟 **User Details** 🌟
🆔 ID: <code>{_id}</code>
👤 First Name: {fname}
👥 Last Name: {lname}
⏳ Is Trial: {is_trial}
🔰 Status: Active
💰 Remaining: {remaining}
📅 Join Date: {dates}
"""
        await cmd.reply_text(text=message_text)
    else:
        await cmd.reply_text("I Couldn't find any Information About You!")
