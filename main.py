from pyrogram import Client
from ToXic.api import start, downloader, helper
from ToXic.api.users import is_served_user, get_served_users, add_served_user
from ToXic.api.broadcast import stats, broadcast

api_id = 
api_hash = ""
bot_token = ""

app = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    plugins={"root": "ToXic.api", "users": "ToXic.users", "broadcast": "ToXic.broadcast"},
)

app.run()
