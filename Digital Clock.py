from tkinter import Label, Tk
import time

appWindow = Tk()
appWindow.title("Python Dijital Clock")
appWindow.geometry("500x100")
appWindow.resizable(1,1)

text = ("Roboto",80,"bold")
background = "#000000"
foreground = "#f1f1f1"
border = 30

label = Label(appWindow,font=text,bg=background,fg=foreground,bd=border)
label.grid(row=0,column=1)

def digitalClock():
    liveTime = time.strftime("%H:%M:%S")
    label.config(text=liveTime)
    label.after(200,digitalClock)
digitalClock()
appWindow.mainloop()    