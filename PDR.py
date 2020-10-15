from tkinter import *
import sys
import os

# set window info and color
window = Tk()
window['background']='#272727'
lbl =Label(window, text="App Configurable Hardware", fg='white', font='Helvetica 12 bold', background='#272727')
lbl.place(x=120, y=20)

# Reset Button
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
reset_button = Button( text="Reset", width=6, height=2, font='Helvetica 9 bold', background='#3b3f42', fg='white',
                       command= restart_program)
reset_button.place(x=200, y=450)

#======================================================================
# control box
#======================================================================
def control():
    Control_lbl = Label(window, text="Control Output", fg='white', font='Helvetica 10 bold', background='#272727')
    Control_lbl.place(x=290, y=250)
    L1 = Label(window, text="Enter Value", fg='white', font='Helvetica 10 bold', background='#272727')
    L1.place(x=260, y=280)
    E1 = Entry(window, bd=4, font='Helvetica 9 bold', background='#3b3f42', fg='white')
    E1.place(x=260, y=310)
#======================================================================
# monitor box
#======================================================================
def monitor():
    monitor_lbl = Label(window, text="Monitor Input", fg='white', font='Helvetica 10 bold', background='#272727')
    monitor_lbl.place(x=85, y=250)
    temprture_button = Button(text="Temperatures = 35°", width=18, height=2, font='Helvetica 9 bold', background='#3b3f42', fg='white')
    temprture_button.place(x=60, y=280)
    Humidity_button = Button(text="Humidity = 83%", width=18, height=2, font='Helvetica 9 bold', background='#3b3f42', fg='white')
    Humidity_button.place(x=60, y=330)
    control_button = Button(text="Control", width=6, height=2, font='Helvetica 9 bold', background='#3b3f42', fg='white',
                          command=control)
    control_button.place(x=100, y=380)


#======================================================================
# output list and box
#======================================================================
def outputBlock():
    output = ("PWM", "MQTT")
    lb = Listbox(window, height=5, width=12,selectmode='multiple', font='Helvetica 9 bold', background='#3b3f42', fg='white')
    for num in output:
        lb.insert(END, num)
    lb.place(x=310, y=90)
    output_lbl = Label(window, text="Select Output", fg='white', font='Helvetica 10 bold', background='#272727')
    output_lbl.place(x=313, y=60)
    output_button = Button(text="Next", width=6, height=2, font='Helvetica 9 bold', background='#3b3f42', fg='white',
                          command= monitor)
    output_button.place(x=330, y=185)

#======================================================================
# input type list and box
#======================================================================
def InputBlock():
    var = StringVar()
    var.set("one")
    input = ("Temperature", "Humidistat")
    la = Listbox(window, height=5, width=12, selectmode='multiple', font='Helvetica 9 bold', background='#3b3f42', fg='white')
    for num in input:
        la.insert(END, num)
    la.place(x=175, y=90)
    input_type_lbl =Label(window, text="Select Input Type", fg='white', font='Helvetica 10 bold' ,background='#272727')
    input_type_lbl.place(x=160, y=60)
    input_type_button = Button( text="Next", width=6, height=2, font='Helvetica 9 bold', background='#3b3f42', fg='white', command= outputBlock)
    input_type_button.place(x=195, y=185)

#======================================================================
# input list and box
#======================================================================
var = StringVar()
var.set("one")
input = ("I2C", "ADC")
la = Listbox(window, height=5, width=12, selectmode='multiple', font='Helvetica 9 bold', background='#3b3f42', fg='white')
for num in input:
    la.insert(END, num)
la.place(x=40, y=90)
input_lbl =Label(window, text="Select Input", fg='white', font='Helvetica 10 bold' ,background='#272727')
input_lbl.place(x=43, y=60)
input_button = Button( text="Next", width=6, height=2, font='Helvetica 9 bold', background='#3b3f42', fg='white', command= InputBlock)
input_button.place(x=60, y=185)




window.title('ECE484: Project 01 (App Configurable Hardware)')
window.geometry("400x300+10+10")
window.mainloop()