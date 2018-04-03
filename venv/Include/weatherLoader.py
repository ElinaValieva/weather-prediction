import requests
import math
from datetime import datetime, time, date

apiKey = "45b7a8b65841193a9b57eaf237df1693"
citys = ["oselki", "kipen", "pavlovsk", "peterhof", "lisiy nos", "kronstadt", "kolpino", "vyborg", "saint petersburg"]

# function to download data from api.openweathermap
def getData(city):
    request = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=45b7a8b65841193a9b57eaf237df1693")
    data = request.json()
    day = datetime.now().date().day
    temp = data['main']['temp']
    temp = math.ceil((temp -273.15)/1.8) #convert from Kelvin to Celsia
    pressure = data['main']['pressure']
    clouds = 1 if (data['clouds']['all'] > 50) else 0
    deg = convertDeg(data['wind']['deg'])
    speed = data['wind']['speed']
    result = str(day) + ";" + str(temp) + ";" + str(pressure) + ";" + str(clouds) + ";" + str(deg) + ";" + str(speed)
    return result


# function to convert to num destination wind
# 0 - не существует, 1 - Штиль, 2 - Ю, 3 - ЮЗ, 4 - З, 5 - СЗ, 6 - С, 7 - СВ, 8 - В, 9 - ЮВ
def convertDeg(deg):
    if (deg in range(0, 45) or deg == 360):
        result = 6
    elif (deg in range (46, 89)):
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
    else :
        result = 0
    return result

result = ""
for i in range (0, len(citys)):
    result = getData(citys[i]) + result;

print(result)