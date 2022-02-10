from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from main import parse

bot = Bot(token='5177734052:AAFunhDkKmX9jQicDugPcTO1E2J80c31S5Q')
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def start(message: types.Message):
    await message.answer('Введи ФИО человека')


@dp.message_handler()
async def echo_message(msg: types.Message):
    try:
        await bot.send_message(msg.from_user.id, parse(msg.text))
    except:
        await msg.answer('ахахахахахахаххаха ищи себя')


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
