# Simple Text Editor GUI
import tkinter as tk
from tkinter import filedialog

def open_file():
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, 'r') as file:
            content = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, 'w') as file:
            file.write(text_area.get("1.0", tk.END))

app = tk.Tk()
app.title("Text Editor")
app.geometry("500x400")

text_area = tk.Text(app, wrap=tk.WORD)
text_area.pack(expand=True, fill="both")

frame = tk.Frame(app)
frame.pack()

tk.Button(frame, text="Open", command=open_file).pack(side=tk.LEFT, padx=10, pady=5)
tk.Button(frame, text="Save", command=save_file).pack(side=tk.LEFT, padx=10, pady=5)

app.mainloop()
