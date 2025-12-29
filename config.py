import os

# Приоритет переменной из .env (как вы просили), иначе хардкод
TOKEN = os.getenv("BOT_TOKEN", "8424464965:AAGeOBkcs9pKShMCAJ92WYr8nNT6LY3OcXY")
ADMIN_CHAT_ID = -1003384645515
LISTENER_CHAT_ID = -1003520534409
DB_NAME = "massive_project.db"
