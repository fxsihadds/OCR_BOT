from pyrogram import Client, filters
from pyrogram.types import Message
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')


bot = Client(
    'OCR',
    api_id=config['PYROGRAM']['API_ID'],
    api_hash=config['PYROGRAM']['API_HASH'],
    bot_token=config['PYROGRAM']['BOT_TOKEN'],
    plugins=dict(root='plugins')
)

print('BOT ALIVE')
bot.run()
