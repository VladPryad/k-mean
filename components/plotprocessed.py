import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from services.set import Set
from utils.kmeans import Clusterer
import numpy as np
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

        s = np.append(startset, clusterer.centroids, axis = 0)
        x = [el[0] for el in s]
        y = [el[1] for el in s]

        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])

        ax.scatter(
            x,
            y,
            marker = 'o',
            s = np.append([5.0] * len(startset), [15.0] * config._CLUSTER_COUNT, axis = 0),
            c = np.append(clusterer.cluster_assignments, [config._CLUSTER_COUNT + 1] * config._CLUSTER_COUNT, axis = 0))

        fig.suptitle('Clustered objects', fontsize=16)

        chart_type = FigureCanvasTkAgg(fig, self)
        chart_type.get_tk_widget().pack()