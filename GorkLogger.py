import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import datetime

root = tk.Tk()

### screen config ###

root.geometry("700x400") # sets screen size
root.minsize(620, 380)
root.title("Call Logger") # sets the title of the app
root.config(bg="#0C0C0C") #sets the root background colour
root.resizable(True, True) #prevents wuindow from being resized

### theme + style ###

style = ttk.Style(root)
style.theme_use("clam")

FONT_UI = ("Segoe UI", 24)
FONT_TITLE = ("Segoe UI", 24, "bold")

root.option_add("*Font", FONT_UI)

# colour palette
BG = '#0C0C0C'
PANEL ='#481E14'
TEXT_BG ='#0C0C0C'
TEXT_FG ="#ECAB9C"
ACCENT ='#9B3922'

root.configure(bg=BG)

# style tweaks
style.configure("Card.TFrame", background=PANEL)
style.configure("CardTitle.TLabel", background=PANEL, foreground=ACCENT, font=FONT_TITLE)
style.configure("Status.TLabel", background=BG, foreground=ACCENT)
style.configure("Caller.TEntry", fieldbackground=TEXT_BG, background=BG, foreground=TEXT_FG, insertcolor=ACCENT)

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
    caller_answer.focus_set() #sets focus to the caller entry upon submission.

def submit_event(event=None): # adding event to bind to key press
    save_text()

# Key bind ctrl + enter to submit
root.bind("<Control-Return>", submit_event)

### GUI layout ###

# Root grid (3 rows)
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=0)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=0)

# row 1

top = ttk.Frame(root, style="Card.TFrame", padding=12)
top.grid(row=0, column=0, sticky='ew', padx=12, pady=(12, 8))

top.grid_columnconfigure(0, weight=0)
top.grid_columnconfigure(1, weight=1)

caller_question = ttk.Label(top, text="Caller =>", style="CardTitle.TLabel").grid(row=0, column=0, sticky='w', padx=(0, 10))
caller_answer = ttk.Entry(top, textvariable=callerid, style="Caller.TEntry")
caller_answer.grid(row=0, column=1, sticky='ew')

# row 2

mid = ttk.Frame(root, style="Card.TFrame", padding=12)
mid.grid(row=1, column=0, sticky='nsew', padx=12, pady=(0, 8))
mid.grid_columnconfigure(0, weight=1)
mid.grid_rowconfigure(0, weight=1)

notes = tk.Text(mid, wrap="word", bg=TEXT_BG, fg=TEXT_FG, insertbackground=TEXT_FG, bd=0, highlightthickness=0, font=FONT_UI)
notes.grid(row=0, column=0, sticky='nsew')

root.mainloop()