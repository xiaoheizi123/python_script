# -*- coding:utf-8 -*-

import json

def writejfile(gfile,Jfile):
	with open('D://competition/ai_challenger/result.json','w') as f:
		result=[]
		new_dict={}
		ftxt=open(gfile,'r')
		for line in ftxt:
			print(line)
			m=line.split(',')
			new_dict["image_id"]=(m[0].split("'"))[1]
			print(m[0])
			new_dict["label_id"]=[x for x in [int(m[1]),int(m[2]),int((m[3].split("]"))[0])]]
			print(m[1])
			result.append(new_dict)
			
			new_dict={}
		json.dump(result,f,indent=4)


if __name__=='__main__':
	result_txt_path='D://competition/ai_challenger/1.txt'
	result_json_path='D://competition/ai_challenger/result.json'
	writejfile(result_txt_path,result_json_path)
