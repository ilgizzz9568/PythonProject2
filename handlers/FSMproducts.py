from aiogram  import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import main_db
import buttons


class FSMProducts(StatesGroup):
    name_product = State()
    category = State()
    size = State()
    price = State()
    product_id = State()
    photo = State()
    submit = State()


async def start_fsm_store(message: types.Message):
    await message.answer('Введите название товара:', reply_markup=buttons.cancel_fsm)
    await FSMProducts.name_product.set()

async def name_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text


    await FSMProducts.next()
    await message.answer('Введите категорию товара:')


async def category_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
            data['category_product'] = message.text


    await FSMProducts.next()
    await message.answer('Введите размер:')


async def size_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size_product'] = message.text


    await FSMProducts.next()
    await message.answer('Введите цену товара:')


async def price_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price_product'] = message.text


    await FSMProducts.next()
    await  message.answer('Введите артикул:')


async def product_id_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text


    await FSMProducts.next()
    await message.answer('отправьте фото:')


async def photo_load (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSMProducts.next()
    await message.answer('Верные ли данные ?',reply_markup=buttons.submit)
    await message.answer_photo(photo=data['photo'],
                               caption=f'Название товара - {data["name_product"]}\n'
                                       f'Категория - {data["category_product"]}\n'
                                       f'Размер товара - {data["size_product"]}\n'
                                       f'Цена - {data["price_product"]}\n'
                                       f'Артикул - {data["product_id"]}')


async def submit_load(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            await main_db.sql_insert_store(
                name_product=data['name_product'],
                category=data['category_product'],
                size=data['size_product'],
                price=data['price_product'],
                product_id=data['product_id'],
                photo=data['photo']
            )

            await message.answer('Ваши данные в базе!',reply_markup=buttons.remove_keyboard)
            await state.finish()
    elif message.text == 'нет':
        await message.answer('Отменено!', reply_markup=buttons.remove_keyboard)
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands='add')
    dp.register_message_handler(name_load, state=FSMProducts.name_product)
    dp.register_message_handler(category_load, state=FSMProducts.category)
    dp.register_message_handler(size_load, state=FSMProducts.size)
    dp.register_message_handler(price_load, state=FSMProducts.price)
    dp.register_message_handler(product_id_load, state=FSMProducts.product_id)
    dp.register_message_handler(photo_load, state=FSMProducts.photo, content_types=['photo'])
    dp.register_message_handler(submit_load, state=FSMProducts.submit)



