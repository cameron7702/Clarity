import python_weather
import asyncio
from datetime import datetime

degree = u'\N{DEGREE SIGN}'

async def getweather():
    client = python_weather.Client(format=python_weather.METRIC)
    try:
        weather = await client.find("Kingston")
    except:
        await client.close()
        return "Offline"

    today = datetime.today().strftime('%Y-%m-%d')

    for forecast in weather.forecasts:
        if str(forecast.date)[:10] == today:
            weather = f'{forecast.sky_text}: {forecast.temperature}{degree}C'

    await client.close()
    return weather

def weather():
    loop = asyncio.get_event_loop()
    weather = loop.run_until_complete(getweather())
    return weather