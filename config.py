## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgB-EibFtEFW20fe9w2YR0wBbfrZYIGJWHA5NL74NiSAXO5xTdTMnJHFGukHCFTt-68WzGP9VkYMu9tMW_qhM1vaEQ4TC0jYIzVWB5FF3wP3P2SOgn57obB0QplbHlh_v7LMhMZVVJDGfHbPAmkJAbgoJmxecLK0i0FSmVThBew8eVqFXBQWxe8sfRllq2yMiXWIHop2xk8svs8ukNkqAzNSS_UQomGLYXTm4NHGua7DhCG1I1bzwC9MovLSqQRrymILQpfTRBaOZ_uUr9xwjTpZ-uCyxmnpvI7G5kEUAJQHe4D0cjilgZkh0UOOUL69-qrKM6uGoxZoNJTN78RoNiOpAAAAASxokk8A
")
BOT_TOKEN = getenv("BOT_TOKEN", "5337470376:AAFw7gHP0nWB3czRNiUgA1kthgBw_4itv-g")
BOT_NAME = getenv("BOT_NAME", "𝑺𝒂𝒏𝒂𝒂 𝑴𝒖𝒔𝒊𝒄 ♪")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "ƁƠƳƘƛ┋𝑇𝑀")
OWNER_USERNAME = getenv("OWNER_USERNAME", "BOYKA_50")
ALIVE_NAME = getenv("ALIVE_NAME", "ƁƠƳƘƛ┋𝑇𝑀")
BOT_USERNAME = getenv("BOT_USERNAME", "HYJJp_bot")
OWNER_ID = getenv("OWNER_ID", "2139870419")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "w_b_ml")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TeaMember")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "S6222_50")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2139870419").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
