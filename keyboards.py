"""Определения клавиатур бота."""

from __future__ import annotations

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from aiogram.types import User
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def user_display_name(user: User | None) -> str:
    """Возвращает отображаемое имя пользователя."""
    if not user:
        return "друг"
    if user.first_name:
        return user.first_name
    if user.username:
        return user.username
    return "друг"


def start_menu() -> ReplyKeyboardMarkup:
    """Reply-меню для /start: «Привет» и «Пока»."""
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="Привет"),
        KeyboardButton(text="Пока"),
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def links_menu() -> InlineKeyboardMarkup:
    """Inline-меню для /links: URL-кнопки новости, музыка, видео."""
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Новости", url="https://news.ycombinator.com/"),
        InlineKeyboardButton(text="Музыка", url="https://music.youtube.com/"),
        InlineKeyboardButton(text="Видео", url="https://www.youtube.com/"),
    )
    builder.adjust(1)
    return builder.as_markup()


def dynamic_more_menu() -> InlineKeyboardMarkup:
    """Начальная inline-клавиатура для /dynamic: «Показать больше»."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Показать больше", callback_data="show_more")],
        ]
    )


def dynamic_options_menu() -> InlineKeyboardMarkup:
    """Inline-клавиатура опций после «Показать больше»: Опция 1, Опция 2."""
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Опция 1", callback_data="opt_1"),
        InlineKeyboardButton(text="Опция 2", callback_data="opt_2"),
    )
    builder.adjust(2)
    return builder.as_markup()
