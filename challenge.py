# -*- coding: utf-8 -*-
"""
Created on 10/16 20:05:37 2017

@author: zr
"""

import os
import csv
import numpy as np

#为了提高文件的可移植性，所以要写成函数的形式,并且记得传参
"""
def MakeTxtFile1(path_pic,path_txt):
	for root,dirs,files in os.walk(path_pic):
		if(root=="D://competition/ai_challenger/"):
			print(dirs)
			f1=open(path_txt,"w")
			for i in range(80):
				if(dirs==str(i)):
					print(true)
					for lines in files:
						f1.writelines(lines + str(i)+'\n')
			f1.close()"""

def MakeTxtFile(path_pic,path_txt,path_temp):
	for i in range(80):
		f1=open(path_temp,'a')
		#f2=open(path_txt,'a')
		for root,dirs,files in os.walk(os.path.join(path_pic,str(i))):
			print(i)
			print(root)
			print("^^^^^^^^^^^^^^^^^^^^^")
			print(dirs)
			print("^^^^^^^^^^^^^^^^^^^^^")
			print(files)
			for img in files:
				f1.write(img+" "+str(i)+"\n")
		f1.close()
		
def txtofpicfolder(path_pic,path_saved_txt):
	num=0
	ft=open(path_saved_txt,'w')
	for root,dirs,files in os.walk(path_pic):
		for image in files:
			#print(image)
			ft.write(image+'\n')
			num+=1
	print(num)
	ft.close()

def csv_name_file(path,class_name_file):
	n=0
	fn=open(class_name_file,'w')
	with open(path,'r') as f:
		item=f.readlines()
		print(item)

		for line in item:
			#odom=line.split()
			print(line)
			print(n)
			fn.writelines(line)
			n=n+1
	print(n)
	fn.close()


	#调用部分也还是要写成一整个函数模式

if __name__=="__main__":
	ai_path_pic='D://competition/ai_challenger/'
	ai_path_txt='D://competition/ai_challenger/pic_list'
	ai_path_temp='D://competition/ai_challenger/pic_temp'
	#MakeTxtFile(ai_path_pic,ai_path_txt,ai_path_temp)
	ai_path_test_pic='D://competition/ai_challenger/ai_challenger_scene_test_a_20170922/scene_test_a_images_20170922'
	ai_path_name_test='D://competition/ai_challenger/name_test'
	path='D://competition/ai_challenger/listm.txt'
	ai_path_name_file='D://competition/ai_challenger/class_name'

	#txtofpicfolder(ai_path_test_pic,ai_path_name_test)
	csv_name_file(path,ai_path_name_file)



'''txt_path=path_pic+'str(n)\\'
			if not os.path.exists(txt_path):
				os.makedirs(txt_path)'''