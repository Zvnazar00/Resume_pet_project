from aiogram import Dispatcher
from Resumeaiogram.config import Admins


async def notify_admins(dp: Dispatcher):
    for admin in Admins.split(','):
        try:
            await dp.bot.send_message(chat_id=admin, text='Бот працює!')
        except Exception as error:
            print(f'Не удалось отправить сообщение разработчику {admin}. Ошибка: {error}')

