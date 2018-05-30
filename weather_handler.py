import datetime

import weather_loader


class WeatherHandler(object):
    TEMPERATURE = "temperature"
    WIND = "wind"
    WIND_SPEED = "wind_speed"
    WIND_DIRECTION = "wind_direction"
    PRESSURE = "pressure"
    CLOUDS = "clouds"
    WEATHER = "weather"
    DAY = "day"
    TODAY = "с"
    TOMORROW = "з"
    DAY_AFTER_TOMORROW = "п"
    WEEK = "н"

    def __init__(self):
        self.weather = None
        self.last_update = None

    def _update(self):
        current_date = datetime.date.today().strftime("%Y%m%d")
        if self.last_update is None or current_date != self.last_update:
            self.last_update = current_date
            self.weather = weather_loader.calculate_weekly_weather()
            return True
        return False

    @staticmethod
    def _map_day(day):
        if day[0] == WeatherHandler.TODAY:
            return 0
        elif day[0] == WeatherHandler.TOMORROW:
            return 1
        elif day[0] == WeatherHandler.DAY_AFTER_TOMORROW:
            return 2
        else:
            return None

    @staticmethod
    def get_params(weather_list, param):
        if param == WeatherHandler.TEMPERATURE:
            data = {WeatherHandler.TEMPERATURE: str(weather_list[1])}
            return data
        elif param == WeatherHandler.WIND:
            data = {WeatherHandler.WIND_SPEED: str(weather_list[5]),
                    WeatherHandler.WIND_DIRECTION: WeatherHandler.convert_dir(round(weather_list[4]))}
            return data
        elif param == WeatherHandler.PRESSURE:
            data = {WeatherHandler.PRESSURE: str(weather_list[2])}
            return data
        elif param == WeatherHandler.CLOUDS:
            data = {WeatherHandler.CLOUDS: str(round(weather_list[3]))}
            return data
        elif param == WeatherHandler.DAY:
            data = {WeatherHandler.DAY: str(weather_list[0])}
            return data
        elif param == WeatherHandler.WEATHER:
            data = {
                WeatherHandler.TEMPERATURE: str(weather_list[1]),
                WeatherHandler.WIND_SPEED: str(weather_list[5]),
                WeatherHandler.WIND_DIRECTION: WeatherHandler.convert_dir(round(weather_list[4])),
                WeatherHandler.PRESSURE: str(weather_list[2]),
                WeatherHandler.CLOUDS: str(round(weather_list[3]))
            }
            return data
        else:
            raise Exception("param is not recognize: " + param)

    @staticmethod
    def convert_dir(direct):
        if direct == 0 or direct == 1:
            return "Calm"
        elif direct == 2:
            return "South"
        elif direct == 3:
            return "Southwest"
        elif direct == 4:
            return "West"
        elif direct == 5:
            return "Northwest"
        elif direct == 6:
            return "North"
        elif direct == 7:
            return "Northeast"
        elif direct == 8:
            return "East"
        elif direct == 9:
            return "Southeast"
        else:
            return "Calm"

    def get_response(self, param, day):
        self._update()

        response = []

        if day[0] != WeatherHandler.WEEK:
            day_num = WeatherHandler._map_day(day)
            if day_num is None:
                raise Exception("day param is not recognize: " + day)
            else:
                response.append(WeatherHandler.get_params(self.weather[day_num], param))
                return response
        else:
            for weather in self.weather:
                response.append(WeatherHandler.get_params(weather, param))
            return response
