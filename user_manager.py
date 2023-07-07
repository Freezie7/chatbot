from db import DB
class UserManager():
    def __init__(self):
        self.db = DB()

    def register(self, user_id):
        if self.db.user_exists(user_id) == False:
            self.db.add_user(user_id)

    def add_note(self, user_id, note):
        return self.db.add_record(user_id, note)