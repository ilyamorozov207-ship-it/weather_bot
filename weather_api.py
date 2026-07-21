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
            "current": "temperature_2m,wind_speed_10m"
        }
    )

    data = response.json()

    temperature = data["current"]["temperature_2m"]
    wind = data["current"]["wind_speed_10m"]

    return temperature, wind


