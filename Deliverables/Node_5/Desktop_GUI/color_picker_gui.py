# GUI Color Picker
import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color = colorchooser.askcolor(title="Choose a color")
    if color[1]:
        label.config(text=f"Selected: {color[1]}", bg=color[1])

app = tk.Tk()
app.title("Color Picker")
app.geometry("300x150")

label = tk.Label(app, text="Click below to pick a color", font=("Arial", 12))
label.pack(pady=20)

tk.Button(app, text="Pick Color", command=pick_color).pack(pady=5)

app.mainloop()
