from tkinter import *
import tkinter as tk
from psutil import cpu_percent

window = Tk()
window.geometry("900x600")
window.title("CPU -- RAM --Disk Usage")

def toggle_widget():
    global widget_state

    if widget_state:
        cpu_title_label.place_forget()
        cpu_Label.pack_forget()
        widget_state = False
    else:
        cpu_title_label.place(x=20, y=155)
        cpu_Label.pack(padx=230, pady=150)
        widget_state = True

# function to display CPU information
def show_cpu_info():
    cpu_use = cpu_percent(interval=1)
    cpu_Label.config(text= '{}%'.format(cpu_use))
    cpu_Label.after(10000,show_cpu_info)

widget_state = False  # Initially, the widget is not displayed
toggle_button = tk.Button(window, text="Toggle Widget", command=toggle_widget)
toggle_button.pack()

# Title program
title_program = Label(window, text='PC PERFORMANCE MANAGER', font='Arial 40 bold', fg='#14747F')
title_program.place(x=110, y=20)

# CPU Title
cpu_title_label = Label(window, text='CPU Usage: ', font='Arial 24 bold', fg='#FA5125')
# cpu_title_label.place(x=20, y=155)

# Label to show Percent of CPU
cpu_Label = Label(window, bg='#071C1E', fg='#FA5125', font='Arial 30 bold', width=20)



if __name__ =='__main__':
    show_cpu_info()

window.mainloop()
