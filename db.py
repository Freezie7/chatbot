from pathlib import Path
import sqlite3

PROJECT_ROOT = Path(__file__).parent.parent

class DB():
    def __init__(self):
        self.conn = sqlite3.connect(PROJECT_ROOT / "bot_0.5.1.db")
        self.cursor = self.conn.cursor()

    def create_users(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS USERS(id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER UNIQUE)''')
        self.conn.commit()

    def create_records(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS RECORDS(id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER REFERENCES USERS(id) ON DELETE CASCADE NOT NULL, note TEXT NOT NULL)''')
        self.conn.commit()

    def get_id(self, user_id):
        with self.conn:
            return self.cursor.execute("SELECT 'id' FROM 'USERS' WHERE 'user_id' = ?", (user_id,)).fetchone()[0]

    def add_record(self, user_id, note):
        self.cursor.execute('''INSERT INTO 'RECORDS'(user_id,note) VALUES(?, ?)''',
                            (self.get_id(user_id=user_id), note))

    def user_exists(self, user_id):
        return bool(self.cursor.execute("SELECT `id` FROM `USERS` WHERE `user_id` = ?",
                                        (user_id,)).fetchall())

    def add_user(self, user_id):
        with self.conn:
            return self.cursor.execute('''INSERT INTO 'USERS'(user_id) VALUES(?)''', (user_id,))

    def close(self):
        self.conn.close()
