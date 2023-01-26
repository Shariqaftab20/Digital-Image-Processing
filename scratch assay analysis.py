""" 
scratch assay analysis 
we will use entropy filter here since the contrast of the image is
low and boundaries cant be distinguieshed
  
"""

from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage import io
from matplotlib import pyplot as plt
import numpy as np
from skimage.filters import threshold_otsu
import glob

path="scratch_assay/*"
time=0
time_list=[]
area_list=[]

for file in glob.glob(path):
    img=io.imread(file)
    
    a=(int)(img[0].size/3)
    squeez_img=img[0:a,0:a,0:1]
    squeez_img=np.squeeze(squeez_img)
    
    entropy_img=entropy(squeez_img, disk(10))
    thresh_val=threshold_otsu(entropy_img)
    
    binary_img = entropy_img <= thresh_val
    scratch_area=np.sum(binary_img==True)
    #print(time, scratch_area)
    time_list.append(time)
    area_list.append(scratch_area)
    time+=1
    
#print(time_list, area_list)
plt.plot(time_list,area_list,'bo') 
     


