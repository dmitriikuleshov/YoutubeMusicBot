from aiogram.utils import executor
from create_bot import dp
from download_audio import download_audio

from handlers import client, admin, other


async def on_startup(_):
    print('Bot is online')


client.register_handlers_client(dp)
# other.register_handlers_other(dp)

# skip_updates - если бот не онлайн, он потом
# не будет отвечать на эти сообщения
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
