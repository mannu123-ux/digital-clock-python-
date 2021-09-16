from tkinter import*
from tkinter.ttk import*
from time import strftime
window=Tk()
window.title("clock")
window.geometry("500x500")
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000,time)

lbl=Label(window)
lbl.pack()
time()
window.mainloop()

    
