import pydantic
import requests, json
from pydantic import BaseModel, validator

class BaseModel(BaseModel):
    class Config:
        extra = pydantic.Extra.forbid

class Temperature(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float

    @validator('temp')
    def c_in_f(cls, value):
        return round(value * 9 / 5 + 32, 2)

class Weather(BaseModel):
    temperature: Temperature
    pressure: int
    description: str
    name: str


class Coordinate:

    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    def get_weather_information(self):
        r = requests.get(f'https://fcc-weather-api.glitch.me/api/current?lat={self.__latitude}&lon={self.__longitude}')
        try:
            if r.status_code != 200:
                raise Exception(f'error : {r.status_code}')
            j_date = json.loads(r.text)
            try:
                _feels_like_ = j_date.get['main']['feels_like']
            except:
                _feels_like_ = 0
            data = {
                'temperature': {
                    'temp': j_date['main']['temp'],
                    'feels_like': _feels_like_,
                    'temp_min': j_date['main']['temp_min'],
                    'temp_max': j_date['main']['temp_max']

                },
                'pressure': j_date['main']['pressure'],
                'description': j_date['weather'][0]['description'],
                'name': j_date['name']
            }

        except Exception as e:
            return None
        return Weather(**data)

coordinate = Coordinate(35, 139)
weather = coordinate.get_weather_information()
print(f'In  {weather.name} {weather.temperature.temp} F')
