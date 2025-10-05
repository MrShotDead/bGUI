from tkinter import *
from tkinter.ttk import *
import time

screen = Tk()
screen.geometry("600x700")
screen.title("Basics")
screen.configure(background="teal")

#Creating a menubar
menubar = Menu(screen)
#add menu
file = Menu(menubar)
menubar.add_cascade(label = "File", menu=file)
file.add_command(label = "Save As", command=None)
file.add_command(label = "New", command=None)
file.add_command(label = "Open", command=None)
file.add_separator()
file.add_command(label = "Close", command=exit)

edit = Menu(menubar)
menubar.add_cascade(label = "Edit", menu=edit)
edit.add_command(label = "Cut", command=None)
edit.add_command(label = "Copy", command=None)
edit.add_command(label = "Paste", command=None)
edit.add_separator()
edit.add_command(label = "Undo", command=None)
screen.config(menu=menubar)

#Creating A Spinbox
month = Spinbox(screen, from_="01", to="12")
month.pack(padx=10, pady=5)

#Creating Progress Bar
def Bar():
    while progress_bar["value"]!=100:
        progress_bar["value"]+=50
        time.sleep(1)
progress_bar = Progressbar(screen, length=350, orient=VERTICAL, mode="determinate",)
progress_bar.pack(pady=20)
Button(screen, text="Download bar", command=Bar).pack(pady=50)
screen.mainloop()