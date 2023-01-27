""" 
Denoising an Image
we will use Gaussian filter median filter and local means filter
with gaussian filter we loose a ot of data 
with median filter data is lil more preserved

  
"""

from skimage import io,img_as_float
from skimage.restoration import denoise_nl_means,estimate_sigma
from matplotlib import pyplot as plt
import numpy as np
from scipy import ndimage as nd
import glob

img=(io.imread("noisy.jpg"))
plt.imshow(img)
guassian_img=nd.gaussian_filter(img, sigma=5)
plt.imshow(guassian_img)
plt.imsave("guassian_img.jpg",guassian_img)
median_img=nd.median_filter(img, size=5)
plt.imshow(median_img)
plt.imsave("median_img.jpg",median_img)

sigma_est=np.mean(estimate_sigma(img,multichannel=True))
local_mean_img=denoise_nl_means(img,h=1.15 * sigma_est, fast_mode=True, patch_size=5, patch_distance=3, multichannel=True)
plt.imsave("NLM.jpg",local_mean_img)


