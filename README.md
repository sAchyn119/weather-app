## Weather App - Python Project
## Description

This project is a Python-based Weather App with two modes:

# Beginner Mode (CLI)
A simple command-line interface where users can input a city name to get the current weather, including:

Temperature (°C)

Humidity (%)

Weather condition (description)

# Advanced Mode (GUI)
A graphical user interface built with Tkinter that displays:

Temperature (°C or °F)

Humidity (%)

Wind speed (m/s)

Weather condition (description)

Weather icon

Unit toggle between Celsius and Fahrenheit

This project demonstrates practical skills in API integration, user input handling, GUI development, error handling, and data visualization.

# Summary of Key Imports

requests: To make HTTP requests and fetch weather data from OpenWeatherMap API

tkinter: To create the GUI interface

messagebox (from tkinter): To display error messages

BytesIO (from io) and Image, ImageTk (from PIL): To handle and display weather icons

# Features

Fetch real-time weather data using OpenWeatherMap API

CLI mode for beginner users

GUI mode with:

Input box for city

Weather icon display

Temperature, humidity, wind speed, and condition

Unit conversion between °C and °F

Error handling for invalid city names or connection issues

Menu to switch between CLI and GUI without restarting

# Installation

Clone the repository:
https://github.com/sAchyn119/weather-app.git


# Usage

Run the Python file:

python weather_app.py


# Choose mode:

1 → CLI Beginner mode

2 → GUI Advanced mode

3 → Exit program

In GUI mode, enter a city name and click Get Weather.

Toggle between Celsius and Fahrenheit using the Switch Unit button.

# CLI Mode Example:

Weather in London:
Temperature: 18°C
Humidity: 70%
Condition: Clear sky

Author
sachin yadav
