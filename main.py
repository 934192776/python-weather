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