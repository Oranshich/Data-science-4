import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.decomposition import PCA
import seaborn as sns

def model(pre_proc):
    print(pre_proc.head(5))
    wcss = []
    X = pre_proc.iloc[:, [2, 5]].values
    # for i in range(1, 11):
    #     kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    #     kmeans.fit(X)
    #     wcss.append(kmeans.inertia_)
    # plt.plot(range(1, 11), wcss)
    # plt.title('Elbow Method')
    # plt.xlabel('Number of clusters')
    # plt.ylabel('WCSS')
    #plt.show()
    #
    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(pre_proc)
    pre_proc['Cluster'] = y_kmeans
    # plt.scatter(pre_proc['Social support'], pre_proc['Generosity'])
    reduced_data = PCA(n_components=2).fit_transform(pre_proc)
    # print(reduced_data)
    # results = pd.DataFrame(reduced_data, columns=['Generosity', 'Social support'])
    # print(results)
    # sns.scatterplot(x="Generosity", y="Social support", hue=pre_proc['Cluster'], data=results)
    # plt.title('K-means Clustering with 2 dimensions')
    # plt.show()
    plt.scatter(reduced_data[y_kmeans == 0, 0], reduced_data[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(reduced_data[y_kmeans == 1, 0], reduced_data[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(reduced_data[y_kmeans == 2, 0], reduced_data[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow')
    # plt.title('Generosity as dependent in Social Support attribute')
    # plt.xlabel('Social support')
    # plt.ylabel('Generosity')
    # # plt.scatter(pre_proc['Social support'], pre_proc['Generosity'], s=100, c='red', label='Cluster 1')
    # # plt.scatter(pre_proc[pred_y == 1, 0], pre_proc[pred_y == 1, 1], s=100, c='blue', label='Cluster 2')
    # # plt.scatter(pre_proc[pred_y == 2, 0], pre_proc[pred_y == 2, 1], s=100, c='green', label='Cluster 3')
    plt.show()

    # py.sign_in('oransh', '5cq2961z6AYEEPyEql7N')
    # py.image.save_as('choromap', filename='name.png')
    return None