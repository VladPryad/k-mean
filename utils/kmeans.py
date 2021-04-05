from sklearn.cluster import KMeans
import config

class Clusterer:
    def __init__(self, scaledset):
        self.kmeans = KMeans(
            init="k-means++",
            n_clusters = config._CLUSTER_COUNT,
            n_init = 10,
            max_iter = 300)

        self.kmeans.fit(scaledset)
        self.sse = self.kmeans.inertia_
        self.centroids = self.kmeans.cluster_centers_
        self.iters = self.kmeans.n_iter_
        self.cluster_assignments = self.kmeans.labels_
