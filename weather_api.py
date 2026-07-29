import requests


def get_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(
        url,
        params={
            "name": city,
            "count": 1,
            "language": "ru"
        }
    )

    data = response.json()

    if not data.get("results"):
        return None

    city_data = data["results"][0]

    latitude = city_data["latitude"]
    longitude = city_data["longitude"]


    return latitude, longitude



def get_weather(latitude, longitude):

    api_key = "https://api.open-meteo.com/v1/forecast"

    response = requests.get(
        api_key,
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "apparent_temperature,"
                "relative_humidity_2m,"
                "cloud_cover,"
                "precipitation,"
                "wind_speed_10m,"
                "wind_direction_10m,"
                "weather_code"
            ),
            "timezone": "auto",
            "models": "ecmwf_ifs025"
        }
    )

    data = response.json()

    temperature = data["current"]["temperature_2m"]
    wind = data["current"]["wind_speed_10m"]
    apparent = data["current"]["apparent_temperature"]
    humidity = data["current"]["relative_humidity_2m"]
    cloud_cover = data["current"]["cloud_cover"]
    precipitation = data["current"]["precipitation"]
    wind_direction = data["current"]["wind_direction_10m"]
    weather_code = data["current"]["weather_code"]


    return {
        "temperature": temperature,
        "wind": wind,
        "apparent": apparent,
        "humidity": humidity,
        "cloud_cover": cloud_cover,
        "precipitation": precipitation,
        "wind_direction": wind_direction,
        "weather_code": weather_code
    }
