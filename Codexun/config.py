## Disclaimer By Team Codexun

## Don't try to edit this file otherwise your bot will be crash.

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAxBtgYIuA-xxEWfvKxRyY4zrHglQozA5_7h5YQgYH8eCgmzm1p43gaWIHFP51Lom_CX1PRGkcRquuBoTdi7heHPZfJ-RfF36QdyBa9Icqs-9ydLA-HecU-5ma90Nd4FG76f30jMA6xCUIdZ_gaQYErGVLJlp0YrSCZlKx_QH21prqOQj25VYM4EuLSSRKN9OZ6MnO2S72UTqDmOSiKENcbUv0NwCZhjJSwrY1ftFq8mOe7NS0-2JV62NSZlf_rkzgPZK3FR88bLuDbSb0PKoiobaWC1_sTx038sy3RxQgp0P5Dgx5ibSDLFOT4SadwRH3rDI-4xhsXK-0-liSxCaDCAAAAATCfhggA")
BOT_TOKEN = getenv("BOT_TOKEN", "5181191526:AAEf763hXLvfer-CXWl9MzSb7UHQApYQVbU")
BOT_NAME = getenv("BOT_NAME", "Resso Music")
BOT_USERNAME = getenv("BOT_USERNAME", "Ressomusicbot")
ASSID = int(getenv("ASSID", "5110728200"))
ASSNAME = getenv("ASSNAME", "Resso Assistant")
ASSUSERNAME = getenv("ASSUSERNAME", "BrokenMusicAs")
BOT_ID = int(getenv("BOT_ID", "5181191526"))
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/PavanMagar/CodexunMusicBot")
USERS = getenv("2056407064")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://unreal:unreal@cluster0.cdl1j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
API_ID = int(getenv("API_ID", "10098309"))
API_HASH = getenv("API_HASH", "aaacac243dddc9f0433c89cab8efe323")
OWNER_ID = int(getenv("OWNER_ID", "2056407064"))
UPDATE = getenv("UPDATE", "Codexun")
SUPPORT = getenv("SUPPORT", "TeamCodexun")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/e594d98181c2f54b872fd.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/f2a2d31f60a9e0f3dbe94.png")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2056407064").split()))
ASSISTANT_NAME = getenv("ASSNAME", "Resso")
COMMAND_PREFIXES = ("/ ! .").split()
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a085a3cea21f994264152.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
