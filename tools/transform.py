

from generateXML import GenerateXml

import json

from PIL import Image

import os

folder_image="/home/yarley/yanxp/dataset/coco/images/train2014/"

folder_json="/home/yarley/yanxp/dataset/coco/Annotations/train2014/"

folder_xml="/home/yarley/yanxp/dataset/coco/Annotations/train2014xml/"

for filename in os.listdir(folder_json):

    filename=filename.split(".")

    filename=filename[0];

  #  print filename

    img=Image.open(folder_image+filename+'.jpg','r');

    im_size=list(img.size);

    width=im_size[0];

    height=im_size[1];

    name=["aeroplane","bicycle","bird","boat","bottle","bus","car","cat","chair","cow","diningtable","dog","horse","motorbike","person","pottedplant","sheep","sofa","train","tvmonitor"];



    myfile1=open("labelmap_coco.prototxt","r")

    lines=myfile1.readlines();

    myfile1.close();

    lists=[];

    names=[];

    indexname=[];

    labelname=[];

    coord=[];

    for line in lines:

        lists.append(line.split()); ##extract data from labelamp 

    j=0

    for i in range(len(lists)):     

        if i%5==4:

            names.append(lists[i-1][1:]);

            j=j+1

    for i in range(len(names)):              

        names[i-1]=" ".join(names[i-1]);

        names[i-1]=names[i-1].strip('"');

 #   print "names:",names

    for i in range(len(name)):

        for j in range(len(names)):

           # print name[i]

            if name[i]=='aeroplane':

                name[i]='airplane';

           # print names[j]

            if name[i]==names[j]:

               if j<12:

                   k=j

               elif j<25:

                   k=j+1

               elif j<27:

                   k=j+2

               elif j<41:

                   k=j+4

               elif j<61:

                   k=j+5

               elif j<62:

                   k=j+6

               elif j<63:

                   k=j+8

               elif j<74:

                   k=j+9

               else:

                   k=j+10

               indexname.append(name[i]);

               indexname.append(k);

    indexname[0]="aeroplane"

    #print indexname

    myfile2=open(folder_json+filename+".json","r")

    anno=json.load(myfile2);

    myfile2.close();

    for j in range(len(indexname)-1):

        for l in anno["annotation"]:

            if l["category_id"]==indexname[j+1]:

                labelname.append(indexname[j]);

                coord.append(l["bbox"][0]);

                coord.append(l["bbox"][1]);

                coord.append(l["bbox"][2]+l['bbox'][0]);

                coord.append(l["bbox"][3]+l['bbox'][1]);
    if len(labelname)>0:
        GenerateXml(filename,folder_xml,width,height,labelname,coord);           


