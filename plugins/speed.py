import os
import sys, time
from speedtest import Speedtest, ConfigRetrievalError
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from datetime import datetime
from database.utilitis import Admin
#=====================================================
@Client.on_message(filters.user(Admin.owner_id) & filters.command('speedtest'))
async def speedtest(client, message):
    msg = await message.reply_text("`Speedtest...`")
    try:
        speed = Speedtest()
    except ConfigRetrievalError:
        await msg.edit("Can't connect to Server at the Moment, Try Again Later !")
        return
    speed.get_best_server()
    speed.download()
    speed.upload()
    speed.results.share()
    result = speed.results.dict()
    photo = result['share']
    text = f'''
➲ <b>SPEEDTEST INFO</b>
┠ <b>Upload:</b> <code>{get_size(result['upload'])}/s</code>
┠ <b>Download:</b>  <code>{get_size(result['download'])}/s</code>
┠ <b>Ping:</b> <code>{result['ping']} ms</code>
┠ <b>Time:</b> <code>{datetime.strptime(result['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")}</code>
┠ <b>Data Sent:</b> <code>{get_size(int(result['bytes_sent']))}</code>
┖ <b>Data Received:</b> <code>{get_size(int(result['bytes_received']))}</code>

➲ <b>SPEEDTEST SERVER</b>
┠ <b>Name:</b> <code>{result['server']['name']}</code>
┠ <b>Country:</b> <code>{result['server']['country']}, {result['server']['cc']}</code>
┠ <b>Sponsor:</b> <code>{result['server']['sponsor']}</code>
┠ <b>Latency:</b> <code>{result['server']['latency']}</code>
┠ <b>Latitude:</b> <code>{result['server']['lat']}</code>
┖ <b>Longitude:</b> <code>{result['server']['lon']}</code>

➲ <b>CLIENT DETAILS</b>
┠ <b>IP Address:</b> <code>{result['client']['ip']}</code>
┠ <b>Latitude:</b> <code>{result['client']['lat']}</code>
┠ <b>Longitude:</b> <code>{result['client']['lon']}</code>
┠ <b>Country:</b> <code>{result['client']['country']}</code>
┠ <b>ISP:</b> <code>{result['client']['isp']}</code>
┖ <b>ISP Rating:</b> <code>{result['client']['isprating']}</code>
'''
    await message.reply_photo(photo=photo, caption=text)
    await msg.delete()


def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

@Client.on_message(filters.command('restart') & filters.user(555994473))
async def restart(bot: Client, cmd: Message):
    """with open('restart.txt', 'w+') as restart:
        restart.write(f'{msg.chat.id}\n{msg.id}')"""
    msg = await cmd.reply("<b>⎚ `Restarting...`</b>")
    time.sleep(2)
    await msg.edit_text("<b>`✅️ Successfully Bot Restarted`</b>")
    os.execl(sys.executable, sys.executable, 'main.py')
