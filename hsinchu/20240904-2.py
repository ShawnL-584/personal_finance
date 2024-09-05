import numpy as np
import cv2
from PIL import Image

# with Image.open(r'C:\Users\my039\OneDrive\桌面\python\113市府AI技術應用與自動控制培訓班(個人大頭照)\劉凡綺.jpg') as im:
#     img = np.array(im)

import urllib.request  #  直接打開網路上的照片
url = r'https://p3.itc.cn/images01/20230919/91c499baeacb47e0af215305b122820f.jpeg'
img = np.array(Image.open(urllib.request.urlopen(url)))

cv2.namedWindow('Face',0)
cv2.imshow("Face", img[::,::,::-1])    # 顯示影像，記得轉成BGR模式

cv2.waitKey(0)
cv2.destroyAllWindows()