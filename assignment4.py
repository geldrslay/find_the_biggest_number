
# Assignment 4. Finding the largest number among the three numbers entered by the user.
# Ask user to input 3 numbers. 
# Determine and display the largest among the three numbers.

import customtkinter 
from tkinter import * 
from tkinter import messagebox

# Main Window

window=customtkinter.CTk ()
window.title("What's At Peak?")
window.geometry("866x500")
window.configure(bg="#FFF9C7")
window.resizable (False, False)

# Background

image = PhotoImage(file="bg.png")
Label (window, image=image,border =0,bg="#FFF9C7").place(x=0, y=-40)

# Fonts 

font1=("Showcard Gothic", 130)
font2=("Bell MT", 20,'bold')
font3=("Bell MT", 16,"italic")

# Title

title= Label(window, text="SOLVE WITH AYE!", fg="#3B3486", bg="#FFF9C7",font=font1)





# Frame


window.mainloop()
