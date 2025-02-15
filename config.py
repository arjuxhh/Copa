from os import environ
from info import is_enabled
# config.py
DATABASE_URI = "mongodb+srv://GORU:GORU@cluster0.euujugz.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = environ.get('DATABASE_NAME', "")  # Add the actual database name
COLLECTION_NAME = "Telegram_files"
USE_CAPTION_FILTER = True
IMDB = "some_value"
IMDB_TEMPLATE = "some_value"
MELCOW_NEW_USERS = True
P_TTI_SHOW_OFF = False
SINGLE_BUTTON = True
SPELL_CHECK_REPLY = True
PROTECT_CONTENT = False
