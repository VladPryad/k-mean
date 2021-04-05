import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from services.set import Set
import config
import tkinter as tk

class PlotRaw(tk.Frame):
    def __init__(self, parent, startset):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        super(PlotRaw, self).__init__()

        s = startset
        x = [el[0] for el in s]
        y = [el[1] for el in s]

        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.scatter(x, y, color='r')

        chart_type = FigureCanvasTkAgg(fig, self)
        chart_type.get_tk_widget().pack()