from tkinter import *
from psutil import disk_partitions, disk_usage, virtual_memory, cpu_percent




window = Tk()
window.geometry("900x600")
window.title("CPU -- RAM --Disk Usage")

window.mainloop()