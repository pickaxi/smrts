from os import getenv
INST_COOKIES = """
"""
YTUB_COOKIES = """
"""
API_ID = int(getenv("API_ID", "25880697"))
API_HASH = getenv("API_HASH", "ccbeeaf507caf64c00ec327407faa7a2")
BOT_TOKEN = getenv("BOT_TOKEN", "8353168774:AAHZc0Po_ckCwI0JtOvYjkQGFOLq_rYTOpg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7618349770 7336381823").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://fixmayart834:FMWwXBd4JJYMs2Iv@cluster0.ltpube9.mongodb.net/?retryWrites=true&w=majority")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002504099057"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
