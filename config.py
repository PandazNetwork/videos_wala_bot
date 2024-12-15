import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7967067742:AAFcBgB94Kb607JcrdVm1STbp98xtHHmMRU")
APP_ID = int(os.environ.get("APP_ID", "27247089"))
API_HASH = os.environ.get("API_HASH", "2456e376e82f580ea1d1ed9d6444df8f")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002336908318"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7733263597"))

# Port
PORT = os.environ.get("PORT", "80")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://gihabi8558:IfnVcGxDbkzA3DOo@terbogram.xyrm1.mongodb.net/?retryWrites=true&w=majority&appName=terbogram")
DB_NAME = os.environ.get("DATABASE_NAME", "Videowalbot")

# Token variables
SHORTLINK_URL1 = os.environ.get("SHORTLINK_URL1", "pandaznetwork.com")
SHORTLINK_API1 = os.environ.get("SHORTLINK_API1", "5f82d8793633efb1268e8a4d3e7b4911e217d20a")
SHORTLINK_URL2 = os.environ.get("SHORTLINK_URL2", "pandaznetwork.com")
SHORTLINK_API2 = os.environ.get("SHORTLINK_API2", "5f82d8793633efb1268e8a4d3e7b4911e217d20a")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 28800))
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://youtu.be/EGpBKQjqXko")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002295749037"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002407134876"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "3000"))

START_MSG = os.environ.get("START_MESSAGE", "<b>👋 Hello {first}\n\nI am file sharing Bot \nI can Provide You Video Files For You \nEnjoy Watching Video 😁👻📂💀</b> ")


#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\nɪ ᴀᴍ ᴀ ᴠɪᴅᴇᴏ ᴘʀᴏᴠɪᴅᴇʀ ʙᴏᴛ. ɢᴇᴛ ᴠɪᴅᴇᴏs ᴘʀɪᴠᴀᴛᴇ ʟɪɴᴋs ғʀᴏᴍ » @instagram_viral_links_2</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "670513835 6979119858 6245748322 5614632454 849118795").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We @instagram_viral_links_2 or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", False) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(7733263597)

LOG_FILE_NAME = "logs.txt"

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
