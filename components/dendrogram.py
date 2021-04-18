import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from services.set import Set
from scipy.cluster.hierarchy import dendrogram, linkage
import config
import tkinter as tk

class Dendrogram(tk.Frame):
    def __init__(self, parent, startset):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        super(Dendrogram, self).__init__()

        s = startset

        linked = linkage(s, 'single')

        labelList = range(1, config._POINTS_COUNT + 1)

        fig = plt.figure(figsize=(10, 7))
        dendrogram(linked,
            orientation='top',
            labels=None,
            distance_sort='descending',
            show_leaf_counts=True)
        
        fig.suptitle('Dendrogram', fontsize=16)

        chart_type = FigureCanvasTkAgg(fig, self)
        chart_type.get_tk_widget().pack()