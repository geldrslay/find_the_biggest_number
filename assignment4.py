
# Assignment 4. Finding the largest number among the three numbers entered by the user using only if-else statement.

import customtkinter 
from tkinter import * 
from tkinter import messagebox

# Create main window. 

window=customtkinter.CTk ()
window.title("Game Time!")
window.geometry("866x500")
window.configure(bg="#FFFFFF")
window.resizable (False, False)

image = PhotoImage(file="bg.png")
Label (window, image=image,border =0,bg="#FFFFFF").place(x=0, y=-40)

# Determine fonts to be used. 

font1= ("Cooper Black", 120)
font2= ("Fixedsys",22)
font3= ("Fixedsys",30)
font4= ("Fixedsys",50)

# Create window's main page/start page. 

def start ():

    heading.destroy()
    subheading.destroy ()
    start_button.destroy()

    game ()

heading= Label(window, text="GAME TIME!", fg ="#2D3250",bg="#FFFFFF", font=font1) 
heading.place(x=125, y=140)

subheading = Label(window, text="Let us find the largest among any number of your choice.", fg ="#2D3250",bg="#FFFFFF", font=font2) 
subheading.place (x=190, y=340)

start_button=customtkinter.CTkButton(window, command =start, text="START", font=font3,fg_color="#FFFFFF", bg_color="#FFFFFF",text_color="#2D3250", border_width=2, border_color="#2D3250", hover_color="#C499F3")
start_button.place(x=358, y=280)

# Create page where the numbers will be inserted by the user. 

def game ():

    instruction = Label(window, text="Enter three numbers on each corresponding box then press calculate.", fg ="#2D3250",bg="#FFFFFF", font=font2) 
    instruction.place (x=110, y=125)

    first_number_entry= customtkinter.CTkEntry (window, font=font4, text_color="#2D3250",justify="center", fg_color="#FFFFFF", bg_color="#2D3250", border_width=2, width=180, height=150)
    first_number_entry.place(x=110, y=135)

    second_number_entry= customtkinter.CTkEntry (window, font=font4,  text_color="#2D3250",justify="center", fg_color="#FFFFFF", bg_color="#2D3250", border_width=2, width=180, height=150)
    second_number_entry.place(x=340, y=135)

    third_number_entry= customtkinter.CTkEntry (window, font=font4,  text_color="#2D3250",justify="center", fg_color="#FFFFFF", bg_color="#2D3250", border_width=2, width=180, height=150)
    third_number_entry.place(x=570, y=135)

    calculate_button=customtkinter.CTkButton(window, text="CALCULATE", font=font3,fg_color="#FFFFFF", bg_color="#FFFFFF",text_color="#2D3250", border_width=2, border_color="#2D3250", hover_color="#C499F3")
    calculate_button.place(x=327, y=320)

    exit_button=customtkinter.CTkButton(window, text="EXIT", font=font3,fg_color="#FFFFFF", bg_color="#FFFFFF",text_color="#2D3250", border_width=2, border_color="#2D3250", hover_color="#C499F3")
    exit_button.place(x=590, y=320)

    try_again_button=customtkinter.CTkButton(window, text="AGAIN", font=font3,fg_color="#FFFFFF", bg_color="#FFFFFF",text_color="#2D3250", border_width=2, border_color="#2D3250", hover_color="#C499F3")
    try_again_button.place(x=135, y=320)



    
    
   










window.mainloop()
