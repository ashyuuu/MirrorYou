import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather_info = {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_info
    else:
        print("Failed to fetch weather data:", data["message"])
        return None

def main():
    api_key = "d3d4325ff5f6d3a19c6d2108de9bdf48"
    city = "Irvine"  # Replace with your desired city
    weather = get_weather(api_key, city)
    if weather:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    main()
