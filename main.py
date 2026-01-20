import requests
from datetime import datetime
from rich import print


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def display_temperature(day, temperature, unit="C"):
    print(f"[blue]{day}[/blue]: {round(temperature)}º{unit}")


API_KEY = "2046c535afeb092fo82f1d306d8a2b2t"
BASE_URL = "https://api.shecodes.io/weather/v1"


def get_current_weather(city):
    url = f"{BASE_URL}/current?query={city}&key={API_KEY}"
    response = requests.get(url)
    return response.json()


def get_forecast_weather(city):
    url = f"{BASE_URL}/forecast?query={city}&key={API_KEY}"
    response = requests.get(url)
    return response.json()


def display_current_weather(city):
    data = get_current_weather(city)

    if "city" not in data:
        print("[red]Unable to fetch current weather. Please check the city name or API key.[/red]")
        return

    city_name = data["city"]
    country = data["country"]
    temperature = data["temperature"]["current"]

    print(
        f"\nIt is currently {round(temperature)}ºC "
        f"({round(convert_celsius_to_fahrenheit(temperature))}ºF) "
        f"in {city_name}, {country}."
    )


def display_forecast(city):
    data = get_forecast_weather(city)

    if "daily" not in data:
        return

    print("\n[green bold]Forecast:[/green bold]")
    for day in data["daily"]:
        date = datetime.fromtimestamp(day["time"])
        if date.date() != datetime.today().date():
            display_temperature(
                date.strftime("%A"),
                day["temperature"]["day"]
            )


def welcome():
    print("[purple bold]Welcome to my Weather App[/purple bold]")


def credit():
    print("\n[yellow]This app was built by Jing[/yellow]")


def main():
    welcome()
    city = input("Enter a city: ").strip()

    if not city:
        print("Please enter a valid city.")
        return

    display_current_weather(city)
    display_forecast(city)
    credit()


if __name__ == "__main__":
    main()
