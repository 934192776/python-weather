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