from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from parsings_info import joke_parser, weather_parser, horoscope_parser
from aiogram.dispatcher.filters import Text
from bot_help import help_for_user


class WeatherCity(StatesGroup):
    Weather = State()


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, help_for_user, reply_markup=kb_client)


async def command_joke(message: types.Message):
    try:
        if len(joke_parser.list_of_jokes) == 0:
            joke_parser.list_of_jokes = joke_parser.parser()
        await bot.send_message(message.from_user.id, joke_parser.list_of_jokes[0], reply_markup=kb_client)
        del joke_parser.list_of_jokes[0]


    except StopIteration:
        await message.answer('sorry the Jokes are over', reply_markup=kb_client)


async def command_weather(message: types.Message):
    await message.answer('Weather now entered your city', reply_markup=kb_client)
    await WeatherCity.Weather.set()

    @dp.message_handler(state=WeatherCity.Weather)
    async def weather_answer(mess: types.Message, state: FSMContext):
        answer = mess.text
        await bot.send_message(mess.from_user.id, weather_parser.get_weather(answer))
        await message.answer('Please choose either the weather now or a joke or a horoscope', reply_markup=kb_client)
        await state.finish()


async def command_horoscope(message: types.Message):
    await bot.send_message(message.from_user.id, horoscope_parser.esoteric, reply_markup=kb_client)
    await message.answer('Please choose either the weather now or a joke or a horoscope', reply_markup=kb_client)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, Text(equals=['/start', 'Help']))
    dp.register_message_handler(command_joke, Text(equals='Jokes'))
    dp.register_message_handler(command_weather, Text(equals='Weather'), state=None)
    dp.register_message_handler(command_horoscope, Text(equals='Horoscope'))
