# Real-Time Clock Display GUI
import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    app.after(1000, update_clock)

app = tk.Tk()
app.title("Real-Time Clock")
app.geometry("250x100")

label = tk.Label(app, text="", font=("Helvetica", 32))
label.pack(expand=True)

update_clock()
app.mainloop()
