from tkinter import *
from psutil import disk_partitions, disk_usage, virtual_memory, cpu_percent




window = Tk()
window.geometry("900x600")
window.title("CPU -- RAM --Disk Usage")



# function to display CPU information
def show_cpu_info():
    cpu_use = cpu_percent(interval=1)
    # print('{}%'.format(cpu_use))
    cpu_Label.config(text= '{}%'.format(cpu_use))
    cpu_Label.after(200,show_cpu_info)


# Title program 
title_program = Label(window, text='PC PERFORMANCE MANAGER', font='Arial 40 bold', fg='#14747F')
title_program.place(x=110, y=20) 

#CPU Title
cpu_title_label = Label(window, text='CPU Usage: ', font='Arial 24 bold', fg='#FA5125')
cpu_title_label.place(x=20, y=155)
# Label to show Percent of CPU
cpu_Label = Label(window, bg ='#071C1E', fg='#FA5125', font='Arial 30 bold', width=20)
cpu_Label.place(x=230, y=150)
if __name__ =='__main__':
    show_cpu_info()

window.mainloop()