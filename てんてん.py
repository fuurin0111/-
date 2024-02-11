import cv2
import numpy as np



image_name = input('変えたい画像の絶対urlを入れてください')
image_url = image_name
im_gray_url = image_name+'_gray.png'
new_im_gray_url = image_name+'_gray.png'

im_gray = cv2.imread(image_url, cv2.IMREAD_GRAYSCALE)
print(im_gray.shape)
im_gray_y,im_gray_x = im_gray.shape
print(im_gray.dtype)
cv2.imwrite(im_gray_url, im_gray)

if (im_gray_y > 350 and im_gray_x < 700) or (im_gray_x > 600 and im_gray_x < 1200):
    im_gray = cv2.resize(im_gray, dsize=None, fx=0.5, fy=0.5)
    im_gray_y,im_gray_x = im_gray.shape
elif (im_gray_y >= 700 and im_gray_x < 1400) or (im_gray_x < 2400 and im_gray_x >= 1200):
    im_gray = cv2.resize(im_gray, dsize=None, fx=0.25, fy=0.25)
    im_gray_y,im_gray_x = im_gray.shape
    

new_im_gray = []
img_size = 2
a = []
for i in range(round(im_gray_y/img_size)):
    a = []
    for j in range(round(im_gray_x/img_size)):
        if round(im_gray[i*img_size][j*img_size]/128) == 2:
              a.append("　")
        else:
              a.append("⬜")
    new_im_gray.append(a)

for i in range(round(im_gray_y/img_size)):
    print(*new_im_gray[i])
