
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

font1= ("Cooper Black", 70)
font2= ("Fixedsys",18)
font3= ("Fixedsys",25)
font4= ("Fixedsys",30)
font5= ("Cooper Black", 40)

# Determine functions to be used. 

    


def entry_validation(): 
    if any (entry == "" for entry in (first_number_entry.get(), second_number_entry.get(), third_number_entry.get())):
        messagebox.showerror("Oops!", "Kindly fill out all required fields.")
        return
    try:
        first_number= float(first_number_entry.get())
        second_number=float(second_number_entry.get())
        third_number=float(third_number_entry.get())
    
    except ValueError:
        messagebox.showerror("Oops!", "Please enter numerical values only.")
        return
    
    def calculate_highest_number(first_number, second_number, third_number):
        if first_number> second_number and first_number > third_number:
            return first_number
        elif second_number>= first_number and second_number>= third_number:
            return second_number
        else:
            return third_number
    
    highest_number = calculate_highest_number(first_number, second_number, third_number)
    number_text_label.configure(text="The highest number is:", font=('Helvetica', 15))
    highest_number_label.configure(text=(highest_number), font=('Helvetica', 30, 'bold'), text_color="#D21404")

def try_again():
    first_number_entry.delete(0, END)
    second_number_entry.delete(0, END)
    third_number_entry.delete(0, END)
    number_text_label.configure(text="")
    highest_number_label.configure(text="")

number_text_label = customtkinter.CTkLabel(window, text="")
number_text_label.place(relx=0.5, rely=0.4, anchor=CENTER)

highest_number_label = customtkinter.CTkLabel(window, text="")
highest_number_label.place(relx=0.5, rely=0.65, anchor=CENTER)



    

# Create corresponding buttons for each function.

calculate_button=customtkinter.CTkButton(window, command= entry_validation, text="CALCULATE", font=font3,fg_color="#FFFFFF", bg_color="#FFFFFF",text_color="#2D3250", border_width=2, border_color="#2D3250", hover_color="#C499F3")
calculate_button.place(x=360, y=350)

exit_button=customtkinter.CTkButton(window, text="EXIT", font=font3,fg_color="#FFFFFF", bg_color="#FFFFFF",text_color="#2D3250", border_width=2, border_color="#2D3250", hover_color="#C499F3")
exit_button.place(x=590, y=350)

try_again_button=customtkinter.CTkButton(window, command= try_again, text="AGAIN", font=font3,fg_color="#FFFFFF", bg_color="#FFFFFF",text_color="#2D3250", border_width=2, border_color="#2D3250", hover_color="#C499F3")
try_again_button.place(x=135, y=350)


# Create window's heading. 

heading= Label(window, text="GAME TIME!", fg ="#2D3250",bg="#FFFFFF", font=font1) 
heading.place(x=380, y=95)

subheading = Label(window, text="Let us help you find the highest amongst any number of your choice.", fg ="#2D3250",bg="#FFFFFF", font=font2) 
subheading.place (x=110, y=210)

# Create part where the numbers will be inserted by the user. 

first_number_entry= customtkinter.CTkEntry (window, font=font4, text_color="#2D3250",justify="center", fg_color="#FFFFFF", bg_color="#2D3250", border_width=2, width=180, height=60)
first_number_entry.place(x=110, y=190)

second_number_entry= customtkinter.CTkEntry (window, font=font4,  text_color="#2D3250",justify="center", fg_color="#FFFFFF", bg_color="#2D3250", border_width=2, width=180, height=60)
second_number_entry.place(x=340, y=190)

third_number_entry= customtkinter.CTkEntry (window, font=font4,  text_color="#2D3250",justify="center", fg_color="#FFFFFF", bg_color="#2D3250", border_width=2, width=180, height=60)
third_number_entry.place(x=570, y=190)




    
    
   










window.mainloop()
