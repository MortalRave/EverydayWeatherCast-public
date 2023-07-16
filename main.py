import datetime as dt
import requests
import datetime

BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
API_KEY = "your api key"
CITY = "your city"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

def temp_to_celcius(x):
    return str(round((x - 273.15),1))

def unix_hour(x):
    time = datetime.datetime.fromtimestamp(int(x))
    return time.strftime("%H:%M")
    
city_name = CITY
sun_rise = unix_hour(int(response['city']['sunrise']))
sun_set = unix_hour(int(response['city']['sunset']))

class Timestamp:
    #tln = timelaps number
    def __init__(self,tln):
        self.tln = tln
        self.hour = str(unix_hour(int(response['list'][tln]['dt'])))
        self.temp = str(temp_to_celcius(int(response['list'][tln]['main']['temp']))) + '°C'
        self.weather = response['list'][tln]['weather'][0]['description']
        self.feeltemp = str(temp_to_celcius(int(response['list'][tln]['main']['feels_like']))) + '°C'
        self.pressure = str(response['list'][tln]['main']['pressure']) + ' hPa'
        self.rain = '-'
        self.rain_drop()
        

    def rain_drop(self):
        value = '-'
        try:
            value = response['list'][self.tln]['rain']
        except:
            value = 'no rain'

        if value == 'no rain':
            self.rain = '0 mm'
        else:
            self.rain = str(response['list'][self.tln]['rain']['3h']) + ' mm'
    


#Timestamps
h1 = Timestamp(0)
h2 = Timestamp(1)
h3 = Timestamp(2)
h4 = Timestamp(3)
h5 = Timestamp(4)
h6 = Timestamp(5)
h7 = Timestamp(6)
h8 = Timestamp(7)
h9 = Timestamp(8)