from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import config

class Set:
    def __init__(self, count, deviation):
        self.set, self.setDescription = make_blobs(
            n_samples = config._POINTS_COUNT,
            centers = config._CLUSTER_COUNT,
            cluster_std = config._DEVIATION,
            random_state = config._SEED
        )
        self.set = StandardScaler().fit_transform(self.set)
    
    def getSet(self):
        return self.set

    def printSet(self):
        for i in range(len(self.set)):
            print(f" {self.set[i].x}  {self.set[i].y} \r\n")
        