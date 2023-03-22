
import pandas as pd
import numpy as np
import os
import glob

#Crear dataframe con índice 0 para menor edad e índice mayor para mayor edad
mmse=pd.read_csv(r"C:\Users\SALASDRAI\Downloads\MMSE.csv", sep=";")
mmse_ordenado=mmse.sort_values(by="Edad en la visita")
mmse_indices=mmse_ordenado.reset_index()
#print(mmse_indices)

#Unir dataframes
evmedica=pd.read_csv(r"C:\Users\SALASDRAI\Downloads\EVALUACIONMEDICA.csv", sep=",")
unidos=mmse_indices.merge(evmedica, on="Codigo", how="right").drop(["Edad en la visita_y"], axis=1).drop(["Sexo_y"], axis=1)
print(unidos)

#Contar celdas que no son NaN
print(unidos.count())

#poner filas como columnas
print(unidos.transpose())

#columnas en orden alfabetico


