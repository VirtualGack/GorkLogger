import tkinter as tk
import datetime

root = tk.Tk()

root.geometry("500x250")
root.title("GorkLogger")
root.config(bg="#121210")

now = datetime.datetime.now()
print(now)

date = datetime.date.today()
print(date)

file_title = f'call_log_{date}'
print(file_title)

root.mainloop()