from pathlib import Path
import sqlite3

PROJECT_ROOT = Path(__file__).parent.parent
class DB():
    def __init__(self):
        self.conn = sqlite3.connect(PROJECT_ROOT / "account.db")
        self.cursor = self.conn.cursor()
    def create(self):
        self.cursor.executescript("CREATE TABLE IF NOT EXISTS USERS(id int primary key check(id > 0), user_id int check(user_ic > 0) unique, date datetime")
        self.conn.commit()
        self.cursor.executescript("CREATE TABLE IF NOT EXISTS RECORDS(id int primary key check(id > 0), user_id int check(user_ic > 0) unique, date datetime")
        self.conn.commit()
        self.conn.close()

db = DB()
db.create()