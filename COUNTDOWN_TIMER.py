import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")

        # Create the timer display
        self.timer_label = tk.Label(root, textvariable=self.time_var, font=("Arial", 48), bg="black", fg="white")
        self.timer_label.pack(pady=20)

        # Entry fields for hours, minutes, and seconds
        tk.Label(root, text="Hours:").pack()
        self.hours_entry = tk.Entry(root, width=3)
        self.hours_entry.pack()

        tk.Label(root, text="Minutes:").pack()
        self.minutes_entry = tk.Entry(root, width=3)
        self.minutes_entry.pack()

        tk.Label(root, text="Seconds:").pack()
        self.seconds_entry = tk.Entry(root, width=3)
        self.seconds_entry.pack()

        # Start button
        self.start_button = tk.Button(root, text="Start Countdown", command=self.start_countdown)
        self.start_button.pack(pady=20)

        # Stop button
        self.stop_button = tk.Button(root, text="Stop Countdown", command=self.stop_countdown)
        self.stop_button.pack(pady=10)
        self.stop_button.config(state=tk.DISABLED)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset Timer", command=self.reset_timer)
        self.reset_button.pack(pady=10)
        self.reset_button.config(state=tk.DISABLED)

        self.running = False
        self.time_left = 0

    def start_countdown(self):
        try:
            hours = int(self.hours_entry.get() or 0)
            minutes = int(self.minutes_entry.get() or 0)
            seconds = int(self.seconds_entry.get() or 0)

            self.time_left = hours * 3600 + minutes * 60 + seconds

            if self.time_left <= 0:
                messagebox.showerror("Invalid Time", "Please enter a valid countdown time.")
                return

            self.running = True
            self.update_timer()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for hours, minutes, and seconds.")

    def update_timer(self):
        if self.running:
            if self.time_left > 0:
                mins, secs = divmod(self.time_left, 60)
                hours, mins = divmod(mins, 60)
                self.time_var.set(f"{hours:02}:{mins:02}:{secs:02}")
                self.time_left -= 1
                self.root.after(1000, self.update_timer)
            else:
                self.time_var.set("00:00:00")
                messagebox.showinfo("Time's up!", "The countdown has finished.")
                self.stop_countdown()

    def stop_countdown(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)

    def reset_timer(self):
        self.time_var.set("00:00:00")
        self.hours_entry.delete(0, tk.END)
        self.minutes_entry.delete(0, tk.END)
        self.seconds_entry.delete(0, tk.END)
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
