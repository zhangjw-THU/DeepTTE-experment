
import numpy as np
import ujson as json

import argparse
#get_file_name
parser = argparse.ArgumentParser()
parser.add_argument('--name', type = str)
args = parser.parse_args()
name = args.name


flete1 = open(name,"r")
print("check : ",name)
lines = flete1.readlines()

def get_list(data):
	a = list(data)
	return a

def time_gap_array(line):
	elements = json.loads(line)
	time_gap = np.array(elements["time_gap"])
	time_gap_diff = np.diff(time_gap)
	a = get_list(time_gap_diff)
	return a

flete2 = open(name+"_checked",'a')

wrong = 0
for line in lines:
	a = time_gap_array(line)
	check = 0
	for i in a:
		if i<0:
			wrong +=1
			check = 1
			print("Wrong : ",wrong)
			break

	if check == 1:
		print(line)
		continue
	flete2.write(line)


print("OVER! ")
flete2.close()
flete1.close()


		



