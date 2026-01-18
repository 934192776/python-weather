# Collected the data
first_name = input("What's your name? ")
city = input("What city are you currently? ")
celsius_temperature  = input(f"What is the temperature in {city}? ")

# Calculated the Fahrenheit temperature
fahrenheit_temperature = (float(celsius_temperature) * 9/5) + 32
fahrenheit_temperature = round(fahrenheit_temperature)

# Display the welcome message
welcome_message = f"Hi {first_name.capitalize()}, you are in {city.capitalize()} and it is currently {celsius_temperature}ºC or {fahrenheit_temperature}ºF)"
print(welcome_message)

# Calculate tonight's temperatures
tonight_celsius_temperature = float(celsius_temperature) - 10
tonight_celsius_temperature = round(tonight_celsius_temperature)
tonight_fahrenheit_temperature = (float(tonight_celsius_temperature) * 9/5) + 32
tonight_fahrenheit_temperature = round(tonight_fahrenheit_temperature)

# Display prediction message
prediction_message = f"I predict that tonight, the temperature will reach {tonight_celsius_temperature}ºC or {tonight_fahrenheit_temperature}ºF)"

print(prediction_message)

print("Have a good day!")



city = input("Enter the name of a city: ")
temperature = input(f"Enter the temperature in {city}: ")

if city and temperature:
  temperature = int(temperature)
  
  if temperature > 20:
    print(f"It is currently warm in {city} with a temperature of {temperature} degrees.")
  elif temperature > 10:
    print(f"It is currently chilly in {city} with a temperature of {temperature} degrees.")
  else:
    print(f"It is currently cold in {city} with a temperature of {temperature} degrees.")
else:
  print("Please try again and enter a city and temperature")




def convert_celsius_to_fahrenheit(celsius_value):
  """Converts a Celsius value into Fahrenheit"""
  fahrenheit_value = (float(celsius_value) * 9/5) + 32
  
  return fahrenheit_value

def display_temperature(city_name, temperature):
  """Displays the temperature of a city"""
  fahrenheit_temperature = convert_celsius_to_fahrenheit(temperature)    
  print(f"It is currently {temperature}ºC ({round(fahrenheit_temperature)}ºF) in {city_name.capitalize()}")
  
city = input("Enter the name of the city: ")
celsius_temperature = input(f"Enter the temperature in {city.capitalize()}: ")
if city and celsius_temperature:
  display_temperature(city, celsius_temperature)
else:
  print("You did not enter a city and/or temperature")



def concert_celsius_to_fahrenheit(celsius_temperature):
  farehnheit_temperature = (celsius_temperature * 9/5) + 32
  return farehnheit_temperature

weather = {
  "city":"Lisbon",
  "country":"Portugal",
  "temperature": 17.94,
  "humidity":77
}

# Display the weather in Lisbon such as:
# It is 18ºC (64ºF) in Lisbon, Portugal, the humidity level is 77%.

city = weather["city"]
country = weather["country"]
temperature = weather["temperature"]
humidity = weather["humidity"]
farehnheit_temperature = concert_celsius_to_fahrenheit(temperature)
print(f"It is {round(temperature)}ºC ({round(farehnheit_temperature)}ºF) in {city}, {country} the humidity level is {humidity}%.")

forecast = {
  "city":"Lisbon",
  "country":"Portugal",
  "daily": [
    17.76,
    13.08,
    12.14,
    11.25,
    14.29
  ]
}
      
# Display the forecast in Lisbon such as:
# The forecast for Lisbon, Portugal for the next 5 days is:
# Day 1: 18ºC
# Day 2: 13ºC
# Day 3: 12ºC
# Day 4: 11ºC
# Day 5: 14ºC

city = forecast["city"]
country = forecast["country"]

print(f"The forecast for {city}, {country} for the next 5 days is:")

index = 0
for temperature in forecast["daily"]:
  fahrenheit_temperature = round(concert_celsius_to_fahrenheit(temperature))
  print(f"Day {index + 1}: {round(temperature)}ºC ({fahrenheit_temperature}ºF)")
  index = index + 1



from rich import print
import requests

# Get the city from user
city = input("Enter a city: ")
city = city.strip()

# Make API call
api_key = "2046c535afeb092fo82f1d306d8a2b2t"
api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"
api_response = requests.get(api_url)
weather_data = api_response.json()

# Generate message from api result
country_name = weather_data['country']
city_name = weather_data["city"]
temperature = round(weather_data['temperature']['current'])

print(f"It is currently {temperature}ºC in {city_name}, {country_name}.")




import requests
from rich import print
from datetime import datetime

def display_temperatue(day, temperature, unit='C'):
  """Displays a temperature with day"""
  print(f"[blue]{day}[/blue]: {round(temperature)}º{unit}")

def display_current_weather(city):
  """Displays the current weather"""
  api_key = "2046c535afeb092fo82f1d306d8a2b2t"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

  response = requests.get(api_url)
  current_weather_data = response.json()
  current_weather_city = current_weather_data['city']
  current_weather_temperature = current_weather_data['temperature']['current']
  
  display_temperatue("Today", round(current_weather_temperature))

def display_forecast_weather(city_name):
  """Display the weather forecast of a city"""
  api_key = "2046c535afeb092fo82f1d306d8a2b2t"
  api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"

  response = requests.get(api_url)
  forecast_weather_data = response.json()
  print("\n[green bold]Forecast:[/green bold]")
  for day in forecast_weather_data['daily']:
    timestamp = day['time']  
    date = datetime.fromtimestamp(timestamp)
    formatted_day = date.strftime("%A")
    temperature = day['temperature']['day']
    
    if date.date() != datetime.today().date():
      display_temperatue(formatted_day, round(temperature))

def credit():
  """Display a credit message"""
  print("\n[yellow]This app was built by Matt Delac[/yellow]")

def welcome():
  """Display a welcome"""
  print("[purple bold]Welcome to my weather app[/purple bold]")
  

welcome()
city_name = input("Enter a city: ")
city_name = city_name.strip()

if city_name:
  display_current_weather(city_name)
  display_forecast_weather(city_name)
  credit()
else:
  print("Please try again with a city")
