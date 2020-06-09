import pandas as pd
import PreProccesing as pp
import ModelCreation as mc
import GUI
# Global Vars
path = './Dataset.csv'

df = pd.read_csv(path)
# Begin the PreProcessing
pre_proc = pp.pre_processing(df)
mc.model(pre_proc)
print("Preprocessing completed successfully!")

# if __name__ == '__main__':
#     our_root_window = GUI.Root()
#     our_root_window.mainloop()
