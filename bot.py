import os
import sys
from urllib.parse import urlparse

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes


def load_env_file() -> None:
    """Read simple KEY=value entries from .env without an extra dependency."""
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if not os.path.isfile(env_path):
        return

    with open(env_path, encoding="utf-8") as env_file:
        for raw_line in env_file:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def required_setting(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value or value.startswith("PUT_"):
        raise ValueError(f"Заполните {name} в файле .env")
    return value


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo_url = required_setting("PHOTO_URL")
    link_url = required_setting("BUTTON_URL")
    text = os.getenv("START_TEXT", "Привет!  Актуальный бот тут👇").strip()
    button_text = os.getenv("BUTTON_TEXT", "Открыть бота").strip()

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(button_text, url=link_url)]]
    )
    await update.effective_message.reply_photo(
        photo=photo_url,
        caption=text,
        reply_markup=keyboard,
    )


def validate_url(name: str, value: str) -> None:
    parsed = urlparse(value)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError(f"{name} должен быть полной ссылкой, начинающейся с https://")


def main() -> None:
    load_env_file()
    try:
        token = required_setting("BOT_TOKEN")
        photo_url = required_setting("PHOTO_URL")
        button_url = required_setting("BUTTON_URL")
        validate_url("PHOTO_URL", photo_url)
        validate_url("BUTTON_URL", button_url)
    except ValueError as error:
        print(error, file=sys.stderr)
        raise SystemExit(1) from error

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()


if __name__ == "__main__":
    main()
