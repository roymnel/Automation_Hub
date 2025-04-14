# main.py
# Admin GUI Dashboard for Automation Hub

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import time

class AutomationHubAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("Automation Hub – Admin Dashboard")
        self.root.geometry("1200x700")
        self.root.configure(bg="#1e1e1e")

        # Header
        header = tk.Label(root, text="AUTOMATION HUB ADMIN DASHBOARD", font=("Segoe UI", 20, "bold"),
                          bg="#1e1e1e", fg="#00bfff", pady=10)
        header.pack()

        # Tabs
        self.tabs = ttk.Notebook(root)
        self.tabs.pack(expand=True, fill="both", padx=10, pady=10)

        self.create_dashboard_tab()
        self.create_controls_tab()
        self.create_logs_tab()
        self.create_footer()

    def create_dashboard_tab(self):
        dashboard_tab = tk.Frame(self.tabs, bg="#2c2c2c")
        self.tabs.add(dashboard_tab, text="Live Overview")

        self.status_label = tk.Label(dashboard_tab, text="System Idle", font=("Segoe UI", 14),
                                     bg="#2c2c2c", fg="white")
        self.status_label.pack(pady=20)

        self.revenue_label = tk.Label(dashboard_tab, text="Revenue This Month: $0.00", font=("Segoe UI", 16, "bold"),
                                      bg="#2c2c2c", fg="#00ff7f")
        self.revenue_label.pack(pady=10)

        self.active_services = tk.Label(dashboard_tab, text="Active Services: 0", font=("Segoe UI", 14),
                                        bg="#2c2c2c", fg="white")
        self.active_services.pack(pady=5)

    def create_controls_tab(self):
        controls_tab = tk.Frame(self.tabs, bg="#2c2c2c")
        self.tabs.add(controls_tab, text="Tools & Scripts")

        tk.Button(controls_tab, text="Run Google Trends Scan", command=self.mock_scan,
                  bg="#1e90ff", fg="white", font=("Segoe UI", 12), width=30).pack(pady=10)

        tk.Button(controls_tab, text="Update Services Page", command=self.mock_update_services,
                  bg="#32cd32", fg="white", font=("Segoe UI", 12), width=30).pack(pady=10)

        tk.Button(controls_tab, text="Sync SEO Keywords", command=self.mock_seo_sync,
                  bg="#ff8c00", fg="white", font=("Segoe UI", 12), width=30).pack(pady=10)

    def create_logs_tab(self):
        logs_tab = tk.Frame(self.tabs, bg="#2c2c2c")
        self.tabs.add(logs_tab, text="System Logs")

        self.log_output = tk.Text(logs_tab, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 11), wrap="word")
        self.log_output.pack(expand=True, fill="both", padx=10, pady=10)

    def create_footer(self):
        self.status_bar = tk.Label(self.root, text="Ready", bd=1, relief="sunken", anchor="w",
                                   bg="#1e1e1e", fg="#808080", font=("Segoe UI", 10))
        self.status_bar.pack(side="bottom", fill="x")

    def update_status(self, message):
        self.status_bar.config(text=message)
        self.log_output.insert("end", f"[LOG] {message}\n")
        self.log_output.see("end")

    def mock_scan(self):
        self.run_threaded_task("Scanning Google Trends...", 3)

    def mock_update_services(self):
        self.run_threaded_task("Updating services based on pain points...", 4)

    def mock_seo_sync(self):
        self.run_threaded_task("Syncing SEO keywords...", 2)

    def run_threaded_task(self, message, duration):
        def task():
            self.update_status(message)
            self.status_label.config(text=message)
            time.sleep(duration)
            self.update_status(f"{message} Done.")
            self.status_label.config(text="System Idle")
        threading.Thread(target=task).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationHubAdmin(root)
    root.mainloop()
