from os import environ
from info import is_enabled
# config.py
DATABASE_URI = "mongodb+srv://GORU:GORU@cluster0.euujugz.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = environ.get('DATABASE_NAME', "")  # Add the actual database name
COLLECTION_NAME = "Telegram_files"
USE_CAPTION_FILTER = True
IMDB = "some_value"
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<code>{query}</code>\n\n<b>〓〓〓 <a href={url}>{title}</a> 〓〓〓\n\n⭐️ ɪᴍᴅʙ  {rating} | ⏰ ʀᴜɴ {runtime} ᴍɪɴ |\n📆 ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ : {release_date}</b>\n\n● <code>{genres}</code>\n● <code>languages</code>\n\n📖 <b>ꜱᴛᴏʀʏ</b> : {plot}\n\n<b><i>★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ</i></b> <a href='https://t.me/moviehub_support'><b><i>ᴍᴏᴠɪᴇʜᴜʙ</i></b></a>")
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
P_TTI_SHOW_OFF = False
SINGLE_BUTTON = True
SPELL_CHECK_REPLY = True
