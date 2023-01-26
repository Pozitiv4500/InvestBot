from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import TOKEN
from PriceAndDeltaPrice import price_now
import json
from PriceAndDeltaPrice import STOCK_delta_price1
from PriceAndDeltaPrice import STOCK_delta_price2
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, executor, Bot
from aiogram import types
import asyncio
import logging
from RefactorOfParserDiv import DIVI
from Inforamation import my_self_sort

class UserState(StatesGroup):
    name = State()
    address = State()
class UserState4(StatesGroup):
    ticker = State()
    kol_vo = State()
    price = State()
    commision = State()

class UserState1(StatesGroup):
    name = State()
    address = State()
class UserState2(StatesGroup):
    name = State()
    address = State()

class UserState6(StatesGroup):
        name = State()
        address = State()



storage = MemoryStorage()


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp = Dispatcher(bot, storage=storage)
kb = [
        [
            types.KeyboardButton(text="Актуальная цена"),
            types.KeyboardButton(text="Дивиденды")],
           [types.KeyboardButton(text="Уведомление об акции"),
            #types.KeyboardButton(text="Доходность")
            types.KeyboardButton(text="В Портфель"),
            types.KeyboardButton(text="Помощь")
        ],
    ]
keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=""
    )
portfolio1 = [
        [
            types.KeyboardButton(text="В главное меню"),
            types.KeyboardButton(text="Добавить акции"),
            types.KeyboardButton(text="Удалить акции")],
            [types.KeyboardButton(text="Показать портфель"),

            types.KeyboardButton(text="Помощь")

        ],
    ]
portfolio = types.ReplyKeyboardMarkup(
        keyboard=portfolio1,
        resize_keyboard=True,
        input_field_placeholder=""
    )
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):


    await message.reply("Привет, это бот с инструментами для помощи в торговле на бирже.\n" 
'Выбери функцию в меню или нажми "<b>Помощь</b>"', reply_markup=keyboard,parse_mode="html")


async def background_on_start(l,m) -> None:
    a = True
    c = l.split()
    try:
        d = c[0]
        p = c[1]
    except:
        a = False

    if price_now(d) == 'Неверно введён тикер акции':
        await bot.send_message(m, 'Неверно указан тикер акции или цена уведомления')
        a = False



    else:
        if p > price_now(d):

          await bot.send_message(m, 'Когда цена ' + d + " повыситься до " + p + ' вам придёт сообщение от бота')
          await bot.send_message(m, 'В данный момент цена '+d+" составляет "+price_now(d))
          while a == True:
             await asyncio.sleep(5)

             if STOCK_delta_price1(l) == True:
                await bot.send_message(m, '<b>Цена '+d+' повысилась до '+p+"</b>",parse_mode="html")
                a = False
        else:
            await bot.send_message(m, 'Когда цена ' + d + " снизиться до " + p + ' вам придёт сообщение от бота')
            await bot.send_message(m, 'В данный момент цена ' + d + " составляет " + price_now(d))
            while a == True:
                await asyncio.sleep(5)

                if STOCK_delta_price2(l) == True:
                    await bot.send_message(m, '<b>Цена ' + d + ' снизилась до ' + p + "</b>",parse_mode="html")
                    a = False

@dp.message_handler(lambda message: message.text == "В Портфель")
async def user_register(message: types.Message):
    await message.answer("Добро пожаловать в ваш портфель",reply_markup=portfolio)

@dp.message_handler(lambda message: message.text == "В главное меню")
async def user_register(message: types.Message):
    await message.answer("Добро пожаловать в главное меню",reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Актуальная цена")
async def user_register(message: types.Message):
    await message.answer("Введите биржевой тикер акции")
    await UserState.name.set()
@dp.message_handler(state=UserState.name)
async def echo_message(msg: types.Message, state: FSMContext):
    if price_now(msg.text) == 'Неверно введён тикер акции':
        await bot.send_message(msg.from_user.id,'Неверно введён тикер акции! Возвращаю вас в меню')
    else:
        await bot.send_message(msg.from_user.id,price_now(msg.text) + ' RUB')

    await state.finish()

@dp.message_handler(lambda message: message.text == 'Дивиденды')
async def user_register(message: types.Message):
    await message.answer("Введите биржевой тикер акции")
    await UserState2.name.set()
@dp.message_handler(state=UserState2.name)
async def echo_message(msg: types.Message, state: FSMContext):
    await bot.send_message(msg.from_user.id,DIVI(msg.text), parse_mode="html")
    await state.finish()

@dp.message_handler(lambda message: message.text == "Уведомление об акции")
async def user_register(message: types.Message):
    await message.answer("Введите биржевой тикер акции и цену о которой вас уведомить(цену введите через точку)")
    await message.answer("Пример: SBER 133.71")
    await UserState1.name.set()
@dp.message_handler(state=UserState1.name)
async def echo_message(msg: types.Message, state: FSMContext):
    l = msg.text
    m = msg.from_user.id
    if l.find(",") != -1:
        await msg.answer("Цена должна быть написана через запятую! Возвращаю вас в меню")
        await state.finish()
    else:
         asyncio.create_task(background_on_start(l, m))
         await state.finish()
@dp.message_handler(lambda message: message.text == "Добавить акции")
async def user_register(message: types.Message):
    await message.answer("Введите тикер акции")
    await UserState4.ticker.set()


@dp.message_handler(state=UserState4.ticker)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(ticker=message.text)

    data = await state.get_data()
    if price_now(data['ticker']) ==  'Неверно введён тикер акции':
        await message.answer("Неверно введён тикер акции, Возвращаю вас в меню")
        await state.finish()

    else:
        await message.answer("Отлично! Введите количество приобретаемых акций (не лотов).")
        await UserState4.next()  # либо же UserState.adress.set()


@dp.message_handler(state=UserState4.kol_vo)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(kol_vo=message.text)

    data = await state.get_data()
    try:
        nothing = int(data['kol_vo'])

        if data['kol_vo']== 0:
            await message.answer("Количество не может быть равна 0! Возвращаю вас в меню")
            await state.finish()
        else:
            await message.answer("Отлично! Введите цену покупки за шт.Пример: 130.3")
            await UserState4.next()
    except:
        await message.answer("Количество должно быть целым числом! Возвращаю вас в меню")
        await state.finish()


@dp.message_handler(state=UserState4.price)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)

    data = await state.get_data()
    try:
        nothing = float(data['price'])
        if float(data['price']) <= 0:
            await message.answer("Цена не может быть отрицательным числом!Возвращаю вас в меню")
            await state.finish()
        else:
          await message.answer("Отлично! Введите комиссию за покупку (в процентах от сделки, например: 0.3)")
          await UserState4.next()
    except:
        await message.answer("Цена должна быть положительным числом,написанным через точку! Возвращаю вас в меню")
        await state.finish()

    #await state.finish()


@dp.message_handler(state=UserState4.commision)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(commision=message.text)
    data = await state.get_data()
    try:
        nothing = float(data['price'])
        if data['price']== 0:
            await message.answer("Коммиссия не может быть равна 0! Возвращаю вас в меню")
            await state.finish()
        else:

            await message.answer('Акция успешно добавлена в ваш портфель')





            with open('USERS_INFO.json', encoding='utf8') as f:
                file = json.load(f)

                new_data = {

                            "ticker": data["ticker"].upper(),
                            "kol_vo": data['kol_vo'],
                            "price": data['price'],
                            "commision": data['commision'],


                }
                big_new_data = { message.from_user.id : [{

                            "ticker":data["ticker"].upper(),
                            "kol_vo": data['kol_vo'],
                            "price": data['price'],
                            "commision": data['commision'],

                }
                ]
                }
                for j in range(0, 100):
                    try:
                        l = file['USERS'][j][str(message.from_user.id)]
                        right = j
                        break
                    except:
                        pass

                try:
                        file['USERS'][right][str(message.from_user.id)].append(new_data)
                except:
                        file['USERS'].append(big_new_data)
                with open('USERS_INFO.json', 'w', encoding='utf8') as outfile:
                    json.dump(file, outfile,ensure_ascii=False, indent=2)
            await state.finish()
    except:
        await message.answer("Коммисиия должна быть положительным числом,написанным через точку! Возвращаю вас в меню")
        await state.finish()
@dp.message_handler(lambda message: message.text == 'Показать портфель')
async def user_register(message: types.Message):
    d=message.from_user.id
    with open('USERS_INFO.json', encoding='utf8') as f:
        file = json.load(f)
        if my_self_sort(file,d) == "Ваш портфель пока пуст":
            await message.answer("Ваш портфель пока пуст" , parse_mode="html")
        else:
            await message.answer("Ваш портфель:"+"\n"+'\n'+my_self_sort(file,d), parse_mode="html")

@dp.message_handler(lambda message: message.text == 'Удалить акции')
async def user_register(message: types.Message):
    await message.answer("Введите тикер акции, которую хотите удалить из портфеля")
    await UserState6.name.set()
@dp.message_handler(state=UserState6.name)
async def echo_message(msg: types.Message, state: FSMContext):
    d = msg.from_user.id
    with open('USERS_INFO.json', encoding='utf8') as f:
        file = json.load(f)
        if my_self_sort(file, d) == "Ваш портфель пока пуст":
            await msg.answer("Ваш портфель пока пуст", parse_mode="html")
        else:
            for i in range(0, 100):
                try:
                    l = file['USERS'][i][str(msg.from_user.id)]
                    right = i
                    break
                except:
                    pass
            for i in file['USERS'][right][str(msg.from_user.id)]:
             try:
                if i['ticker'] == msg.text.upper():
                    del i['ticker']
                    del i['kol_vo']
                    del i['price']
                    del i['commision']


             except:
                 pass



            with open('USERS_INFO.json', 'w', encoding='utf-8') as outfile:
                json.dump(file, outfile, ensure_ascii=False, indent=2)
            await msg.answer("Акции данной компании были успешно удалены из вашего портфеля", parse_mode="html")
    await state.finish()
@dp.message_handler(lambda message: message.text == 'Помощь')
async def user_register(message: types.Message):
    await message.answer("Здравствуйте, это телеграмм бот с инструментами для помощи в торгах на бирже.\n"
                         'Бот может:\n'
                         ' 🔸 Команда: "<b>Актуальная цена</b>" - выводит актуальную цену акции;\n'
                         ' 🔸 Команда: "<b>Дивиденды</b>" - выводит дивиденды комании прошедшие и ближайшие, привилегированные и непривилегированные;\n'
                         ' 🔸 Команда: "<b>Уведомление об акции</b>" - ставит уведомление по акции, по которому бот оповестит вас;\n'
                         ' 🔸 Команда: "<b>Добавить акции</b>" - добавляет акции в ваш портфель, чтобы вы могли их отслеживать;\n'
                         ' 🔸 Команда: "<b>Удалить акции</b>" - удаляет акции из вашего портфеля;\n'
                         ' 🔸 Команда: "<b>Показать портфель</b>" - показывает ваш портфель;\n', parse_mode="html")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text + ' не является командой. Если хотите узнать функционал бота, введите команду "Помощь" или выберите эту команду в меню')

if __name__ == '__main__':
    executor.start_polling(dp)
