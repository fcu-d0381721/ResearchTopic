import pandas as pd
import numpy as np
import cv2
import math
# 極東: 316436.52     2769354.22 (想要讓他變成正方形，兩者間相差7019.44，故在最東邊加上去)
# 極西: 295660.54     2778745.69
# 極南: 309517.65     2761660.91
# 極北: 305533.52     2789459.33


#  視窗大小
x_step = 500
y_step = 500
a = 0.02
c = 1

df = pd.read_csv('../Data/轉.csv', encoding='utf-8')
img = np.zeros([x_step + 1, y_step + 1, 1])
img1 = np.zeros([x_step + 1, y_step + 1, 1])

x = list()
y = list()
#  內差法使用(縮小到窗格大小)
max_x =  323455.96 - 295660.54
max_y =  2789459.33 - 2761660.91
windows = max_x / x_step

for value in df.X:
    value = value - 295660.54
    float(value) / (math.ceil(float(max_x / y_step)))
    x.append(float(value) /(math.ceil(float(max_x/y_step))))

for value in df.Y:
    value = value - 2761660.91
    y.append(float(value) /(math.ceil(float(max_y/y_step))))

#  將圖片有點的地方標示1 周圍的部分利用擴散函數給值
for index in range(len(x)):
    img_x = math.floor(x[index])
    img_y = math.floor(y[index])

    img[img_x][img_y][0] = img[img_x][img_y][0] + 1
    for rowX in range(x_step):
        for rowY in range(y_step):
            d = np.sqrt(np.square((img_x - rowX)*windows) + np.square((img_y - rowY)*windows))
            fvq = c*np.exp(-a*d)
            if img[rowX][rowY][0] >= 1:
                img[rowX][rowY][0] = 1
            elif img[rowX][rowY][0] != 0:
                if img[rowX][rowY][0] < fvq:
                    img[rowX][rowY][0] = fvq
            else:
                img[rowX][rowY][0] = img[rowX][rowY][0] + fvq

#  由於RGB範圍為0-255 所以在輸出的時候要除以這個範圍
cv2.imwrite('color_img.png', 255*img)
cv2.imshow("image", img)
cv2.waitKey()
