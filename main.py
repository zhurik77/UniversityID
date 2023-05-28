import aiogram
import asyncio
from aiogram import Bot,Dispatcher,types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
import logging
import sqlite3
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = "5932195474:AAELJmjaT8SA7_rOpDvbhm_Z6FlDz75XUBM"
bot = Bot(token=API_TOKEN)
disp = Dispatcher(bot)

#langSetKb = InlineKeyboardMarkup(row_width=1)
langSetButton = InlineKeyboardButton("Выбор языка/Language setup", callback_data="b1")
langSetKb = InlineKeyboardMarkup(resize_keyboard = True).add(langSetButton)

@disp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Привет!\nЯ bot_name от команды team_name\nIf you do not understand me, please, select another Language by pressing the button below',reply_markup=langSetKb)

langbt1 = InlineKeyboardButton(" Русский ", callback_data="langbt1")
langbt2 = InlineKeyboardButton(" English ", callback_data="langbt2")
langbtSet = InlineKeyboardMarkup(resize_keyboard = True).add(langbt1,langbt2)

@disp.callback_query_handler(lambda c: c.data == 'b1')
async def process_callback_langSetButton(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Пожалуйста, выберите язык", reply_markup=langbtSet)










if __name__ == '__main__':
   executor.start_polling(disp, skip_updates=True)
