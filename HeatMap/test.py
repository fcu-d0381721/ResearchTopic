from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd


df = pd.read_csv('../Data/轉成功.csv', encoding='utf-8')
print(df.iloc[0:22, 153:-2])
scaler = MinMaxScaler()
print(scaler.fit(df.iloc[0:22, 153:-2]))
X = scaler.transform(df.iloc[0:22, 153:-2])
print(X)
