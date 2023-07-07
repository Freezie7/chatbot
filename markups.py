from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
class Markup:
    def __init__(self):
        pass
    @staticmethod
    def start_markup():
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(InlineKeyboardButton('Добавить заметку', callback_data='cb_addnote'))
        return markup