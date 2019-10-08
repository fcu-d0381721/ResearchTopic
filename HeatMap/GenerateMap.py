import pandas as pd
import numpy as np
import cv2
import math
import time

#  窗格大小
x_step = 500
y_step = 500
a = 0.02
c = 1
dis = 1000
cnt = 0

# df = pd.read_csv('../Data/轉.csv', encoding='utf-8')
rain = pd.read_csv('../Data/2017-06-30.csv', encoding='utf-8')
rainstop = pd.read_csv('../Data/雨量測站.csv', encoding='utf-8')
del rain['Unnamed: 0']
rain['X'] = rainstop[rainstop['測站']=='信義']['X'].values[0]
rain['Y'] = rainstop[rainstop['測站']=='信義']['Y'].values[0]

img = np.zeros([x_step + 1, y_step + 1, 1])

x = list()
y = list()
#  內差法使用(縮小到窗格大小)
max_x =  323455.96 - 295660.54
max_y =  2789459.33 - 2761660.91
windows = max_x / x_step

value = rainstop[rainstop['測站']=='信義']['X'].values[0] - 295660.54
x.append(float(value) /(math.ceil(float(max_x/y_step))))

value = rainstop[rainstop['測站']=='信義']['Y'].values[0] - 2761660.91
y.append(float(value) /(math.ceil(float(max_y/y_step))))


img_x = math.floor(x[0])
img_y = math.floor(y[0])
img[img_x][img_y][0] = img[img_x][img_y][0] + 1
cv2.imshow("image1", img*255)
for m in range(1, 31):
    for h in range(1, 25):
        img_1 = np.zeros([x_step + 1, y_step + 1, 1])
        con = rain['觀測時間'] == h
        con1 = rain['日期'] == "06-" + str(m)
        t = rain[con & con1].reset_index(drop=True)
        for i in range(1, len(t.columns) - 3):
            for rowX in range(x_step):
                for rowY in range(y_step):
                    d = np.sqrt(np.square((img_x - rowX)*windows) + np.square((img_y - rowY)*windows))
                    if d <= dis:
                        if t.iloc[0, i] == "..." or t.iloc[0, i] == 'X':
                            img_1[rowX][rowY][0] = 0
                        else:
                            img_1[rowX][rowY][0] = t.iloc[0, i]

            alpha = 1 / i+1
            beta = (1.0 - alpha)
            # cv2.imwrite('img.jpg', img*255)
            # cv2.imshow("image", img*255)
            # cv2.imshow("image", img_1/255)
            img = cv2.addWeighted(img_1, alpha, img, beta, 0.0)
            # cv2.imwrite('img_1.jpg', img_1 * 255)
            # cv2.imwrite('color_img.jpg', img * 255)
            # cv2.imshow("image", img)
            cv2.imshow("image", img)
            cv2.waitKey()