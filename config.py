import os

API_ID = int(os.environ.get("API_ID", 25603034))
API_HASH = os.environ.get("API_HASH", "294a7bf4488b21609436de1cdd05c316")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5983400035:AAHuXglu4ch9pnS89JQObVi57aeoBVuC6sQ")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "-1001577667595")
IS_PRIVATE = os.environ.get("IS_PRIVATE", 'True') # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", '5764988016'))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', 'streaamdb')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "5791145987").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
