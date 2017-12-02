# -*- coding:utf-8 -*-


import os
def compute_format(path,result_path):
	with open(result_path,'w') as fw:
		new_dict={}
		new_list=[]
		temp_list=[]
		fr=open('D://temp_put/groundtruth1.txt','r')
		print(fr)
		for line in fr:
			temp=[x for x in line.split(',')]
			temp_1=[float(temp[i]) for i in range(len(temp)) ]
			#print(temp_1)
			#print('IIIIIIIIIIII')
			new_list.append(temp_1)
		for line in new_list:
			temp_compu=[]
			a=int(line[0])

			b=int(line[1])

			w=int(line[2]-line[0])

			h=int(line[7]-line[1])

			temp_compu.append(a)
			temp_compu.append(b)
			temp_compu.append(w)
			temp_compu.append(h)

			temp_list.append(temp_compu)
			#fw.write(str(a)+str(b)+'\n')
			fw.write(str(temp_compu)+'\n')

		# print(temp_list)

		#fw.writelines(str(temp_list)+'/n')


if __name__ =="__main__":
	path='D://temp_put/groundtruth1.txt'
	result_path='D://temp_put/groundresult1.txt'
	compute_format(path,result_path)