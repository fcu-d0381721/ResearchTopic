import pandas as pd
import numpy as np
import cv2
import math
from sklearn.preprocessing import MinMaxScaler
# X Y
# 極東: 316436.52     2769354.22 (想要讓他變成正方形，兩者間相差7019.44，故在最東邊加上去)(328455.96)
# 極西: 295660.54     2778745.69 (290660.54)
# 極南: 309517.65     2761660.91  (2756660.91)
# 極北: 305533.52     2789459.33  (2794459.33)
#  視窗大小
x_step = 500
y_step = 1000


df = pd.read_csv('../Data/轉成功.csv', encoding='utf-8')
print(df.iloc[0:22, 153:-2])
scaler = MinMaxScaler()
print(scaler.fit(df.iloc[0:22, 153:-2]))
X = scaler.transform(df.iloc[0:22, 153:-2])
print(X)

img = np.zeros([x_step + 1, y_step + 1, 1])
# img1 = np.zeros([x_step + 1, y_step + 1, 1])

x = list()
y = list()
#  內差法使用(縮小到窗格大小)
max_x =  330000 - 280000
max_y =  2800000 - 2700000

# raw_max_x = df['X'].max() - 290000
# raw_max_y = df['Y'].max() - 2700000

windows = max_x / x_step

for value in df.X:
    value = value - 280000
    x.append(float(value) / ((float(max_x/x_step))))

for value in df.Y:
    value = value - 2700000 -25000
    y.append(float(value) / ((float(max_y/y_step))))

#  將圖片有點的地方標示1 周圍的部分利用擴散函數給值
month = ['6', '7', '8', '9', '10', '11', '12']
day = [30, 31, 31, 30, 31, 30, 31]
count = 0
for m in range(len(month)):
    for d in range(1, day[m]+1):
        for index in range(len(x)):

            img_x = round(x[index])
            img_y = round(y[index])

            # img[img_x][img_y][0] = 1
            img[img_x-24:img_x+27, img_y-24:img_y+30, 0] = X[index,count]
        count += 1
        # img[img_x][img_y][0] = 1
#  由於RGB範圍為0-255 所以在輸出的時候要除以這個範圍
        cv2.imwrite('./image/' + month[m] + '-' + str(d) + '.png', img*255)
        cv2.imshow("image", img)
        # cv2.waitKey()