import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def model(pre_proc):
    print(pre_proc['Social support'])
    wcss = []

    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(pre_proc)
        wcss.append(kmeans.inertia_)
    # plt.plot(range(1, 11), wcss)
    # plt.title('Elbow Method')
    # plt.xlabel('Number of clusters')
    # plt.ylabel('WCSS')
    # plt.show()
    #
    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(pre_proc)
    pre_proc['Cluster'] = y_kmeans
    # plt.scatter(pre_proc['Social support'], pre_proc['Generosity'])
    X = pre_proc.iloc[:, [2, 5]].values
    print(X)
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow')
    # plt.scatter(pre_proc['Social support'], pre_proc['Generosity'], s=100, c='red', label='Cluster 1')
    # plt.scatter(pre_proc[pred_y == 1, 0], pre_proc[pred_y == 1, 1], s=100, c='blue', label='Cluster 2')
    # plt.scatter(pre_proc[pred_y == 2, 0], pre_proc[pred_y == 2, 1], s=100, c='green', label='Cluster 3')
    #plt.show()
    return None