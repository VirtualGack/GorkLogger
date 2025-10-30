import tkinter as tk
import datetime

root = tk.Tk()

### screen config ###

root.geometry("550x250")
root.title("GorkLogger")
root.config(bg="#121210")

### set variables ###

now = datetime.datetime.now() #sets the current date and time when calld.
#print(now)

current_time = now.strftime("%H:%M:%S") #seperates the time from now into HH:MM:SS.
# print(current_time)

date = datetime.date.today() # seperates the date from now.
# print(date)

file_title = f'call_log_{date}' #will be used to set the name of the txt file.
# print(file_title)

### main script ###

caller_question = tk.Label(root, text="Caller =>", font=("Helvetica", 18) )
caller_question.grid(row= 0, column= 0, pady=5, padx=10)

caller_answer = tk.Entry(root, font=("Helvetica", 18), width=31)
caller_answer.grid(row= 0, column= 1, pady=5, padx= 10)

notes = tk.Text(root, font=("Helvetica", 15), height= 5)
notes.grid(row= 1, column= 0)



root.mainloop()