import matplotlib.pyplot as plt
import pandas as pd

def read(path):
    list_lines=[]
    with open(path, 'r') as sample_data:
        for line in sample_data:
            data=line.split()
            try:
                data[0]=float(data[0])
                data[1]=float(data[1])
                list_lines.append(data)
            except (IndexError, ValueError):
                continue
    dataframe = pd.DataFrame(list_lines,columns=['2Theta','Intensity'])
    return dataframe

def plot_graph(dataframe,title_graph=None):
    dataframe.plot(x='2Theta',xlabel='2$\Theta$ (degrees)',ylabel='Intensity (a.u.)',title=title_graph,yticks=[],legend=False)
    plt.show()

PATH='/home/larissa/Downloads/Análises/ZnFe2O4_1.txt'

df= read(PATH)
print(df)
plot_graph(df,'XRD Zinc Ferrite ($ZnFe_{2}O_{4}$)')
