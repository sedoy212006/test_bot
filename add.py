from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
token = "5395649292:AAHAo5z_zyz3o-VU1TfRCOyKY--LXc74rMo"
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id

    text = "Привет)))"

    sent_message = await bot.send_message(chat_id, text=text)

    sent_message = await bot.send_photo(chat_id,
                                        photo="https://i.pinimg.com/originals/f4/d2/96/f4d2961b652880be432fb9580891ed62.png")


executor.start_polling(dp)

# bot.get_updates()
