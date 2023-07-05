from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
class Markup:
    def __init__(self):
        pass
    @staticmethod
    def start_markup():
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(InlineKeyboardButton('Добавить замтеку', callback_data='cb_addnote'),
                   InlineKeyboardButton('Изменить заметку', callback_data='cb_update'),
                   InlineKeyboardButton('Удалить заметку', callback_data='cb_delnote'))
        return markup