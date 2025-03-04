# API -> Application Programming Interface
# api_used = openweathermap.org
from pprint import pprint
import requests

API_KEY = '4f8248b114738d3092a691e1ae9b0ba8'

class City:
    def __init__(self, name, lat, long, units="metric"):
        self.name = name
        self.lat = lat
        self.long = long 
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            API_URL = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.long}&appid={API_KEY}&units={self.units}'
            res = requests.get(API_URL)
        except:
            print("No internet Acces :(")

        self.response_json = res.json()

        self.temp = self.response_json['main']['temp']
        self.temp_min = self.response_json['main']['temp_min']
        self.temp_max = self.response_json['main']['temp_max']
    
    def print_temp(self):
        unit_symbol = "C"
        if  self.units == "imperial":
            unit_symbol = "F"
        print(f"In {self.name}, it is currently - {self.temp}° {unit_symbol}")
        print(f"Today's High - {self.temp_max}° {unit_symbol}")
        print(f"Today's Low - {self.temp_min}° {unit_symbol}")

my_city = City('London', 51.5072, 0.1276, 'imperial')
my_city.print_temp()



        