import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Global Vars
path = './Dataset.csv'


if __name__ == '__main__':
    df = pd.read_csv(path)
    print(df)
