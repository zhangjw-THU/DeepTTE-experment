import numpy as np
import ujson as json
import numpy as np
import ujson as json

import argparse
#get_file_name
parser = argparse.ArgumentParser()
parser.add_argument('--name', type = str)
args = parser.parse_args()
name = args.name

#get_mean_and_std
def get_list(data):
	a = list(data)
	return a
#get_dist_gap_array:
def dist_gap_array(line):
	elements = json.loads(line)
	dist_gap = np.array(elements["dist_gap"])
	dist_gap_diff = np.diff(dist_gap)
	a = get_list(dist_gap_diff)
	return a
def dist_gap_mean_std(lines):
	dist_gap = []
	for line in lines:
		a = dist_gap_array(line)
		for i in a:
			if i<0:
				print("waring")
			dist_gap.append(i)

	dist_gap = np.array(dist_gap)
#	print("dist_gap:",dist_gap.size)
	return dist_gap.mean(),dist_gap.std()


#get_time_gap
#get_time_gap_array:
def time_gap_array(line):
	elements = json.loads(line)
	time_gap = np.array(elements["time_gap"])
	time_gap_diff = np.diff(time_gap)
	a = get_list(time_gap_diff)
	return a

def time_gap_mean_std(lines):
	time_gap = []
	for line in lines:
		a = time_gap_array(line)
		for i in a:
			if i<0:
				print(line)
				print("waring") 
			
			time_gap.append(i)
	time_gap = np.array(time_gap)
	return time_gap.mean(),time_gap.std()

#get_lngs_gap_array:
def lngs_array(line):
	elements = json.loads(line)
	lngs = np.array(elements["lngs"])
	a = get_list(lngs)
	return a

def lngs_mean_std(lines):
	lngs = []

	for line in lines:
		a = lngs_array(line)
		for i in a:
			lngs.append(i)
	lngs = np.array(lngs)
	return lngs.mean(),lngs.std()


#get_lats_gap_array:
def lats_array(line):
	elements = json.loads(line)
	lats = np.array(elements["lats"])
	#dist_gap_diff = np.diff(dist_gap)
	a = get_list(lats)
	return a

def lats_mean_std(lines):
	lats = []

	for line in lines:
		a = lats_array(line)
		for i in a:
			lats.append(i)

	lats = np.array(lats)
	return lats.mean(),lats.std()

#get_dist_mean_and_std:
def dist_array(line):
	elements = json.loads(line)
	dist = np.array(elements["dist"])
	#dist_gap_diff = np.diff(dist_gap)
	return dist

def dist_mean_std(lines):
	dist = []
	for line in lines:
		a = dist_array(line)
		dist.append(a)
	dist = np.array(dist)
	return dist.mean(),dist.std()
#get_time_mean_and_std:
def time_array(line):
	elements = json.loads(line)
	time = np.array(elements["time"])
	#dist_gap_diff = np.diff(dist_gap)
	return time

def time_mean_std(lines):
	time = []
	for line in lines:
		a = time_array(line)
		time.append(a)
	time = np.array(time)
	return time.mean(),time.std()

#main()
ftele = open(name)
#print("20161102_demo_F:")
lines = ftele.readlines()
length = len(lines)
dgm1,dgs1=dist_gap_mean_std(lines)
tgm1,tgs1=time_gap_mean_std(lines)
lnm1,lns1=lngs_mean_std(lines)
lam1,las1=lats_mean_std(lines)
dm1,ds1=dist_mean_std(lines)
tm1,ts1=time_mean_std(lines)
ftele.close()



print("dgm:",dgm1)
print("dgs:",dgs1)
print("tgm:",tgm1)
print("tgs:",tgs1)
print("lnm:",lnm1)
print("lns:",lns1)
print("lam:",lam1)
print("las:",las1)
print("dm:",dm1)
print("ds:",ds1)
print("tm:",tm1)
print("ts:",ts1)
"""
ftele = open("gps_V4_20161105","r")
print("gps_V4_20161105:")
lines = ftele.readlines()
length = len(lines)
dgm2,dgs2=dist_gap_mean_std(lines)
tgm2,tgs2=time_gap_mean_std(lines)
lnm2,lns2=lngs_mean_std(lines)
lam2,las2=lats_mean_std(lines)
dm2,ds2=dist_mean_std(lines)
tm2,ts2=time_mean_std(lines)
ftele.close()

ftele = open("gps_V4_20161109","r")
print("gps_V4_20161109:")
lines = ftele.readlines()
length = len(lines)
dgm3,dgs3=dist_gap_mean_std(lines)
tgm3,tgs3=time_gap_mean_std(lines)
lnm3,lns3=lngs_mean_std(lines)
lam3,las3=lats_mean_std(lines)
dm3,ds3=dist_mean_std(lines)
tm3,ts3=time_mean_std(lines)
ftele.close()

ftele = open("gps_V4_20161110","r")
print("gps_V4_20161110:")
lines = ftele.readlines()
length = len(lines)
dgm4,dgs4=dist_gap_mean_std(lines)
tgm4,tgs4=time_gap_mean_std(lines)
lnm4,lns4=lngs_mean_std(lines)
lam4,las4=lats_mean_std(lines)
dm4,ds4=dist_mean_std(lines)
tm4,ts4=time_mean_std(lines)
ftele.close()
"""
"""
print("dgm:",(dgm1+dgm2+dgm3+dgm4)/4)
print("dgs:",(dgs1+dgs2+dgs3+dgs4)/4)
print("tgm:",(tgm1+tgm2+tgm3+tgm4)/4)
print("tgs:",(tgs1+tgs2+tgs3+tgs4)/4)
print("lnm:",(lnm1+lnm2+lnm3+lnm4)/4)
print("lns:",(lns1+lns2+lns3+lns4)/4)
print("lam:",(lam1+lam2+lam3+lam4)/4)
print("las:",(las1+las2+las3+las4)/4)
print("dm:",(dm1+dm2+dm3+dm4)/4)
print("ds:",(ds1+ds2+ds3+ds4)/4)
print("tm:",(tm1+tm2+tm3+tm4)/4)
print("ts:",(ts1+ts2+ts3+ts4)/4)
"""

