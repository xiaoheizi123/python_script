# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:05:37 2017

@author: zr
"""

import json
from PIL import Image
import os

with open("D://competition/ai_challenger/ai_challenger_scene_validation_20170908/validation.json", 'r') as load_f:
    load_dict = json.load(load_f)

    # print(load_dict)
    # print(type(load_dict))

print("------------------------------------")


raw_data = []
for i in range(len(load_dict)):
    for value in load_dict[i]:
        raw_data.extend(load_dict[i].values())
# print(raw_data)

j = len(raw_data)

path='D://competition/ai_challenger/ai_challenger_scene_validation_20170908/valid_list.txt'
f1=open(path,'a')
temp_url = [raw_data[0 + 3 * m] for m in range((int)(j / 3))]
temp_num = [raw_data[1 + 3 * m] for m in range((int)(j / 3))]
temp_name = [raw_data[2 + 3 * m] for m in range((int)(j / 3))]
print(temp_num)
#print(len(temp_num))

print(temp_name)
for i in range(len(temp_url)):
    f1.write(temp_name[i]+" "+temp_num[i] +"\n")

"""
pic = []
pic_1 = []
class_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
             '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
             '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
             '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
             '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
             '60', '61', '62', '63', '64', '65', '66', '67', '68', '69',
             '70', '71', '72', '73', '74', '75', '76', '77', '78', '79']


class_per_num = []
for i in class_num:
    for x in range(len(temp_num)):
        if(i == temp_num[x]):
            pic.append(temp_num[x])
            pic_1.append(temp_name[x])     #表示图片名字
# print(pic)



for ch in class_num:
    class_per_num.append(pic.index(ch))
print(class_per_num)
print(len(class_per_num))"""

#path='D:\\competition\\ai_challenger\\scene_train_images_20170904'
#new_path='D:\\competition\\ai_challenger\\0'
"""
for root,dirs,files in os.walk(path):
    for i in pic_1:
        file_path=root + '/' + i
        new_file_path = new_path + '/' + i
        shutil.move(file_path,new_file_path)

"""  
   # print("the lujing is %s" % (files))


"""for name in pic_1[159351:161637]:
    path1='D:\\competition\\ai_challenger\\scene_train_images_20170904\\' + name 
    img = Image.open(path1)
    img.save('D:\\competition\\ai_challenger\\79\\'+ name)"""

"""
path1='D:\\competition\\ai_challenger\\scene_train_images_20170904\\00000ae5e7fcc87222f1fb6f221e7501558e5b08.jpg'
img = Image.open(path1)
img.save('D:\\competition\\ai_challenger\\0\\00000ae5e7fcc87222f1fb6f221e7501558e5b08.jpg')
"""
"""
for i in range(80):
    for name in pic_1[class_per_num[i]:class_per_num[i+1]]:
        filename = 'D:\\competition\\ai_challenger\\'+ str(i) +'\\'
        sdf= os.path.dirname(filename)
        try:
            os.stat(sdf)
        except:
            os.mkdir(sdf)
        img = Image.open('D:\\competition\\ai_challenger\\scene_train_images_20170904\\'+name)
        img.save(filename+ name)
"""
