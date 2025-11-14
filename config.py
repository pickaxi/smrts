from os import getenv
INST_COOKIES = """
"""
YTUB_COOKIES = """
"""
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7618349770 7336381823").split()))
MONGO_DB = getenv("MONGO_DB", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002504099057"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "5000000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "50000000"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
