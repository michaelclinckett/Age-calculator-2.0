''' AGE calculator
Source: https://www.askpython.com/python-modules/tkinter/age-calculator
Date: 22/01/2022
'''
#__________ IMPORT __________#
from datetime import date
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

today = date.today()


#__________ Functions __________#
#def get_age():
#    #get the 3 entries
#    d = int(e_date.get())
#    m = int(e_month.get())
#    y = int(e_year.get())
#
#    calc_age = find_age(d, m, y)
#    display_calc_age(calc_age)


def find_age(d, m, y):
    #find the age
    age = today.year - y - ((today.month, today.day) < (m, d))
    tbox_age.config(state='normal')
    return age

def display_calc_age(age):
    tbox_age.config(state='normal')
    #age calculated is insert into the text box after clearing th eprevious info in the textbox.
    tbox_age.delete('1.0', tk.END)
    tbox_age.insert(tk.END, age)
    tbox_age.config(state='disabled')


def exit():
    window.destroy()


def validation():
    #gets the three entries
    d = e_date.get() 
    #m = e_month.get()
    m = month_chosen.current()
    y = e_year.get()

    msg = ''

    if len(d) < 0 or len(y) == 0:
        msg = 'day, month and year can\'t be empty'
    else:
        try:
            if any(ch.isdigit() for ch in d) == False:
                msg = 'Put in a numerical numbers for date to proceed'
            #elif any(ch.isdigit() for ch in m) == False:
            elif m == 0:
                msg = 'Chose a month'
            elif any(ch.isdigit() for ch in y) == False:
                msg = 'Put in a numerical numbers for year to proceed'
            else:
                # msg = 'success!'
                day = int(d) - 1
                                  #month = int(m)
                month = m #month is already in number from list position
                year = int(y)
                if day == 0 or year == 0 or day > 31:        
                  calc_age = find_age(day, month, year)
                  display_calc_age(calc_age)
                  if year > today.year:
                    msg = 'Year cannot be over the current year'
                else:
                  msg = 'Day and year must exist'

        except Exception as ep:
            messagebox.showerror('error', ep)
    if msg != "":
        messagebox.showinfo('message', msg)


#__________ Main __________#

window = tk.Tk()
window.geometry("400x300")
window.config(bg="#00287F")
window.resizable(width=False, height=False)
window.title("Age calculator 2.0")

# Labels for Heading and Subheading of GuI
lb_heading = tk.Label(window,
                      text="The Age calculator 2.0",
                      font=("Arial", 20),
                      fg="white",
                      bg="#00287F")

lb_subheading = tk.Label(
    window,
    font=("Arial", 9),
    text="Enter your birthday which includes the day, month and year",
    fg="white",
    bg="#00287F")

# Labels for date, month and year
#Date
lb_date = tk.Label(window,
                   text="Date: ",
                   font=('Arial', 12, "bold"),
                   fg="darkgreen",
                   bg="#00287F")
#Month
lb_month = tk.Label(window,
                    text="Month: ",
                    font=('Arial', 12, "bold"),
                    fg="darkgreen",
                    bg="#00287F")
#Year
lb_year = tk.Label(window,
                   text="Year(In AC): ",
                   font=('Arial', 12, "bold"),
                   fg="darkgreen",
                   bg="#00287F")

# Entry boxes for date, month and year
e_date = tk.Entry(window, width=5)
#e_month = tk.Entry(window, width=5)

# Combobox creation
n = tk.StringVar()
month_chosen = ttk.Combobox(window, textvariable = n, width=12)

# Adding combobox drop down list
month_chosen['values'] = ('Select a date...', 
                          'January', 
                          'February',
                          'March',
                          'April',
                          'May',
                          'June',
                          'July',
                          'August',
                          'September',
                          'October',
                          'November',
                          'December')


month_chosen['state'] = 'readonly'

e_year = tk.Entry(window, width=5)

#Button to calculate age
btn_calculate_age = tk.Button(window,
                              text="Calculate Age",
                              font=("Arial", 13),
                              command=validation)

#label for text box that will display the calculated age
lb_calculated_age = tk.Label(window,
                             text="The calculated age is: ",
                             font=('Arial', 12, "bold"),
                             fg="darkgreen",
                             bg="#00287F")
tbox_age = tk.Text(window, width=5, height=0, state="disabled")

#Button to exit application
btn_exit = tk.Button(window,
                     text="Exit Application",
                     font=("Arial", 13),
                     command=exit)

# Placing the elements on the screen
lb_heading.place(x=40, y=5)
lb_subheading.place(x=4, y=40)
lb_date.place(x=117, y=70)
lb_month.place(x=100, y=95)
lb_year.place(x=49, y=120)
e_date.place(x=180, y=70)
#e_month.place(x=180, y=95)
month_chosen.place(x=180,y=95)
e_year.place(x=180, y=120)
btn_calculate_age.place(x=100, y=150)
lb_calculated_age.place(x=10, y=200)
tbox_age.place(x=240, y=200)
btn_exit.place(x=100, y=240)
