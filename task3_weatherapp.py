import tkinter as tk
from tkinter import messagebox
import requests
import datetime  # Import the datetime module

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")  # Set the title of the window

        self.create_widgets()  # Call the method to create widgets

    def create_widgets(self):
        # Create label and entry for entering location
        self.location_label = tk.Label(self.root, text="Enter Location:")
        self.location_label.pack()

        self.location_entry = tk.Entry(self.root)
        self.location_entry.pack()

        # Create button to get weather information
        self.get_weather_button = tk.Button(self.root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        # Create label to display weather information
        self.weather_info_label = tk.Label(self.root, text="")
        self.weather_info_label.pack()

    def get_weather(self):
        # Get the location entered by the user
        location = self.location_entry.get()
        if not location:
            messagebox.showerror("Error", "Please enter a location.")
            return

        api_key = "20362339eb365e9833713a824810cf01"  # Use OpenWeatherMap API key to ensure that we can access the weather data or not
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)  # Send a request to the OpenWeatherMap API
            data = response.json()  # Parse the JSON response

            if response.status_code == 200:  # Check if the request was successful
                # Extract temperature and weather description from the response
                temperature = data["main"]["temp"]
                weather_description = data["weather"][0]["description"]

                # Get current date, time, and day
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                current_day = datetime.datetime.now().strftime("%A")

                # Construct weather information string
                weather_info = f"Location: {location}\nDate: {current_date}\nTime: {current_time}\nDay: {current_day}\nTemperature: {temperature}°C\nWeather: {weather_description}"

                # Update the label to display the weather information
                self.weather_info_label.config(text=weather_info)
            else:
                # Display an error message if the request was not successful
                messagebox.showerror("Error", f"Failed to fetch weather data. Error code: {response.status_code}")
        except Exception as e:
            # Display an error message if an exception occurs during the request
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()  # Create the main window
    app = WeatherApp(root)  # Create an instance of the WeatherApp class
    root.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
