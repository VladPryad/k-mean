import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from services.set import Set
from utils.kmeans import Clusterer
import config
import tkinter as tk

class PlotProcessed(tk.Frame):
    def __init__(self, parent, startset):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        super(PlotProcessed, self).__init__()

        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])

        s = startset
        clusterer = Clusterer(s)

        # res = [[] for i in range(config._CLUSTER_COUNT)]

        # for i in range(len(clusterer.cluster_assignments)):
        #     res[clusterer.cluster_assignments[i]].append(s[i])
        
        # for clusterId in range(config._CLUSTER_COUNT):
        #     cluster = res[clusterId]
        #     x = [e[0] for e in cluster]
        #     y = [e[1] for e in cluster]
        #     ax.scatter(x, y, c = [clusterId for el in range(len(cluster))])

        s = startset
        x = [el[0] for el in s]
        y = [el[1] for el in s]

        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.scatter(x, y, c = clusterer.cluster_assignments)


        chart_type = FigureCanvasTkAgg(fig, self)
        chart_type.get_tk_widget().pack()