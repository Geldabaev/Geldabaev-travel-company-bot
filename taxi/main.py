from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
    print("Бот вышел в онлайн")
    # передать в executor


# запускаем зарегистрированные хендлеры
from handlers import client, opros, correct_delete


client.regiter_handlers_client(dp)
opros.register_handlers_opros(dp)
correct_delete.register_handlers_correct_delete(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup) #skip_updates=True чтобы не засыпало сообщениями когда были оф