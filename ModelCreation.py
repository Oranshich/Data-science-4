import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.text import Text
from sklearn.cluster import KMeans
import pandas as pd
import plotly.express as px
import chart_studio.plotly as py

matplotlib.use("TkAgg")


def model(pre_proc):
    X = pre_proc.iloc[:, [2, 5]].values
    kmeansData = pre_proc.iloc[:, 1:15]
    # for i in range(1, 11):
    #     kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    #     kmeans.fit(X)
    #     wcss.append(kmeans.inertia_)
    # plt.plot(range(1, 11), wcss)
    # plt.title('Elbow Method')
    # plt.xlabel('Number of clusters')
    # plt.ylabel('WCSS')
    # plt.show()
    #
    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    # print(pre_proc.dtypes())
    y_kmeans = kmeans.fit_predict(kmeansData)
    pre_proc['Cluster'] = y_kmeans
    print(pre_proc.head())
    return X, y_kmeans, kmeans


def get_plot(X, y_kmeans, kmeans, figure):
    #reduced_data = PCA(n_components=2).fit_transform(X)
    figure.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    figure.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    figure.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    figure.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow')
    figure.set_title('Generosity as dependent in Social Support attribute')
    figure.set_xlabel('Social support')
    figure.set_ylabel('Generosity')

    return figure


def extractCode(country, codes):

    code = codes.loc[codes['Country'] == country]
    return code['Alpha-3 code'][code['Alpha-3 code'].index[0]]


def choropleth(pre_proc, path="."):
    path = path + "/"
    codes = pd.read_csv("countries_codes_and_coordinates.csv")
    #pre_proc['code'] = codes[pre_proc['country']]
    pre_proc['code'] = pre_proc.apply(lambda row: extractCode(row['country'], codes), axis=1)

    fig = px.choropleth(pre_proc, locations="code",
                        color="Cluster",
                        color_continuous_scale=px.colors.DEFAULT_PLOTLY_COLORS)
    py.sign_in('oransh', 'EN3grDWl8bDjWchtjydW')
    py.image.save_as(fig, filename=path + "map.png")
