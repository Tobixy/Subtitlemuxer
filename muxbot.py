import os
import logging
import pyrogram

if os.path.exists('testconfig.py'):
    from testconfig import Config
else:
    from config import Config

from func.dbhelper import Database as Db

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(message)s - %(levelname)s")
logger = logging.getLogger(__name__)

db = Db().setup()

if not os.path.isdir(Config.DOWNLOAD_DIR):
    os.mkdir(Config.DOWNLOAD_DIR)

plugins = dict(root='plugins')

app = pyrogram.Client(
    'Subtitle Muxer',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    plugins=plugins
)
app.run()
