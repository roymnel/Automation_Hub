# Simple Checklist GUI App
import tkinter as tk

tasks = []

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        tasks.append(task)
        entry.delete(0, tk.END)

def mark_done():
    selected = listbox.curselection()
    for index in selected:
        listbox.itemconfig(index, fg="gray")
        listbox.selection_clear(0, tk.END)

app = tk.Tk()
app.title("Checklist")
app.geometry("300x350")

entry = tk.Entry(app, width=25)
entry.pack(pady=10)

add_btn = tk.Button(app, text="Add Task", command=add_task)
add_btn.pack()

listbox = tk.Listbox(app, width=40, height=12)
listbox.pack(pady=10)

done_btn = tk.Button(app, text="Mark Done", command=mark_done)
done_btn.pack()

app.mainloop()
