import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read(PATH):
    list_lines=[]
    with open(PATH, 'r') as sample_data:
        for line in sample_data:
            data=line.split()
            try:
                if data[0].isnumeric():
                    data[0]
                    data[0]=float(data[0])
                    data[1]=float(data[1])
                    list_lines.append(data)
            except IndexError:
                continue
    dataframe = pd.DataFrame(list_lines,columns=['2Theta','Intensity'])
    return dataframe

PATH='/home/larissa/Downloads/Análises/ZnFe2O4_1.txt'

df= read(PATH)
print(df)
