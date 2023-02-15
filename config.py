#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = "6290776967:AAGDcYFSDFkUt3s1xCJuer5NqAONHVVIdnE"

#Your API ID from my.telegram.org
APP_ID = 3845818

#Your API Hash from my.telegram.org
API_HASH = "95937bcf6bc0938f263fc7ad96959c6d"

#Your db channel Id
CHANNEL_ID = -1001860944958

#OWNER ID
OWNER_ID = 1443454117

#Port
PORT = "8080"

#Database 
DB_URI = "mongodb+srv://1080p:web@cluster0.vxqoovh.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "filesharexbot"

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = -1001799357284

TG_BOT_WORKERS = 4

#start message
START_MSG = "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link."

ADMINS = int(1863307059)

#Force sub message 
FORCE_MSG = "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>"

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = "None"

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = "True"

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = "True"

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

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
