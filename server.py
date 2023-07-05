from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN
from markups import Markup


bot = Bot(TOKEN)
dispatcher = Dispatcher(bot)
markup = Markup()

class Server():
    def __init__(self):
        self.answer = None
        self.from_user = None
        self.data = None
        self.message = None
        self.text = None

    @dispatcher.message_handler(commands=['start'])
    async def send_welcome(self: types.Message):
        text = f"Привет,{self.from_user.first_name}!\n"\
                f"Вас приветствует <b>Бот для заметок</b>!"
        await bot.send_message(
            self.from_user.id,
            text=text,
            parse_mode='html', reply_markup=markup.start_markup())

    @dispatcher.message_handler(commands=['help'])
    async def send_help(self: types.Message):
        text = "Добавить заметку - Создаёт новую заметку \n" \
               "Изменить заметку - Редактирует выбранную заметку \n" \
               "Удалить заметку - Удаляет выбранную заметку"
        await bot.send_message(
            self.from_user.id,
            text=text,
            parse_mode='html')

    @dispatcher.message_handler(commands=['delete'])
    async def send_del(self: types.Message):
        text = "Успешно удалено!"
        await bot.send_message(
            self.from_user.id,
            text=text)

    @dispatcher.callback_query_handler(lambda call:
                                       call.data in ['cb_addnote', 'cb_update', 'cb_delnote'])
    async def handle_start(self: types.CallbackQuery):
        if self.data == 'cb_addnote':
            text='Добавить заметку'
            await self.message.answer(text)
            await self.message.delete()
        elif self.data == 'cb_update':
            text = 'Изменить заметку'
            await self.message.answer(text)
            await self.message.delete()
        elif self.data == 'cb_delnote':
            text = 'Удалить заметку'
            await self.message.answer(text)
            await  self.message.delete()


executor.start_polling(dispatcher, skip_updates=True)