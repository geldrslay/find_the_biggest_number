
# Assignment 4. Finding the largest number among the three numbers entered by the user.
# Ask user to input 3 numbers. 
# Determine and display the largest among the three numbers.

import customtkinter 
from tkinter import * 
from tkinter import messagebox

# Main Window

window=customtkinter.CTk ()
window.title("Game Time!")
window.geometry("866x500")
window.configure(bg="#FFFFFF")
window.resizable (False, False)

# Background

image = PhotoImage(file="bg.png")
Label (window, image=image,border =0,bg="#FFFFFF").place(x=0, y=-40)

# Fonts

font1= ("Cooper Black", 120)
font2= ("Fixedsys",22)
font3= ("Fixedsys",30)

# Title Page

heading= Label(window, text="GAME TIME!", fg ="#2D3250",bg="#FFFFFF", font=font1) 
heading.place(x=125, y=140)

subheading = Label(window, text="Let us find the highest among any number of your choice.", fg ="#2D3250",bg="#FFFFFF", font=font2) 
subheading.place (x=190, y=340)

start_button=customtkinter.CTkButton(window, text="START", font=font3,fg_color="#FFFFFF", bg_color="#FFFFFF",text_color="#2D3250", border_width=2, border_color="#2D3250", hover_color="#C499F3").place(x=358, y=280)

window.mainloop()
