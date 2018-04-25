import requests
import math
from datetime import datetime, time, date
import weatherPredictor
import warnings

warnings.filterwarnings('ignore', '.*do not.*', )

# function to download data from api.openweathermap
citys = ["oselki", "kipen", "pavlovsk", "peterhof", "lisiy nos", "kronstadt", "kolpino", "vyborg"]
filenameTest = 'wx_test'
filenamePrediction = 'wy_test'
day = datetime.now().date().day


# function to download data from api.openweathermap
def getData(city):
    request = requests.get(
        "http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=45b7a8b65841193a9b57eaf237df1693")
    data = request.json()
    day = datetime.now().date().day
    tmp = data['list']
    temp = 0
    pressure = 0
    clouds = 0
    deg = 0
    speed = 0
    result = []
    for i in range(0, len(tmp)):
        if (i % 5 != 0 or i == 0):
            tempF = tmp[i]['main']['temp']
            temp = temp + math.ceil((tempF - 273.15) / 1.8)
            pressure = pressure + tmp[i]['main']['pressure']
            clouds = (1 if (tmp[i]['clouds']['all'] > 50) else 0) + clouds
            deg = deg + convertDeg(tmp[i]['wind']['deg'])
            speed = speed + tmp[i]['wind']['speed']
        else:
            temp = math.ceil(temp / 5)
            pressure = math.ceil(pressure / 5)
            clouds = math.ceil(clouds / 5)
            deg = math.ceil(deg / 5)
            speed = math.ceil(speed / 5)
            st = str(day) + ";" + str(temp) + ";" + str(pressure) + ";" + str(clouds) + ";" + str(deg) + ";" + str(
                speed)
            result.append(st)
            temp = 0
            pressure = 0
            clouds = 0
            deg = 0
            speed = 0
            day = day + 1
    return result


# function to convert to num destination wind
# 0 - не существует, 1 - Штиль, 2 - Ю, 3 - ЮЗ, 4 - З, 5 - СЗ, 6 - С, 7 - СВ, 8 - В, 9 - ЮВ
def convertDeg(deg):
    if (deg in range(0, 45) or deg == 360):
        result = 6
    elif (deg in range(46, 89)):
        result = 7
    elif (deg in range(90, 135)):
        result = 8
    elif (deg in range(136, 179)):
        result = 9
    elif (deg in range(180, 225)):
        result = 2
    elif (deg in range(225, 269)):
        result = 3
    elif (deg in range(270, 305)):
        result = 4
    elif (deg in range(306, 359)):
        result = 5
    else:
        result = 0
    return result


def addToDS(result, filename):
    file = open(filename, 'a')
    file.write('\n' + result)
    file.close()


def func(test):
    for j in range(0, len(test[0])):
        result = ""
        for k in range(0, len(test)):
            if (result != ""):
                result = result + ";" + test[k][j]
            else:
                result = test[k][j]
        addToDS(result, filenameTest)


test = []
for i in range(0, len(citys)):
    test.append(getData(citys[i]))
prediction = getData("saint petersburg")
func(test)
for i in range(0, len(prediction)):
    addToDS(prediction[i], filenamePrediction)
# prediction
weatherPredictor.predict()
