from weather import *
import tkinter as tk
from user_db import *


root = tk.Tk()
root.title("Weather App")

def register():
    username = username_entry.get()
    password = password_entry.get()
    insert_user(username, password)


def login():
    username = username_entry.get()
    password = password_entry.get()
    if(check_password(username, password)):
        weather_frame.grid(row=0, column=0)
        login_frame.grid_forget()
    error_message.config(text="Invalid Password / Username")

def update_weather():
    city = city_entry.get()
    weather_txt = get_weather(city)
    weather_label.config(text=weather_txt)

# --------------------------LOGIN FRAME --------------------------
login_frame = tk.Frame(root)

username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0, padx=20, pady=20)

password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0, padx=20, pady=20)

username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=20, pady=20)

password_entry = tk.Entry(login_frame)
password_entry.grid(row=1, column=1, padx=20, pady=20)

register_button = tk.Button(login_frame, text="Register", command=register)
register_button.grid(row=2, column=0, padx=10, pady=10)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, column=1, padx=10, pady=10)

error_message = tk.Label(login_frame, text="", fg="red")
error_message.grid(row = 3, column=1, padx=10, pady=10)


# --------------------------WEATHER FRAME --------------------------
weather_frame = tk.Frame(root)

city_label = tk.Label(weather_frame, text="Enter city name:")
city_label.grid(row=0, column=0, padx=20, pady=20)

city_entry = tk.Entry(weather_frame)
city_entry.grid(row=0, column=1, padx=20, pady=20)

get_weather_button = tk.Button(weather_frame, text="Get Weather", command=update_weather)
get_weather_button.grid(row=1, column=1, padx=10, pady=10)

weather_label = tk.Label(weather_frame, text="", wraplength=200)
weather_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

login_frame.grid(row=0, column=0)
root.mainloop()
