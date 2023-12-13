import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

MAX_ATTEMPTS = 2 
#Error: number of attempts set lower than expected
#BUG:  Button disabled before expected 
#FAILURE: Unusable button after 2 attempt
attempts = 0

def validate_login():
    global attempts
    username = username_entry.get()
    password = password_entry.get()

    if not (username == "user" and password == "password"):
        attempts += 1
        if attempts >= MAX_ATTEMPTS:
            login_button.config(state="disabled")
            login_success_label.config(text="Maximum attempts reached")
            # ERROR: Function missing return statements
            # BUG: Application always display login success
            # FAILURE: User gets login blocked without knowing why
        login_success_label.config(text=f"Invalid username or password. Attempts left: {MAX_ATTEMPTS - attempts}",)
    login_success_label.config(text="Login successful!")

root = tk.Tk()
root.title("Login")
#Window Size
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

frame = tk.Frame(root)
frame.pack(expand=True)
# Username input
username_label = ttk.Label(frame, text="Username:")
username_label.grid(row=0, column=0, pady=5)
username_entry = ttk.Entry(frame)
username_entry.grid(row=0, column=1, pady=5)

# Password input
password_label = ttk.Label(frame, text="Password:")
password_label.grid(row=1, column=0, pady=5)
password_entry = ttk.Entry(frame, show="*")
password_entry.grid(row=1, column=1, pady=5)

# Button
login_button = ttk.Button(frame, text="Login", command=validate_login)
login_button.grid(row=2, columnspan=2, pady=10)

# Error label
login_success_label = ttk.Label(text="")
login_success_label.pack()

# Run the application
root.mainloop()