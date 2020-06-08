import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import PreProccesing as pp
import GUI
# Global Vars
path = './Dataset.csv'

# df = pd.read_csv(path)
#     # Begin the PreProcessing
#     pre_proc = pp.pre_processing(df)
#     print("Preprocessing completed successfully!")

if __name__ == '__main__':
    our_root_window = GUI.Root()
    our_root_window.mainloop()
