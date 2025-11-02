import tkinter as tk
import tkinter.font as tkFont
import datetime

root = tk.Tk()

### screen config ###

root.geometry("500x250") # sets screen size
root.title("GorkLogger") # sets the title of the app
root.config(bg="#09330d") #sets the root background colour
root.resizable(False, False) #prevents wuindow from being resized

### set variables ###

now = datetime.datetime.now() #sets the current date and time when calld.
current_time = now.strftime("%H:%M:%S") #seperates the time from now into HH:MM:SS.
date = datetime.date.today() # seperates the date from now.
file_title = f'call_log_{date}.txt' #will be used to set the name of the txt file.
font = tkFont.Font(family="Comfortaa", size=18) #sets the font uniform across the app
callerid = "" #sets callerid as an empty string

### Function Script ###

def save_text():
    now = datetime.datetime.now() #setsnow as the current date and time when function is called
    current_time = now.strftime("%H:%M:%S") #sets the formate for the current time
    notes_string = notes.get("1.0", "end-1c") # converts the text from notes into a string that can be saved to file.
    callerid = caller_answer.get() # gets the string value of the caller entry to save to file.
    with open(file_title, 'a',) as file: # opens file ready to be added to (a for append) and creates file if it doesn't exist.
        file.write(f"\n### {current_time} ###\n{callerid}\n{notes_string}\n") # stamps current time, line break(lb) stamps caller ID, lb adds the call notes to the txt file
        caller_answer.delete(0, tk.END) # deletes the text in caller ID box ready for next call
        notes.delete("1.0", tk.END) # deletes the text in notes box ready for next call
        file.close() # closes the file when we are finished.

### GUI layout ###

root.columnconfigure(0, weight=1) 
root.rowconfigure(0, weight=1)

frame = tk.Frame(root, bg="#09330d")
frame.grid(row= 0, column= 0, sticky="nsew")

frame.columnconfigure(0, weight= 1)
frame.columnconfigure(1, weight= 1)
frame.rowconfigure(0, weight= 1)
frame.rowconfigure(1, weight=4)

caller_question = tk.Label(frame, text="Caller =>",  bg="#9cbda1", font=font)
caller_question.grid(row= 0, column= 0, sticky="nsew", pady=5, padx=5)

caller_answer = tk.Entry(frame, bg="#f7f7e8", fg="#09330d", font=font, textvariable= callerid)
caller_answer.grid(row= 0, column= 1, sticky="nsew", pady=5, padx= 10)

notes = tk.Text(root,  height=8, bg="#f7f7e8", fg="#09330d", font=font)
notes.grid(row= 1, column= 0, columnspan=2, sticky="nsew")

submit_btn = tk.Button(root, text="End Call", font=font, bg="#09330D", fg="#9cbda1", command=save_text )
submit_btn.place(rely=1.0, relx=1.0, anchor=tk.SE)

root.mainloop()