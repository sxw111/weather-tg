import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from weather import weather_request
from src.config import settings

logger = logging.getLogger("bot")
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

bot = Bot(token=settings.TG_API_TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    logger.info(f"Received /start command from user {message.from_user.id}")
    await message.answer(
        "Hi, this is a bot that helps you find out the weather. "
        "Write the name of the city."
    )


@dp.message()
async def get_weather(message: types.Message):
    city = message.text.strip()
    logger.info(f"User {message.from_user.id} requested weather for city: {city}")

    weather_data = await weather_request(city=city)

    if weather_data:
        response_message = (
            f"Weather in {city} now:\n"
            f"Temperature - {weather_data['temp']}°C\n"
            f"Humidity - {weather_data['humidity']}%\n"
            f"Description - {weather_data['description']}"
        )
        logger.info(f"Successfully retrieved weather data for city: {city}")
    else:
        response_message = (
            f"Failed to get weather data for the city {city}.\n"
            f"Please enter the city name again."
        )
        logger.error(f"Failed to retrieve weather data for city: {city}")

    await message.reply(response_message)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
