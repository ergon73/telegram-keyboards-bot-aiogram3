# Telegram Bot: Menus and Keyboards (aiogram 3)

Учебный проект по Telegram Bot API на Python. Демонстрирует reply-клавиатуры, inline-клавиатуры, URL-кнопки и динамическую замену inline-меню.

## Features

- `/start`
  - Reply-меню с кнопками **«Привет»** и **«Пока»**
  - Ответы: `Привет, <имя>!` и `До свидания, <имя>!`

- `/links`
  - Inline-кнопки с URL-ссылками: новости, музыка, видео

- `/dynamic`
  - Inline-кнопка **«Показать больше»**
  - По нажатию заменяется на **«Опция 1»** и **«Опция 2»**
  - Нажатие на опцию отправляет сообщение с текстом выбранной опции

## Tech stack

- Python 3.10+
- aiogram 3 (asyncio)
- python-dotenv (локальная загрузка `.env`)

## Project structure

```text
.
├── config.py        # загрузка BOT_TOKEN
├── keyboards.py     # все клавиатуры
├── main.py          # точка входа, хэндлеры
├── requirements.txt
└── .env.example
```

## Setup

### 1) Create Telegram bot token

- Создайте бота через BotFather и получите токен.

### 2) Configure environment

Создайте файл `.env` (не коммитить) рядом с `main.py`:

```env
BOT_TOKEN=123456:ABCDEF_your_token_here
```

### 3) Install dependencies (Windows)

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4) Run

```bat
python main.py
```

Проект использует polling, поэтому не поднимает веб-сервер и не занимает порты (включая `localhost:8000`).

## Manual testing checklist

- `/start` → появились кнопки «Привет» и «Пока»
- Нажать «Привет» → бот ответил `Привет, <имя>!`
- Нажать «Пока» → бот ответил `До свидания, <имя>!`
- `/links` → 3 URL-кнопки открываются
- `/dynamic` → «Показать больше» заменяется на 2 опции, опции отправляют текст
- После нажатий inline-кнопок нет «крутилки» (значит, `callback.answer()` есть)

## Author

Георгий Белянин (Georgy Belyanin)  
georgy.belyanin@gmail.com

## License

MIT
