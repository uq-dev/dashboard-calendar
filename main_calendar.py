import tkinter as tk
from tkinter import ttk
import calendar
import datetime

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Dashboard")
        self.geometry("300x400")
        self.configure(bg="black")
        
        self.current_year = datetime.date.today().year
        self.current_month = datetime.date.today().month

        # 日付と時刻ラベル
        self.time_label = tk.Label(self, font=("Helvetica", 40), fg="green", bg="black")
        self.time_label.pack(pady=10)

        # 前月、表示中の年月、翌月のボタンフレーム
        self.nav_frame = tk.Frame(self, bg="black")
        self.nav_frame.pack(pady=5)

        self.prev_button = tk.Button(self.nav_frame, text="<", command=self.prev_month, font=("Helvetica", 14))
        self.prev_button.pack(side="left")

        self.month_label = tk.Label(self.nav_frame, font=("Helvetica", 14), fg="white", bg="black")
        self.month_label.pack(side="left", padx=20)

        self.next_button = tk.Button(self.nav_frame, text=">", command=self.next_month, font=("Helvetica", 14))
        self.next_button.pack(side="left")

        # カレンダーのフレーム
        self.calendar_frame = tk.Frame(self, bg="black")
        self.calendar_frame.pack(pady=10)

        self.update_time()
        self.update_calendar()

    def update_time(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=now)
        self.after(1000, self.update_time)

    def update_calendar(self):
        # 既存のウィジェットを削除
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        # 年月を表示
        self.month_label.config(text=f"{self.current_year}-{self.current_month:02d}")

        today = datetime.date.today()
        cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
        month_days = cal.monthdayscalendar(self.current_year, self.current_month)

        # カレンダーの日付を中央寄せで表示
        for week in month_days:
            week_str = ""
            for day in week:
                if day == 0:
                    week_str += "   "  # 空白日のスペース
                elif day == today.day and self.current_year == today.year and self.current_month == today.month:
                    week_str += f"[{day:2d}]"  # 今日の日付にマークを付ける
                else:
                    week_str += f" {day:2d} "
            week_label = tk.Label(self.calendar_frame, text=week_str, font=("Courier", 14), fg="white", bg="black")
            week_label.pack()

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.update_calendar()

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.update_calendar()

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
