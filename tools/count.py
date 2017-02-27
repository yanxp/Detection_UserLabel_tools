import os
i=0
folder="/home/yanxp/home/dataset/VOCdevkit2012/VOC2012/Annotations/"
for xmlname in os.listdir(folder):
    xmlname=xmlname.split("_")
    if xmlname[0]=='2007':
	i=i+1
print i
