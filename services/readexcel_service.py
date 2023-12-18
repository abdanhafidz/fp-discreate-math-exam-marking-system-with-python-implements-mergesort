import numpy as np
import pandas as pd


def read(fileName):
    df = pd.read_excel('./repositories/'+fileName)
    data = df.to_numpy()
    for i in range(0,len(data)):
        for j in range(0,3):
            s = data[i][2]
            ans = []
            for k in s:
                if(k!=','):
                    ans.append(k)
            data[i][2] = ans
    return data
