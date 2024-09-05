# CV2 人臉偵測
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

img = np.array(Image.open('全班一號.jpg').convert(mode='RGB'))
pictPath = r'haarcascade_frontalface_alt2.xml'  #  專看人臉的模型
face_cascade = cv2.CascadeClassifier(pictPath)  #  產生一個分類器
print(img.shape)  # (1773, 2364, 3)
faces = face_cascade.detectMultiScale(img, scaleFactor=1.05,  #  利用分類器將人臉挑出來  注意引數的設定值
        minNeighbors = 21, minSize=(10,10),maxSize=(300,300))

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      # 藍色框住人臉

h = img.shape[0]
w = img.shape[1]

# 標註右下角底色是黃色
cv2.rectangle(img, (w-700, h-100),(w,h), (255,255,0), -1)

# 標註找到多少的人臉  要顯示中文喔
img_ = Image.fromarray(img).convert(mode='RGBA')
# make a blank image for the text, initialized to transparent text color
txt = Image.new("RGBA", (w,h), (255, 255, 255, 0))
# get a font
fnt = ImageFont.truetype(r"NotoSansTC-Light.ttf",70)
# get a drawing context
d = ImageDraw.Draw(txt)
# draw text, half opacity
d.text((w-600, h-100),"發現 " + str(len(faces)) + " 個人頭", font=fnt, fill=(255, 0, 0, 200))  # 文字是如何對齊的?
out = Image.alpha_composite(img_, txt).convert(mode='RGB')
img = np.array(out)

cv2.namedWindow('Face',0)
cv2.imshow("Face", img[:,:,::-1])   # 顯示影像
cv2.waitKey(0)
cv2.destroyAllWindows()