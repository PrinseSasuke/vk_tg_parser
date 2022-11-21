from aiogram import types
from loader import dp
from states import get_link
from aiogram.dispatcher import FSMContext
from parser import parse
token = "d5bbb92fd5bbb92fd5bbb92f42d5c6dea0dd5bbd5bbb92fb77471cbf27eff0b52bcf73e"
version = 5.131
sort = "id_asc"

@dp.message_handler(text = '/start')
async def command_start(message = types.Message):
    await message.answer(f"Hello {message.from_user.full_name} \n"+
                         "Enter your link: ")
    await get_link.link.set()
@dp.message_handler(state = get_link.link)
async def state1(message: types.Message, state:FSMContext):
    answer = message.text
    await state.update_data(link = answer)
    data = await state.get_data()
    link = data.get('link')
    group_id = link[15::]
    parse(token = token, version = version, group_id = group_id, sort = sort)
    await message.reply_document(open('names.xlsx', 'rb'))
    await state.finish()