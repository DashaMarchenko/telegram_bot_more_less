from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os
import aiofiles


number = 100
count_of_attempts = 1

bot = Bot('5869243777:AAGsU9hFjeW2HUtfxsYq5WEaP7Vd8Fkj4FQ')
dp = Dispatcher(bot)

users = dict()


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    global count_of_attempts

    if str(message.from_user.id) not in users.keys():
        users[str(message.from_user.id)] = message.from_user.full_name

        async with aiofiles.open('users_data.txt', 'w+') as users_file:
            for ID, username in users.items():
                await users_file.write(f'ID: {ID} | Username: {username}')

    if count_of_attempts == 1:
        await message.answer(f'Привет, я загадал число, попробуй отгадать')

    else:
        await message.answer(f'Введите число: ')


@dp.message_handler()
async def info(message: types.Message):
    global number, count_of_attempts

    try:
        if int(message.text) == number:
            await message.answer(f'Вы угадали! \nКоличество попыток: {count_of_attempts}')

        elif int(message.text) < number:
            await message.answer(f'Число должно быть больше')
            count_of_attempts += 1
            await start_message(message)

        else:
            await message.answer(f'Число должно быть меньше')
            count_of_attempts += 1
            await start_message(message)

    except ValueError:
        await message.answer('Ошибка! | Данные должны иметь числовой тип')
        await start_message(message)


if __name__ == '__main__':
    print('bot polling start')
    executor.start_polling(dp, skip_updates=True)