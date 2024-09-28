from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import dotenv_values
import requests

ENV = dotenv_values(".env")
BOT_TOKEN = str(ENV["RUTUBE_HELPER_BOT_TOKEN"])

# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        "Здравствуйте!\nВас приветсвует бот помщник платформы RUTUBE.\n"
        "Если у Вас есть вопросы, буду рад Вам помочь.\n\n"
        "Отправьте команду /help, чтобы получить дополнительную информацию о боте."
    )


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(
        f"Дополнительная информация\n"
        f"/stat - посмотреть статистику\n\n"
    )


# Этот хэндлер будет срабатывать на команду "/stat"
@dp.message(Command(commands="stat"))
async def process_help_command(message: Message):
    await message.answer(
        f"Дополнительная статистика работы бота.\n"
    )


# Этот хэндлер будет обрабатывать остальные сообщения как запросы к помощнику
@dp.message()
async def process_other_answers(message: Message):
    # обращаемся к API раг системы
    url = 'http://localhost:8000/predict'
    data = {'question': message.text}
    results = requests.post(url=url, json=data)
    results = results.json()
    #{"answer":"API_CALL()","class_1":"42", "class_2":"7"}
    # возвращаем ответ пользователю
    await message.answer(        
        f"{results["answer"]}, "
        f"class 1: {results["class_1"]}, "
        f"class 2: {results["class_2"]}"
    )


if __name__ == "__main__":
    dp.run_polling(bot)