# Telegram-бот: фото и ссылка по /start

Бот отправляет фотографию с подписью и кнопкой-ссылкой, когда пользователь нажимает «Start» или отправляет `/start`.

## Запуск

1. Установите Python 3.10 или новее.
2. Создайте бота в Telegram через [@BotFather](https://t.me/BotFather) командой `/newbot` и скопируйте токен.
3. Скопируйте `.env.example` в `.env` и заполните `BOT_TOKEN`, `PHOTO_URL` и `BUTTON_URL`. Для фото укажите прямой HTTPS-адрес файла изображения.
4. В этой папке выполните:

   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python bot.py
   ```

5. Откройте чат с ботом и нажмите **Start**.

Текст подписи и надпись на кнопке меняются в `.env` через `START_TEXT` и `BUTTON_TEXT`. Токен хранится только локально в `.env`; не публикуйте этот файл.
