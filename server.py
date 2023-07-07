from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN
from markups import Markup
from user_manager import UserManager


bot = Bot(TOKEN)
manage = UserManager()
dispatcher = Dispatcher(bot)
markup = Markup()
history = []

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
        manage.register(self.from_user.id)

    @dispatcher.message_handler(commands=['help'])
    async def send_help(self: types.Message):
        text = "Добавить заметку - Создаёт новую заметку"
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
        #не забыть!

    @dispatcher.callback_query_handler(lambda call:
                                       call.data in ['cb_addnote'])
    async def handle_start(self: types.CallbackQuery):
        if self.data == 'cb_addnote':
            text = 'Введите заметку'
            await self.message.answer(text)
            history.extend(self.data)
            await  self.message.delete()

    @dispatcher.message_handler(content_types=['text'])
    async def message_handle2(self: types.Message):
        text = 'Записано!'
        if history:
            manage.add_note(self.from_user.id, history[0])
            await bot.send_message(self.from_user.id, text)
        else:
            await bot.send_message(self.from_user.id,'Попробуйте ещё раз', reply_markup=markup.start_markup())


executor.start_polling(dispatcher, skip_updates=True)