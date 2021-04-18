import tkinter as tk
from tkinter import ttk
from components.plotraw import PlotRaw
from components.plotprocessed import PlotProcessed
from components.dendrogram import Dendrogram
from services.set import Set
import config

class Tabcontrol(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        super(Tabcontrol, self).__init__()

        tabControl = ttk.Notebook(self)

        s = Set(config._POINTS_COUNT, config._DEVIATION).getSet()

        tabControl.add(PlotRaw(self, s), text='Raw Plot')
        tabControl.add(PlotProcessed(self, s), text='Processed Plot')
        tabControl.add(Dendrogram(self, s), text='Dendrogram')

        tabControl.pack(expand=1, fill="both")
