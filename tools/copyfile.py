import os
import shutil
folder_annotation="/home/yanxp/home/yanxp/py-R-FCN/data/VOCdevkit2012/VOC2012/Annotations/"
folder_image="/home/yanxp/home/yanxp/py-R-FCN/data/VOCdevkit2012/BottleplantImages/"
folder_annotationgroundtruth="/home/yanxp/home/yanxp/py-R-FCN/data/VOCdevkit2012/BottleplantAnnotationsgrouth/"
for xmlname in os.listdir(folder_annotation):
    xmlname=xmlname.split(".")
    jpgname=xmlname[0]+".jpg"
    if os.path.isfile(folder_image+jpgname):
        shutil.copy(folder_annotation+xmlname[0]+'.xml',folder_annotationgroundtruth) 
    
