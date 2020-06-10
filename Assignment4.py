import pandas as pd
import PreProccesing as pp
import ModelCreation as mc
import GUI

# df = pd.read_csv('Dataset.csv')
# # Begin the PreProcessing
# pre_proc = pp.pre_process(df)
# print("Preprocessing completed successfully!")
# mc.model(pre_proc)

if __name__ == '__main__':
    our_root_window = GUI.Root()
    our_root_window.mainloop()
