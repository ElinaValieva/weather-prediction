import json

import flask

from weather_handler import WeatherHandler

app = flask.Flask(__name__)

weather = WeatherHandler()


def to_json(data):
    return json.dumps(data) + "\n"


def resp(code, data):
    return flask.Response(
        status=code,
        mimetype="application/json",
        response=to_json(data)
    )


@app.route('/', methods=['GET'])
def root():
    return resp(200, {
        "temperature": "/temperature?date",
        "wind": "/wind?date",
        "pressure": "/pressure?date",
        "clouds": "/clouds?date",
        "weather": "/weather?date",
    })


@app.route('/temperature', methods=['GET'])
def get_temperature():
    date = flask.request.args.get('date', default='с', type=str)
    try:
        response = weather.get_response(WeatherHandler.TEMPERATURE, date)
    except Exception as e:
        return resp(400, str(e))
    return resp(200, response)


@app.route('/wind', methods=['GET'])
def get_wind():
    date = flask.request.args.get('date', default='с', type=str)
    try:
        response = weather.get_response(WeatherHandler.WIND, date)
    except Exception as e:
        return resp(400, str(e))
    return resp(200, response)


@app.route('/pressure', methods=['GET'])
def get_pressure():
    date = flask.request.args.get('date', default='с', type=str)
    try:
        response = weather.get_response(WeatherHandler.PRESSURE, date)
    except Exception as e:
        return resp(400, str(e))
    return resp(200, response)


@app.route('/clouds', methods=['GET'])
def get_clouds():
    date = flask.request.args.get('date', default='с', type=str)
    try:
        response = weather.get_response(WeatherHandler.CLOUDS, date)
    except Exception as e:
        return resp(400, str(e))
    return resp(200, response)


@app.route('/weather', methods=['GET'])
def get_weather():
    date = flask.request.args.get('date', default='с', type=str)
    try:
        response = weather.get_response(WeatherHandler.WEATHER, date)
    except Exception as e:
        return resp(400, str(e))
    return resp(200, response)


if __name__ == '__main__':
    app.debug = True  # enables auto reload during development
    app.run(host='192.168.0.117', port=8080)
