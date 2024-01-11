
# Assignment 4. Finding the largest number among the three numbers entered by the user.
# Ask user to input 3 numbers. 
# Determine and display the largest among the three numbers.

import customtkinter 
from tkinter import * 
from tkinter import messagebox

# Main Window

window=customtkinter.CTk ()
window.title("Figure Out Numbers with Issa!")
window.geometry("900x500")
window.configure(bg="#86A7FC")
window.resizable (False, False)



#Background

background = PhotoImage(file="bg.png")
background = Label (window,image = image, border=0, bg= "#86A7FC")
background.place(x= 0, y=50)
# Fonts 

window.mainloop()
