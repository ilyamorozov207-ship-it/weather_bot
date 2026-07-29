from weather_api import get_weather

def get_wind_speed(wind_direction):

    dict_wind_speed = [
        "С",
        "СВ",
        "В",
        "ЮВ",
        "Ю",
        "ЮЗ",
        "З",
        "СЗ"
        ]
    index = round(wind_direction / 45) %8
    return dict_wind_speed[index]
