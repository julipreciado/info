import pandas as pd
import numpy as np
import os
import glob

#current =os.getcwd()
#file=glob.glob(current+"/*.csv")
mmse=pd.read_csv(r"C:\Users\SALASDRAI\Downloads\MMSE.csv", sep=";")
print(mmse)
print(mmse.index)
mmse_copy=mmse.copy()
mmse_copy=mmse_copy.set_index("Codigo")
mmse_copy.index
print(mmse_copy)
print(mmse_copy.index)

print(mmse.loc["CTR_001"])