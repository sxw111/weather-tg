# weather-tg
A Telegram bot created using the `aiogram` and `httpx` libraries to fetch weather data through the OpenWeatherMap service.

## Running the Bot
1. Clone the repository to your local machine.
```bash
git clone https://github.com/sxw111/weather-tg.git
cd weather-tg/
```
2. Install the dependencies.
```bash
poetry install
```
3. Create a `.env` file and add your API tokens there.
4. Run the bot with the following command:
```bash
PYTHONPATH=./src poetry run python -m src.bot
```
