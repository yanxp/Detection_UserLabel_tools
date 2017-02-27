# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 21:48:58 2016

@author: yxp
"""
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'
import  xml.dom.minidom
#folder_root=""
folder_image="JPGEImages/"
folder_annotationpred="annotation/"
#folder_annotationorig="annotation_orig/"
folder_pltimage="images/"
for filename in os.listdir(folder_annotationpred):
    filename=filename.split(".")
    filename=filename[0]
    image_original = mpimg.imread(folder_image+filename+'.jpg')
    width=image_original.shape[0]
    height=image_original.shape[1]
    colors = plt.cm.hsv(np.linspace(0, 1, 21)).tolist()
    plt.imshow(image_original)
    currentAxis = plt.gca()
    dom = xml.dom.minidom.parse(folder_annotationpred+filename+'.xml')
    names_pred=dom.getElementsByTagName('name')
    score=dom.getElementsByTagName('score')
    xmin_pred=dom.getElementsByTagName('xmin')
    ymin_pred=dom.getElementsByTagName('ymin')
    xmax_pred=dom.getElementsByTagName('xmax')
    ymax_pred=dom.getElementsByTagName('ymax')
    
   # dom = xml.dom.minidom.parse(folder_root+folder_annotationorig+filename+'.xml')
   # names_orig=dom.getElementsByTagName('name')
   # xmin_orig=dom.getElementsByTagName('xmin')
   # ymin_orig=dom.getElementsByTagName('ymin')
   # xmax_orgi=dom.getElementsByTagName('xmax')
   # ymax_orig=dom.getElementsByTagName('ymax')
    for i in xrange(len(names_pred)):
        
        display_txt = '%s:%.3f'%(names_pred[i].firstChild.data,float(score[i].firstChild.data))
        left_x=xmin_pred[i].firstChild.data
        left_y=ymin_pred[i].firstChild.data
        right_x=xmax_pred[i].firstChild.data
        right_y=ymax_pred[i].firstChild.data
        coords = (left_x,left_y),float(right_x)-float(left_x)+1,float(right_y)-float(left_y)+1
        color = colors[0]
        currentAxis.add_patch(plt.Rectangle(*coords, fill=False, edgecolor=color, linewidth=2))
        currentAxis.text(left_x, left_y, display_txt, bbox={'facecolor':color, 'alpha':0.5})
   # for i in xrange(len(names_orig)-1):
   #     left_x=xmin_orig[i].firstChild.data
   #     left_y=ymin_orig[i].firstChild.data
   #     right_x=xmax_orgi[i].firstChild.data
   #     right_y=ymax_orig[i].firstChild.data
   #     coords = (left_x,left_y),int(right_x)-int(left_x)+1,int(right_y)-int(left_y)+1
   #     color = colors[8]
   #     currentAxis.add_patch(plt.Rectangle(*coords, fill=False, edgecolor=color, linewidth=2))
    plt.savefig(folder_pltimage+filename+'.jpg', dpi=1080)
    plt.close()
