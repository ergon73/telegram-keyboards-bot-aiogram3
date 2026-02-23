"""Точка входа и хэндлеры Telegram-бота."""

from __future__ import annotations

import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

import keyboards as kb
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Обработка /start: отправка reply-меню."""
    await message.answer(
        "Меню:",
        reply_markup=kb.start_menu(),
    )


@dp.message(Command("links"))
async def cmd_links(message: Message) -> None:
    """Обработка /links: отправка inline-кнопок с URL."""
    await message.answer(
        "Ссылки:",
        reply_markup=kb.links_menu(),
    )


@dp.message(Command("dynamic"))
async def cmd_dynamic(message: Message) -> None:
    """Обработка /dynamic: отправка динамической inline-клавиатуры."""
    await message.answer(
        "Динамическое меню:",
        reply_markup=kb.dynamic_more_menu(),
    )


@dp.message(F.text == "Привет")
async def on_hello(message: Message) -> None:
    """Обработка нажатия «Привет»."""
    name = kb.user_display_name(message.from_user)
    await message.answer(f"Привет, {name}!")


@dp.message(F.text == "Пока")
async def on_bye(message: Message) -> None:
    """Обработка нажатия «Пока»."""
    name = kb.user_display_name(message.from_user)
    await message.answer(f"До свидания, {name}!")


@dp.callback_query(F.data == "show_more")
async def on_show_more(callback: CallbackQuery) -> None:
    """Callback «Показать больше»: замена клавиатуры на опции."""
    await callback.answer()

    if callback.message:
        await callback.message.edit_reply_markup(
            reply_markup=kb.dynamic_options_menu()
        )


@dp.callback_query(F.data.in_({"opt_1", "opt_2"}))
async def on_option(callback: CallbackQuery) -> None:
    """Callback «Опция 1» или «Опция 2»: отправка текста выбранной опции."""
    await callback.answer()

    text = "Опция 1" if callback.data == "opt_1" else "Опция 2"
    if callback.message:
        await callback.message.answer(text)


async def main() -> None:
    """Запуск polling."""
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
