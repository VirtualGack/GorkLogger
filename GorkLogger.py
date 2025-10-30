import tkinter as tk
import tkinter.font as tkFont
import datetime

root = tk.Tk()

### screen config ###

root.geometry("500x250")
root.title("GorkLogger")
root.config(bg="#09330d")
root.resizable(False, False)

### set variables ###

now = datetime.datetime.now() #sets the current date and time when calld.
#print(now)

current_time = now.strftime("%H:%M:%S") #seperates the time from now into HH:MM:SS.
# print(current_time)

date = datetime.date.today() # seperates the date from now.
# print(date)

file_title = f'call_log_{date}' #will be used to set the name of the txt file.
# print(file_title)

font = tkFont.Font(family="Comfortaa", size=18)

### GUI layout ###

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root, bg="#09330d")
frame.grid(row= 0, column= 0, sticky="nsew")

frame.columnconfigure(0, weight= 1)
frame.columnconfigure(1, weight= 1)
frame.rowconfigure(0, weight= 1)
frame.rowconfigure(1, weight=4)

caller_question = tk.Label(frame, text="Caller =>",  bg="#9cbda1", font=font ) #font=("Helvetica", 18)
caller_question.grid(row= 0, column= 0, sticky="nsew", pady=5, padx=5)

caller_answer = tk.Entry(frame, bg="#f7f7e8", fg="#09330d", font=font) #width=31 font=("Helvetica", 18)
caller_answer.grid(row= 0, column= 1, sticky="nsew", pady=5, padx= 10)

notes = tk.Text(root,  height=8, bg="#f7f7e8", fg="#09330d", font=font) #font=("Helvetica", 17)
notes.grid(row= 1, column= 0, columnspan=2, sticky="nsew")

submit_btn = tk.Button(root, text="End Call", font=font, bg="#09330D", fg="#9cbda1")
submit_btn.place(rely=1.0, relx=1.0, anchor=tk.SE)



root.mainloop()