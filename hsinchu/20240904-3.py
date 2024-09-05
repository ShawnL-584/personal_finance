# CV2 人臉偵測
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

# pictPath = r'haarcascade_frontalcatface.xml' # 看貓臉
# face_cascade = cv2.CascadeClassifier(pictPath)                    # 建立辨識物件
# img = cv2.imread("cat.jpg")                                       # 讀取貓臉影像
# print(img.shape)  # (431, 576, 3)
# faces = face_cascade.detectMultiScale(img, scaleFactor=1.05,
#         minNeighbors = 9, minSize=(60,60),maxSize=(200,200))

pictPath = r'haarcascade_frontalface_alt2.xml' # 看人臉
face_cascade = cv2.CascadeClassifier(pictPath)



# img = np.array(Image.open(r"全班一號.jpg").convert(mode='RGB'))
# img = np.array(Image.open(r"404241.jpg").convert(mode='RGB'))
img = np.array(Image.open(r"404242.jpg").convert(mode='RGB'))
# img = np.array(Image.open(r"404243.jpg").convert(mode='RGB'))

# img = cv2.imread("class1.jpg")
print(type(img))
print(img.shape)  # (1773, 2364, 3)


faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 7, minSize=(55,55),maxSize=(250,250))

# print(faces)  # [ 471  784   68   68]  x y w h

# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-700, img.shape[0]-100),
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Finding " + str(len(faces)) + " face",
            (img.shape[1]-600, img.shape[0]-25),
            cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 2)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      # 藍色框住人臉

cv2.namedWindow('Face',0)
cv2.imshow("Face", img[:,:,::-1])                                 # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
scaleFactor:圖像大小在每個圖像尺度上減少了多少。
這個值用於創建縮放金字塔，以便檢測圖像中多個縮放的面部
(一些面可能更接近前景，因此更大；其他面可能更小並且在背景中，因此使用不同的縮放)。
比如設置值為1.05，則表明我們在金字塔中的每個級別將圖像的大小減小了5％。

minNeighbors:每個窗口應該有多少個neighbors才能將窗口中的區域視為一個臉。
級聯分類器將檢測面部周圍的多個窗口。
此參數控制需要檢測多少矩形(Neighbors)才能將窗口標記為面部。

minSize:寬度和高度(以像素為單位)的元組，表示窗口的最小尺寸。
小於此大小的邊界框將被忽略。從(30,30)開始並從那裡進行微調是一個好主意。
'''