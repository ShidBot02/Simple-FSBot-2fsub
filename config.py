#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6750822148:AAHkqRrXxVRklrJKgasQAlp8-M4ZTygw5Io")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22980101"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f598fb9457146cc0e7c3b50e4e232d4f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002065786368"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1536699044"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://animecircle:acfilestore1@cluster0.kspizla.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001280711408"))
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001594571768"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start pic
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/d48e6d30e443dcae118b8.jpg")

#start message
START_MSG = os.environ.get("START_MSG", "<b>Hᴇʟʟᴏ, {first} ~\n\n  I am a Telegram Bot that store posts or files for <a href='https://t.me/Animemoviesr'>infinity void ∞</a> , And can be accessed via a Special Link.\n\n👨‍💻 Developed by @Shidoteshika1</b>")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5480790404").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "⚠️ Hey {mention} !\n\n<b>You need to join in my Channels to use me\n\nKindly Join below Channels</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>I am only file store bot\n\nFor More Info Click: /start</b>\n"
HELP_TEXT = """<b>Hello User,

I am a simple file supplier bot that can only store files for a specific channel. You need to join below channels to use me properly.

1. Anime Channel: <a href= 'https://t.me/Animemoviesr'>infinity void ∞</a>
2. Ongoing Channel: <a href= 'https://t.me/Infinity_Ongoing'>∞ ongoing</a></b>

<b>/help</b> - Only this command you can use without joining any channel.

<b>For Contact Admins, Click Below:</b>"""

BOT_CMD = """<b>❏ Cᴏᴍᴍᴀɴᴅs ғᴏʀ ʙᴏᴛ Aᴅᴍɪɴs

‣ /start :</b> start the bot or get posts
<b>‣ /batch :</b> create group messages
<b>‣ /genlink :</b> create link for one post
<b>‣ /users :</b> view bot statistics
<b>‣ /broadcast :</b> broadcast Message
<b>‣ /stats :</b> checking your bot uptime"""



ADMINS.append(OWNER_ID)
ADMINS.append(1536699044)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
