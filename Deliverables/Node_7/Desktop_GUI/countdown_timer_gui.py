# Countdown Timer GUI
import tkinter as tk
import time
from threading import Thread

def start_countdown():
    try:
        seconds = int(entry.get())
        def countdown():
            while seconds >= 0:
                mins, secs = divmod(seconds, 60)
                timer_label.config(text=f"{mins:02d}:{secs:02d}")
                app.update()
                time.sleep(1)
                nonlocal seconds
                seconds -= 1
        Thread(target=countdown).start()
    except ValueError:
        timer_label.config(text="Enter valid number!")

app = tk.Tk()
app.title("Countdown Timer")
app.geometry("300x150")

entry = tk.Entry(app, width=15, font=("Arial", 14))
entry.pack(pady=10)
entry.insert(0, "60")  # default to 60 seconds

start_button = tk.Button(app, text="Start", command=start_countdown)
start_button.pack()

timer_label = tk.Label(app, text="00:00", font=("Arial", 32))
timer_label.pack(pady=10)

app.mainloop()
