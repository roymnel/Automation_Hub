# Password Generator GUI
import tkinter as tk
import random
import string

def generate_password():
    length = 12
    charset = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(charset) for _ in range(length))
    entry.delete(0, tk.END)
    entry.insert(0, password)

app = tk.Tk()
app.title("Password Generator")
app.geometry("300x120")

entry = tk.Entry(app, width=30)
entry.pack(pady=10)

btn = tk.Button(app, text="Generate Password", command=generate_password)
btn.pack()

app.mainloop()
