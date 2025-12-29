import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN", "8424464965:AAGeOBkcs9pKShMCAJ92WYr8nNT6LY3OcXY")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID", -1003384645515))
LISTENER_CHAT_ID = int(os.getenv("LISTENER_CHAT_ID", -1003520534409))
DATABASE_NAME = os.getenv("DATABASE_NAME", "massive_project.db")

# Права доступа
ADMIN_IDS = [123456789]  # ID модераторов
SUPER_ADMIN_IDS = [123456789]  # ID супер-админов
