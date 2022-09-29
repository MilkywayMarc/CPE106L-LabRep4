"""
Author: GROUP 4 (CRUZ | LORENZANA | MARCELINO)
"""

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *

def openfile():
    tf = fd.askopenfilename()
    txtarea.insert(END, tf)
    
ws = Tk()
ws.title("Programming Problem # 2 | Group 4")
ws.geometry("400x450")
ws['bg'] = '#C0C0C0'

txtarea = Text(ws, width = 40, height = 20)
txtarea.pack(pady = 20)

tk.Button(text = 'Click to Open File', command=openfile).pack(fill=tk.X)
tk.mainloop()