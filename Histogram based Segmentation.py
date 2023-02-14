""" 
Histogram based image Segmentationm


  
"""

from skimage import io,img_as_float,img_as_ubyte
from skimage.restoration import denoise_nl_means,estimate_sigma
from matplotlib import pyplot as plt
import numpy as np
from scipy import ndimage as nd


img=img_as_float(io.imread("Histogram.jfif"))


sigma_est=np.mean(estimate_sigma(img,multichannel=True))
local_mean_img=denoise_nl_means(img,h=1.15 * sigma_est, fast_mode=True, patch_size=5, patch_distance=3, multichannel=True)
denoise_ubyte=img_as_ubyte(local_mean_img)
plt.imshow(denoise_ubyte, cmap='gray')
plt.hist(denoise_ubyte.flat,bins=100,range=(0,80))


seg1=(denoise_ubyte <= 55)
seg2=(denoise_ubyte > 55) & (denoise_ubyte <= 110)
seg3=(denoise_ubyte > 110) & (denoise_ubyte <= 210)
seg4=(denoise_ubyte > 210)

seg1.ndim

all_seg=np.zeros((denoise_ubyte.shape[0],denoise_ubyte.shape[1],3))

all_seg[seg1]=(1,0,0)
all_seg[seg2]=(0,1,0)
all_seg[seg3]=(0,0,1)
all_seg[seg4]=(1,1,0)


plt.imshow(all_seg)




