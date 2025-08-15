import requests
import tkinter as tk
from tkinter import messagebox
from io import BytesIO
from PIL import Image, ImageTk


API_KEY = "957e31204a0617d520aaae75788591e4"  
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# BEGINNER 
def beginner_cli():
    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        res = requests.get(API_URL, params=params, timeout=5)
        data = res.json()
        if res.status_code != 200:
            print("Error:", data.get("message", "Unable to fetch weather."))
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]

        print(f"\nWeather in {city.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {desc.capitalize()}\n")

    except requests.exceptions.RequestException:
        print("Error: Unable to connect to the weather service.")

# ADVANCED (GUI)
class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")
        master.geometry("350x400")

        self.unit_celsius = True

        # City input
        tk.Label(master, text="Enter City:", font=("Arial", 12)).pack(pady=5)
        self.city_entry = tk.Entry(master, font=("Arial", 12))
        self.city_entry.pack(pady=5)

        # Search button
        tk.Button(master, text="Get Weather", command=self.fetch_weather, font=("Arial", 12)).pack(pady=5)

        # Unit toggle
        self.unit_btn = tk.Button(master, text="Switch to °F", command=self.toggle_unit)
        self.unit_btn.pack(pady=5)

        # Weather display
        self.weather_label = tk.Label(master, font=("Arial", 12))
        self.weather_label.pack(pady=5)

        # Weather icon
        self.icon_label = tk.Label(master)
        self.icon_label.pack()

    def toggle_unit(self):
        self.unit_celsius = not self.unit_celsius
        self.unit_btn.config(text="Switch to °C" if not self.unit_celsius else "Switch to °F")
        self.fetch_weather()

    def fetch_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showerror("Error", "City name cannot be empty")
            return

        units = "metric" if self.unit_celsius else "imperial"
        try:
            res = requests.get(API_URL, params={"q": city, "appid": API_KEY, "units": units}, timeout=5)
            data = res.json()

            if res.status_code != 200:
                messagebox.showerror("Error", data.get("message", "Unable to fetch weather."))
                return

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            desc = data["weather"][0]["description"]
            wind = data["wind"]["speed"]
            icon_code = data["weather"][0]["icon"]

            self.weather_label.config(
                text=f"Temperature: {temp}°{'C' if self.unit_celsius else 'F'}\n"
                     f"Humidity: {humidity}%\n"
                     f"Condition: {desc.capitalize()}\n"
                     f"Wind Speed: {wind} m/s"
            )

            # Load icon
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            icon_res = requests.get(icon_url)
            img_data = Image.open(BytesIO(icon_res.content))
            img_tk = ImageTk.PhotoImage(img_data)
            self.icon_label.config(image=img_tk)
            self.icon_label.image = img_tk

        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "Unable to connect to the weather service.")

# MAIN 
if __name__ == "__main__":
    while True:
        print("\nChoose Mode:")
        print("1. Beginner (CLI)")
        print("2. Advanced (GUI)")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            beginner_cli()
        elif choice == "2":
            root = tk.Tk()
            root.lift()
            root.attributes('-topmost', True)
            root.after_idle(root.attributes, '-topmost', False)
            app = WeatherApp(root)
            root.mainloop()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
