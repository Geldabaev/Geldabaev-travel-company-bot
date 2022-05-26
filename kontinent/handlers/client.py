from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import zz_zayav, kb_contact, kb_client_menu, kb_client_sochy, kb_client_abhaz, kb_client_voda
from keyboards import kb_client_vozduh, kb_client_proch, kb_client_menu2
from excel_loader import edit2



# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await message.answer("Вас приветствует\nЧат-бот \"7 Континентов\"\n\nЕсли вы зашли не в тот пункт меню,\n и нужно вернуться назад,\nнапишите: /start\n\n"
                             "Если уже начали оформлять заявку\n и что-то ввели не верно,\nнапишите слово: *отмена*", parse_mode= "Markdown", reply_markup=zz_zayav)
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/continent_test_bot')


# @dp.message_handler(commands=['Заполнить_заявку'])
async def otkr_menu(message : types.Message):
    await message.answer("Поделитесь номером телефона", reply_markup=kb_contact)


sp_phone = {}
# перхватываем номер телефона
# @dp.message_handler(content_types=['contact'])
async def contact(message):
    global phonenumber
    if message.contact is not None:
        if edit2['is'] == 0:
            await bot.send_message(message.chat.id, 'Меню', reply_markup=kb_client_menu)
        else:
            await bot.send_message(message.chat.id, 'Меню', reply_markup=kb_client_menu2)
        phonenumber= str(message.contact.phone_number)
        # для вывода в тг создаем список
        sp_phone[message.chat.id] = phonenumber


"""обработчики хендлеров главного меню"""
@dp.message_handler(lambda message: 'Где найти нужный тур?' in message.text)
async def maps(message : types.Message):
    await bot.send_message(message.chat.id, paps)

# путеводитель по боту
paps = ('CОЧИ:\n----------\nКрасная поляна\nОбзорная Сочи\n33 Водопада\nЭпоха времени\nВоронцовские пещеры\nКаньоны Псахо (джип-тур)\nМамонтово Ущелье (джип-тур)\nСолохаул (джип-тур)\nИНДИВИДУАЛЬНЫЙ ТУР\n\n'
        'АБХАЗИЯ:\n----------------\nЗолотое Кольцо\nАбхазское застолье\nТермальные Источники\nГорода Призраки\nАльпийские Луга (джип-тур)\nАбхазский драйв (джип-тур)\nИНДИВИДУАЛЬНЫЙ ТУР\n\n'
        'МОРЕ:\n-----------\nМорская прогулка\nРыбалка в море\nАРЕНДА ЯХТ\n\n'
        'АКТИВ:\n------------\nРафтинг\nДайвинг\nКонные Прогулки\nКвадроциклы и Багги\nПараплан\nВоздушный Шар\nВертолёт\nПарашют\nСолохаул Парк\n\n'
        'Прочее:\n-------------\nШашлыки (индивидуальный)\nВечеринка в лесу\nАквапарк\nСафари Парк\nФорт Боярд\nКвесты\nБилеты на мероприятия\nДРУГОЕ')

# @dp.message_handler(commands="Сочи")
async def sochy(message : types.Message):
    await bot.send_message(message.chat.id, "Ваш выбор!", reply_markup=kb_client_sochy)


# @dp.message_handler(commands="Абхазия")
async def abhaz(message : types.Message):
    await bot.send_message(message.chat.id, "Ваш выбор!", reply_markup=kb_client_abhaz)


# @dp.message_handler(commands="Вода")
async def voda(message : types.Message):
    await bot.send_message(message.chat.id, "Ваш выбор!", reply_markup=kb_client_voda)


# @dp.message_handler(commands="Воздух")
async def vozduh(message : types.Message):
    await bot.send_message(message.chat.id, "Ваш выбор!", reply_markup=kb_client_vozduh)


# @dp.message_handler(commands="Прочее")
async def proch(message : types.Message):
    await bot.send_message(message.chat.id, "Ваш выбор!", reply_markup=kb_client_proch)




def regiter_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(otkr_menu, lambda message: 'Открыть меню' in message.text or 'ИСПРАВИТЬ' in message.text)
    dp.register_message_handler(contact, content_types=['contact'])
    dp.register_message_handler(sochy, lambda message: 'СOЧИ' in message.text) # сочи о на анг, чтобы не среагировал на обзор на сочи кнопку
    dp.register_message_handler(abhaz, lambda message: 'АБХАЗИЯ' in message.text)
    dp.register_message_handler(voda, lambda message: 'МОРЕ' in message.text)
    dp.register_message_handler(vozduh, lambda message: 'АКТИВ' in message.text)
    dp.register_message_handler(proch, lambda message: 'Прочее' in message.text)