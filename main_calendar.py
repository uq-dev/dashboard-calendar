import tkinter as tk
from tkinter import ttk
import calendar
import datetime

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Dashboard")
        self.geometry("560x720")
        self.configure(bg="black")

        self.current_year = datetime.date.today().year
        self.current_month = datetime.date.today().month

        # 日付と時刻ラベル
        self.time_label = tk.Label(self, font=("Helvetica", 40), fg="green", bg="black")
        self.time_label.pack(pady=10)

        # 現在の月のカレンダーのフレーム
        self.current_month_frame = tk.Frame(self, bg="black")
        self.current_month_frame.pack(pady=10)

        # 翌月のカレンダーのフレーム
        self.next_month_frame = tk.Frame(self, bg="black")
        self.next_month_frame.pack(pady=10)

        self.update_time()
        self.update_calendar()

    def update_time(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=now)
        self.after(1000, self.update_time)

    def update_calendar(self):
        # 現在の月のカレンダーの更新
        self.update_single_calendar(self.current_month_frame, self.current_year, self.current_month)

        # 翌月の年月を計算
        if self.current_month == 12:
            next_month = 1
            next_year = self.current_year + 1
        else:
            next_month = self.current_month + 1
            next_year = self.current_year
        
        # 翌月のカレンダーの更新
        self.update_single_calendar(self.next_month_frame, next_year, next_month)

    def update_single_calendar(self, frame, year, month):
        # 既存のウィジェットを削除
        for widget in frame.winfo_children():
            widget.destroy()

        # 月の表示
        month_label = tk.Label(frame, text=f"{year}-{month:02d}", font=("Helvetica", 24), fg="white", bg="black")
        month_label.pack()

        # 曜日ラベルの表示
        days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        weekday_frame = tk.Frame(frame, bg="black")
        weekday_frame.pack()

        for day in days_of_week:
            day_label = tk.Label(weekday_frame, text=day, font=("Courier", 24), fg="white", bg="black")
            day_label.pack(side="left", padx=5)

        today = datetime.date.today()
        cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
        month_days = cal.monthdayscalendar(year, month)

        # カレンダーの日付を表示
        for week in month_days:
            week_str = ""
            for day in week:
                if day == 0:
                    week_str += "   "  # 空白日のスペース
                elif day == today.day and year == today.year and month == today.month:
                    week_str += f"[{day:2d}]"  # 今日の日付にマークを付ける
                else:
                    week_str += f" {day:2d} "
            week_label = tk.Label(frame, text=week_str, font=("Courier", 24), fg="white", bg="black")
            week_label.pack()

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
