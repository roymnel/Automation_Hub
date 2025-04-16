# Task Timer GUI
import tkinter as tk
import time

def start_timer():
    start = time.time()
    def update():
        elapsed = int(time.time() - start)
        label.config(text=f"Time: {elapsed} sec")
        app.after(1000, update)
    update()

app = tk.Tk()
app.title("Task Timer")
app.geometry("200x100")
label = tk.Label(app, text="Time: 0 sec")
label.pack(pady=10)
tk.Button(app, text="Start", command=start_timer).pack()
app.mainloop()
