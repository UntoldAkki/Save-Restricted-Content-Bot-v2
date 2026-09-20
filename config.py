# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "26750159"))
API_HASH = getenv("API_HASH", "fd147a9808d7a294a4864e28a8cea47d")
BOT_TOKEN = getenv("BOT_TOKEN", "8272927957:AAECz87ud2xm4biLKVIUAyRQ6RnGtHBHWdU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7778185746").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://akkiraw_db_user:ca0dOXtD2ibEwQy3@cluster0.kwcj0zx.mongodb.net/?appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1003369488985")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002272912029"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
