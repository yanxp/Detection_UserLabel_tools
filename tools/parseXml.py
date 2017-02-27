# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 16:58:10 2016

@author: yxp
"""

import os
import  xml.dom.minidom
from generateXML import GenerateXml
folder_annotationpred="annotation_pred/"
folder_xml="annotation_orig/"
for filename in os.listdir(folder_annotationpred):
    dom = xml.dom.minidom.parse(folder_annotationpred+filename)
    names_pred=dom.getElementsByTagName('name')
    score=dom.getElementsByTagName('score')
    xmin_pred=dom.getElementsByTagName('xmin')
    ymin_pred=dom.getElementsByTagName('ymin')
    xmax_pred=dom.getElementsByTagName('xmax')
    ymax_pred=dom.getElementsByTagName('ymax')
    height=dom.getElementsByTagName('height')
    width=dom.getElementsByTagName('width')
    labelname=""
    coord=""
    for i in xrange(len(names_pred)):
        name=names_pred[i].firstChild.data
        left_x=xmin_pred[i].firstChild.data
        left_y=ymin_pred[i].firstChild.data
        right_x=xmax_pred[i].firstChild.data
        right_y=ymax_pred[i].firstChild.data
        left_x=int(round(float(left_x)))
        left_y=int(round(float(left_y)))
        right_x=int(round(float(right_x)))
        right_y=int(round(float(right_y)))
        if left_x<0 or left_y<0 or right_x<0 or right_y<0:
            continue
    
        if left_x > right_x or left_y >right_y:
            continue
        if right_x >width:
            rigth_x=width
        if right_y >height:
            right_y=height
        labelname=labelname+""+name
        coord=str(left_x)+" "+str(left_y)+" "+str(right_x)+" "+str(right_y)
    GenerateXml(filename,folder_xml,width[0].firstChild.data,height[0].firstChild.data,labelname,coord)    