# -*- coding: utf-8 -*-
"""
Spyder Editor

a=[1,2,3,4,5]
b=np.array(a)

print (b)   

c=[[2,3,4],[5,6,7]]
d=np.array(c)
print (d)
a= np.zeros((1,5))
print(a) 

b=np.full((3,3),10)
print(b)

c=np.eye(3)
print(c)

a=np.random.random((3,3))
print(a)

x=np.array([[1,2,],[3,4]],dtype=np.float64)
y=np.array([[5,6,],[7,8]],dtype=np.float64)

print(x+y)
print (np.sum(x))
print(np.sum(x ,axis=0))

import imageio  as im

img=im.imread('th.jpg')
print(img)

for num in range(10,21):
    if num%2==0:
        print("%d is an even number"%(num))

def my_func():
    print("Hello from inside the function!!")

my_func()

def my_func1(slang="lodu"):
    print("Hello %s from inside the function!!"%(slang))
    
my_func1()

from scipy import misc,ndimage
import imageio  as im

img=im.imread('th.jpg')

def rotate(img):
    rot_img=ndimage.rotate(img,45)
    im.imsave("rotated.jpg", rot_img)
    
def blurred(img):
    blur_img=ndimage.gaussian_filter(img, sigma=1)
    im.imsave("blurred.jpg", blur_img)
    
def denoised(img):
    denoise_img=ndimage.median_filter(img,3)
    im.imsave("denoised.jpg", denoise_img)
    
rotate(img)
blurred(img)
denoised(img)

import imageio as im
from matplotlib import pyplot as plt

img=im.imread("th.jpg")

rand_img=np.random.random([500,500])
plt.imshow(rand_img)

img[10:200,10:200,:]=[125,125,125]

plt.imshow(img)

This is a temporary script file.
"""
"""
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


img=Image.open("th.jpg")
print(type(img)) 
print(img.format)
img1=np.asarray(img)

plt.imshow(img1)
"""
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread("th.jpg")

print(type(img))
plt.imshow(img)
plt.colorbar()

import matplotlib.pyplot as plt

img=cv2.imread("th.jpg",0)
cv2.imshow("Gray Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2 
import glob
import matplotlib.pyplot as plt


path ="images/*"

for file in glob.glob(path):
    print(file)
    a=cv2.imread(file)
    cv2.imshow("Test",a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

from PIL import Image
img=Image.open("th.jpg")
print(type(img))
print(img.size)
print(img.mode)

small_img=img.resize((100,100))
small_img.save("smallImage.jpg")
"""
from skimage import io,img_as_ubyte
from matplotlib import pyplot as plt

img=img_as_ubyte(io.imread("th.jpg",as_gray=True))
print(type(img)) 
plt.imshow(img)


























