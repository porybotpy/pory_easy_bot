# main.py
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

TOKEN = "7678197588:AAGSRMGuILNVBOtRbC3ZPimfcNO4hs-X6IY"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(CommandStart())
async def welcome(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="شروع چت ناشناس 🕵️", callback_data="start_chat")
    await message.answer(
        "سلام! به ربات ایزی خوش اومدی 🌟\n\nمن پوری‌ام، یه دختر ترنس مهربون که همیشه کنارتم.\n\nبرای شروع چت ناشناس، روی دکمه زیر بزن 👇",
        reply_markup=builder.as_markup()
    )

@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    await callback.answer("این قسمت هنوز در دست ساخت است 😅")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
