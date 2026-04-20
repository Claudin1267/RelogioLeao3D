import tkinter as tk
from datetime import datetime
import pytz

class TimeZoneClock:
    def __init__(self, master):
        self.master = master
        self.master.title('Digital Clock - Time Zones')
        self.timezones = ['UTC', 'America/New_York', 'Europe/London', 'Asia/Tokyo']
        self.create_widgets()
        self.update_clocks()

    def create_widgets(self):
        self.frames = {}
        for tz in self.timezones:
            frame = tk.Frame(self.master)
            frame.pack(side=tk.LEFT, padx=10, pady=10)
            label = tk.Label(frame, text=tz, font=('Helvetica', 16))
            label.pack()
            time_label = tk.Label(frame, font=('Helvetica', 24))
            time_label.pack()
            self.frames[tz] = time_label

    def update_clocks(self):
        for tz in self.timezones:
            local_time = datetime.now(pytz.timezone(tz)).strftime('%Y-%m-%d %H:%M:%S')
            self.frames[tz]['text'] = local_time
        self.master.after(1000, self.update_clocks)

if __name__ == '__main__':
    root = tk.Tk()
    app = TimeZoneClock(root)
    root.mainloop()