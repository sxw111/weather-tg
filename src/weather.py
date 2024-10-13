import httpx

from src.config import settings


async def weather_request(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": settings.WEATHER_API_TOKEN,
        "units": "metric",
        "lang": "en",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
            data = response.json()

            if response.status_code == 200:
                weather = {
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"],
                }

                return weather
            else:
                return None

        except httpx.HTTPStatusError:
            return None
