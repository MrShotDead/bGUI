from tkinter import *

screen = Tk()
screen.geometry("600x700")
screen.title("Basics")
screen.configure(background="black")

#Widgets
login = Label(screen, text="Trinket", fg="yellow", bg="black", font="helvetica 30 bold underline").place(x=300, y=20, anchor="center")
Label (screen, text="Enter Username:" ,fg="red", bg="black", font="helvetica 18").place(x= 50, y=100)
username = Entry(screen)
username.place(x=260, y=107)
Button(screen, text = "Are you sure?", fg="red", bg="black", font="helvetica 20").place(x= 400, y=207)
screen.mainloop()