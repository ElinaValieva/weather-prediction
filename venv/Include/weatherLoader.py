import requests
import math
from datetime import datetime, time, date
import weatherPredictor
import warnings

warnings.filterwarnings('ignore', '.*do not.*', )
# 498817 - Spb
# 475060 - Oselki
# 504875 - Kipen
# 512053 - Pavlovsk
# 510291 - Peterhof
# 534841 - Lisiy nos
# 540771 - Kronstadt
# 546105 - Kolpino
# 470546 - Vyborg
# function to download data from api.openweathermap
citys = ["oselki", "kipen", "pavlovsk", "peterhof", "lisiy nos", "kronstadt", "kolpino", "vyborg"]
citysId = [475060, 504875, 512053, 510291, 534841, 540771, 546105, 470546];
mainCityId = 498817;
filenameTest = 'wx_test'
filenamePrediction = 'wy_test'
day = datetime.now().date().day


# function to download data from api.openweathermap
def getData(city):
    request = requests.get(
        # "http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=45b7a8b65841193a9b57eaf237df1693")
        "http://api.openweathermap.org/data/2.5/forecast?id=" + str(city) + "&appid=45b7a8b65841193a9b57eaf237df1693")
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
        dt = tmp[i]['dt_txt'];
        date_dt = find_date(dt)
        time_dt = find_time(dt)
        if (time_dt == '15'):
            tempF = tmp[i]['main']['temp']
            temp = math.ceil(tempF - 273.15)
            pressure = math.ceil(tmp[i]['main']['pressure'])
            clouds = (1 if (tmp[i]['clouds']['all'] > 50) else 0) + clouds
            deg = convertDeg(tmp[i]['wind']['deg'])
            speed = math.ceil(tmp[i]['wind']['speed'])
            st = str(date_dt) + ";" + str(temp) + ";" + str(pressure) + ";" + str(clouds) + ";" + str(deg) + ";" + str(
                speed)
            result.append(st)
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


def find_date(dt):
    date = dt[:dt.find(' ')]
    date = date[str(date).find('-'):]
    date = date[1:]
    date = date[str(date).find('-'):]
    date = date[1:]
    if (date[0] == '0'):
        date = date[1:]
    return date


def find_time(dt):
    time = dt[dt.find(' '):]
    time = time[:str(time).find(':')]
    time = time[1:]
    return time


test = []
# for i in range(0, len(citys)):
#    test.append(getData(citys[i]))
for i in range(0, len(citysId)):
    test.append(getData(citysId[i]))
# prediction = getData("saint petersburg")
prediction = getData(mainCityId)
func(test)
for i in range(0, len(prediction)):
    addToDS(prediction[i], filenamePrediction)
# prediction
weatherPredictor.predict()
