from aiogram import Bot, Dispatcher, executor, types
from db import db


API_token = "5807616923:AAE9p6EC5p2YVhiXSjLzpPLpLDxejmmPk_I"

bot = Bot(token = API_token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message = types.message):
    await message.reply('Assalomu alaykum! Botimizga xush kelibsiz, bu bot orqali ismlar ma\'nosini bilib olishingiz mumkin, barcha ma\'lumotlar ismlar.com saytidan olingan.')

@dp.message_handler()
async def main_work(message = types.message.ParseMode.HTML):
    dict = db.get_info(message.text)
    if dict:
        resp = '⚡️' + str(dict['title']) + '⚡️' + '\n\n' + 'Ma\'nosi: <b>' + str(dict['meaning']) + '</b>\n\n'
        if dict['types']:
            resp += 'Shakllari: <i>' + str(dict['types']) + '</i>\n\n'
        if dict['category']:
            resp += 'Ism Turi: <b>' + str(dict['category']) + '</b>\n\n'
        resp += "izlashga ketgan vaqt: "+str(dict['duration'])+"soniya\n\n"
        resp += '👁: <b>' + str(dict['views']) + '</b>'
        await message.answer(resp , parse_mode = 'HTML')
    else:
        await message.reply('Afsuski bizda bu ism haqida ma\'lumot topilmadi.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
