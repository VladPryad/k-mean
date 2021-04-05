import tkinter as tk
from tkinter import ttk
from components.plotraw import PlotRaw

class Tabcontrol(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        super(Tabcontrol, self).__init__()

        tabControl = ttk.Notebook(self)

        tabControl.add(PlotRaw(self), text='Raw Plot')

        tabControl.pack(expand=1, fill="both")
