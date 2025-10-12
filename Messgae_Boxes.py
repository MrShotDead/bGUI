from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

screen = Tk()
screen.geometry("600x700")
screen.title("Message Box")
screen.configure(background="black")

def display_messages():
    messagebox.showinfo("info", "This is an ingo box.")
    messagebox.showwarning("warning", "This is an warning box.")
    messagebox.showerror("error", "This is an error box.")
    answer_1 = messagebox.askquestion("Question?", "Do you like python?")
    print(answer_1)
    answer_2 = messagebox.askokcancel("Ok Cancel", "Would you like to proceed?")
    print (answer_2)
    answer_3 = messagebox.askyesno("Yes No", "Are you sure?")
    print (answer_3)
    answer_4 = messagebox.askretrycancel("Ask Retry Cancel", "Would you like to restart??")
    print (answer_4)
    if answer_4:
        file = filedialog.askopenfile(mode="r", filetypes=[("Python files", "*.py"), ("HTML files", "*.html"), ("All Files", "*.*")])
        if file is not None:
            data = file.read()
            print (data)
    if answer_3:
        file=[("Python files", "*.py"), ("HTML files", "*.html"), ("All Files", "*.*")]
        s=filedialog.asksaveasfile(filetypes=file, defaultextension=file)
        print (s)
        a=filedialog.askopenfiles

Button(screen, text="Start", command=display_messages).place(x=240, y=100)

screen.mainloop()