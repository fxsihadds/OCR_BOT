from pyrogram import filters, Client
from pyrogram.types import Message
import os

@Client.on_message(filters.command('srt'))
async def clean_srt(bot:Client, cmd:Message):
    if not cmd.reply_to_message.document: return await cmd.reply_text('<b>`Please Reply With SRT File`</b>')
    status = await cmd.reply_text('<b>`Cleaning...`</b>')
    download = await bot.download_media(cmd.reply_to_message.document)
    await srt_clean(bot, cmd, file=download)
    await status.delete()
    os.remove(download)




async def srt_clean(bot, cmd, file):
    with open(file=file, mode="r", encoding="utf-8") as srt:
        characters_remove = ("~@#$*<&^%$()';|{}[]şğabcdefghijklmnopqrstuvwxyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcçdefgğh"
                             "ıijklmnoprsştüuvwxyz a ā á ǎ à o ō ó ǒ ò e ē é ě è i ī í ǐ ì u ū ú ǔ ù ü ǖ ǘ ǚ ǜ b p m "
                             "f d t n l g k h j q x z c s y w अ आ इ ई उ ऊ ए ऐ ओ औ अं अः क ख ग घ च छ ज झ ट ठ ड ढ ण त थ "
                             "द ध न प फ ब भ म य र ल व श ष स हأا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي")
        trans_table = str.maketrans(characters_remove, ' ' * len(characters_remove))
        trans_remove = [line.translate(trans_table) for line in srt]

        # Remove double spaces
        trans_remove = [' '.join(line.split()) + '\n' for line in trans_remove]

    with open(file="cleaned.srt", mode="w", encoding="utf-8") as saved:
        saved.writelines(trans_remove)

    await bot.send_document(
        chat_id = cmd.chat.id,
        document = 'cleaned.srt',
        caption = 'Clean Srt File'
    )
    os.remove('cleaned.srt')
