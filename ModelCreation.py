import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.text import Text
from sklearn.cluster import KMeans
import pandas as pd
import plotly.express as px
import chart_studio.plotly as py
import os

matplotlib.use("TkAgg")


def model(pre_proc, num_of_run=10, num_of_clusters=3):
    X = pre_proc.iloc[:, [3, 6]].values
    kmeansData = pre_proc.iloc[:, 1::]


    kmeans = KMeans(n_clusters=num_of_clusters, init='k-means++', max_iter=300, n_init=num_of_run, random_state=0)
    # print(pre_proc.dtypes())
    y_kmeans = kmeans.fit_predict(kmeansData)
    pre_proc['Cluster'] = y_kmeans
    return X, y_kmeans, kmeans


def get_plot(X, y_kmeans, kmeans, figure, num_of_clusters=3):
    colors = cm.rainbow(np.linspace(0, 1, num=num_of_clusters))
    x = np.arange(10)
    ys = [i + x + (i * x) ** 2 for i in range(10)]

    for i in range(0, num_of_clusters):
        figure.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s=100, c=colors[i], label='Cluster 1')
    # figure.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    # figure.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
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
    pre_proc['code'] = pre_proc.apply(lambda row: extractCode(row['country'], codes), axis=1)

    fig = px.choropleth(pre_proc, locations="code",
                        color="Cluster",
                        color_continuous_scale=px.colors.DEFAULT_PLOTLY_COLORS)
    py.sign_in('rosengal', 'BCw4CTeuXUnQP4VOeozY')
    img_path = path + "map.png"
    if os.path.exists(img_path):
        os.remove(img_path)
    py.image.save_as(fig, filename=img_path, width=600, height=500)

    return img_path
