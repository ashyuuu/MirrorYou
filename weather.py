import tkinter as tk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt

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
        messagebox.showerror("Error", f"Failed to fetch weather data: {data['message']}")
        return None

def get_weather_forecast():
    api_key = "d3d4325ff5f6d3a19c6d2108de9bdf48"
    city = "Irvine"
    weather = get_weather(api_key, city)
    if weather:
        # Create a new window for displaying weather information
        forecast_window = tk.Toplevel(root)
        forecast_window.title(f"Weather Forecast for {city}")

        # Create subplots for temperature, humidity, and wind speed
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        # Plot temperature, humidity, and wind speed
        labels = ['Temperature', 'Humidity', 'Wind Speed']
        values = [weather['temperature'], weather['humidity'], weather['wind_speed']]
        axs[0].bar(labels, values)
        axs[0].set_title('Weather Metrics')
        axs[0].set_ylabel('Value')

        # Plot weather description
        axs[1].pie([1], labels=[weather['description']], autopct='%1.1f%%')
        axs[1].set_title('Weather Description')

        # Show plots
        plt.tight_layout()
        plt.show()

    else:
        messagebox.showerror("Error", "Weather data not available.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Weather Forecast")

# Create a button to get weather forecast
get_forecast_button = tk.Button(root, text="Get Weather Forecast", command=get_weather_forecast)
get_forecast_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
