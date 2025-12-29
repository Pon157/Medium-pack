import sqlite3
import logging
from datetime import datetime
from typing import Optional, List, Dict, Tuple

class Database:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.init_db()
    
    def init_db(self):
        """Инициализация всех таблиц"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Пользователи
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    gender TEXT DEFAULT 'not_specified',
                    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    warnings INTEGER DEFAULT 0,
                    is_banned BOOLEAN DEFAULT FALSE,
                    ban_until TIMESTAMP,
                    rating_count INTEGER DEFAULT 0,
                    rating_total INTEGER DEFAULT 0
                )
            ''')
            
            # Администраторы/Слушатели
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS listeners (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    name TEXT,
                    gender TEXT,
                    age INTEGER,
                    experience TEXT,
                    examples TEXT,
                    is_active BOOLEAN DEFAULT TRUE,
                    is_online BOOLEAN DEFAULT FALSE,
                    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    rating_count INTEGER DEFAULT 0,
                    rating_total INTEGER DEFAULT 0,
                    topics_handled INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    on_break BOOLEAN DEFAULT FALSE
                )
            ''')
            
            # Активные чаты
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS active_chats (
                    chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    listener_id INTEGER,
                    topic_message_id INTEGER,
                    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    ended_at TIMESTAMP,
                    user_rating INTEGER,
                    user_feedback TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (user_id),
                    FOREIGN KEY (listener_id) REFERENCES listeners (user_id)
                )
            ''')
            
            # Заявки на поддержку
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS support_requests (
                    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    listener_id INTEGER,
                    gender_preference TEXT,
                    status TEXT DEFAULT 'pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    taken_at TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (user_id),
                    FOREIGN KEY (listener_id) REFERENCES listeners (user_id)
                )
            ''')
            
            # Заявки на админа
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS admin_applications (
                    application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    age INTEGER,
                    experience TEXT,
                    examples TEXT,
                    status TEXT DEFAULT 'pending',
                    reviewed_by INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            ''')
            
            conn.commit()
    
    # ... остальные методы для работы с БД
