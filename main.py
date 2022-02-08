''' AGE calculator
Source: https://www.askpython.com/python-modules/tkinter/age-calculator
Date: 22/01/2022
'''
#__________ Functions __________#


#__________ Main __________#

import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.config(bg="#00287F")
window.resizable(width=False,height=False)
window.title("Age calculator 2.0")

# Labels for Heading and Subheading of GuI
lb_heading = tk.Label(window,text="The Age calculator 2.0",font=("Arial",20),fg="white",bg="#00287F")

lb_subheading = tk.Label(window,font=("Arial",9),text="Enter your birthday which includes the day, month and year",fg="white",bg="#00287F")





# Labels for date, month and year
#Date
lb_date = tk.Label(window,text = "Date: ",font=('Arial',12,"bold"),
fg="darkgreen",bg="#00287F")
#Month
lb_month = tk.Label(window,text = "Month: ",font=('Arial',12,"bold"),
fg="darkgreen",bg="#00287F")
#Year
lb_year = tk.Label(window,text = "Year: ",font=('Arial',12,"bold"),
fg="darkgreen",bg="#00287F")

# Entry boxes for date, month and year
e_date = tk.Entry(window,width=5)
e_month = tk.Entry(window,width=5)
e_year = tk.Entry(window,width=5)

#Button to calculate age
btn_calculate_age = tk.Button(window,text="Calculate Age",font=("Arial",13), command='get_age')

#label for text box that will display the calculated age
lb_calculated_age = tk.Label(window,text="The calculated age is: ",
font=('Arial',12,"bold"),fg="darkgreen",bg="#00287F")
tbox_age=tk.Text(window,width=5,height=0,state="disabled")

#Button to exit application
btn_exit = tk.Button(window,text="Exit Application",font=("Arial",13), command=exit)

# Placing the elements on the screen
lb_heading.place(x=40,y=5)
lb_subheading.place(x=4,y=40)
lb_date.place(x=100,y=70)
lb_month.place(x=100,y=95)
lb_year.place(x=100,y=120)
e_date.place(x=180,y=70)
e_month.place(x=180,y=95)
e_year.place(x=180,y=120)
btn_calculate_age.place(x=100,y=150)
lb_calculated_age.place(x=10,y=200)
tbox_age.place(x=240,y=200)
btn_exit.place(x=100,y=240)

def get_age():
    #get the 3 entries
    d = int(e_date.get())
    m = int(e_month.get())
    y = int(e_year.get())

    #find the age 
    age = today.year-y-((today.month, today.day)<(m,d))
    tbox_age.config(state= 'normal')

    #age calculated is insert into the text box after clearing th eprevious info in the textbox.
    tbox_age.delete









































