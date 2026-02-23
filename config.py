"""Загрузка конфигурации из переменных окружения."""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError(
        "Переменная окружения BOT_TOKEN не задана. Создайте .env и добавьте BOT_TOKEN=..."
    )  # noqa: EM101
