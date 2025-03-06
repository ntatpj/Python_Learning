#Import tkinter library
from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
#Define the function to close the window
def change_text():
   label.configure(text="Welcome")
#Create a label
label=Label(win, text= "Click the below button to Change this Text", font=('Aerial 20 bold'))
label.pack(pady=30)
#Create a button widget
button= ttk.Button(win, text="Commit",command=lambda:change_text())
button.pack()
win.mainloop()
