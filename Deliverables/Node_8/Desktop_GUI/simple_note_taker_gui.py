# Simple Note Taker GUI
import tkinter as tk
from tkinter import filedialog

def save_note():
    content = text.get("1.0", tk.END).strip()
    if content:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            status_label.config(text="✅ Note saved.")
    else:
        status_label.config(text="⚠️ Nothing to save.")

app = tk.Tk()
app.title("Note Taker")
app.geometry("400x300")

text = tk.Text(app, wrap=tk.WORD)
text.pack(expand=True, fill="both", padx=10, pady=10)

save_btn = tk.Button(app, text="Save Note", command=save_note)
save_btn.pack(pady=5)

status_label = tk.Label(app, text="", fg="green")
status_label.pack()

app.mainloop()
