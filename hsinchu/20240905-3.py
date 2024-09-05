import os
import numpy as np
import cv2                #影像處理模組 OpenCV
import dlib               #人臉識別模組 dlib

path = './照片/'

name_list = []
for root, dirs, files in os.walk(path):
    for file in files:
        name_list.append(os.path.join(root, file))
print(name_list)

# dlib
detector = dlib.get_frontal_face_detector()    # 使用dlib模組提供的人臉偵測函式，基於HOG特徵，建立找尋人臉的物件
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# 人臉68個特徵形狀預測物件的產生，是基于 Ensemble of Regression Trees 理論

# cv2讀取影像
def cv2_imread(filePath):
    cv_img = cv2.imdecode( np.fromfile(filePath,dtype=np.uint8) , cv2.IMREAD_UNCHANGED )
    return cv_img

for name in name_list :

    img = cv2_imread(name)

    # 取灰度
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 先看到人臉在甚麼地方
    rects = detector(img_gray, 1) # 人臉方框的矩形左上右下座標

    #print(dir(rects[0]))  # <class '_dlib_pybind11.rectangle'>
    # 'area', 'bl_corner', 'bottom', 'br_corner', 'center', 'contains', 'dcenter', 'height',
    # 'intersect', 'is_empty', 'left', 'right', 'tl_corner', 'top', 'tr_corner', 'width'

    img1 = img[rects[0].top():rects[0].bottom(),rects[0].left():rects[0].right()]

    path = name[:-4]+'1.jpg'
    #print(path)  # ./113市府AI技術應用與自動控制培訓班(個人大頭照)/劉凡綺1.jpg
    cv2.imencode('.jpg',img1)[1].tofile(path)