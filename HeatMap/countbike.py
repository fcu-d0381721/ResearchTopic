import pandas as pd

df = pd.read_csv('../Data/cleanupYBdata_2017/6月借量.csv', encoding='utf-8')
site = df['借車場站'].unique()
month = ['06']
day = [30]
del df['Unnamed: 0']
for i in site:
    con = df['借車場站'] == i
    temp = df[con].reset_index(drop=True)
    for m in range(len(month)):
        for d in range(1, day[m]+1):
            if d < 10:
                time = '2017-' + month[m] + '-0' + str(d)
            else:
                time = '2017-' + month[m] + '-' + str(d)
            show = temp[temp['日期'] == time].reset_index(drop=True)
            print(show)
            print(i, show['借車次數'].sum())