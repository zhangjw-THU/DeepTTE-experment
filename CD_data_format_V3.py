#=========Step_0========
"""
2,30.578616,104.068558,1,2014/8/3 10:58:48
2,30.578623,104.068557,1,2014/8/3 10:59:02
2,30.578624,104.068559,1,2014/8/3 10:59:10
2,30.578629,104.068561,1,2014/8/3 10:59:20
"""
import argparse
#get_file_name
parser = argparse.ArgumentParser()
parser.add_argument('--data', type = str)
args = parser.parse_args()
s_data = args.data

#=========================step_1============

print(s_data+":Step_1...")
flete = open(s_data+".txt","r")
import numpy as np
import pandas as pd
import re
lines = flete.readlines()
flete_1 = open(s_data+"_V0.txt",'a')
for line in lines:
	elements =re.split(" |,|/|:|\n",line)	
	point = elements[0]
	for i in range(9):
		point = point+','+elements[i+1]
	point = point +'\n'
	flete_1.write(point)
flete_1.close()
flete.close()

flete2 = pd.read_csv(s_data+"_V0.txt",header=None)
flete2 =flete2.sort_values([0,7,8,9])
flete2.to_csv(s_data+'_V1.txt',header=0,index=0)
print(s_data+":Step1 OVER")

"""
points = pd.DataFrame([ 1.0,30.624806,104.136604,1.0,2014.0,8.0,3.0,21.0,18.0,46.0]).T
for line in lines:
	elements =re.split(" |,|/|:|\n",line)	
	point = []
	for i in range(10):
		point.append(float(elements[i]))
	point = pd.DataFrame(point).T
	points=pd.concat([points,point],axis=0,ignore_index=True)
	#print(points)
points=points.sort_values([0,7,8,9])
points.to_csv(s_data+'_V1.txt',header=0,index=0)
flete.close()
print(s_data+":Step_1 OVER")
"""


"""
1.0,30.65447,104.121588,0.0,2014.0,8.0,3.0,6.0,15.0,58.0
1.0,30.65447,104.121588,0.0,2014.0,8.0,3.0,6.0,16.0,59.0
1.0,30.65447,104.121588,0.0,2014.0,8.0,3.0,6.0,17.0,59.0
1.0,30.65447,104.121588,0.0,2014.0,8.0,3.0,6.0,18.0,59.0
1.0,30.65447,104.121588,0.0,2014.0,8.0,3.0,6.0,20.0,0.0
"""

#=======================step_2=============
print(s_data+":Step_2...")
import numpy as np
import time
#time to unix
def datetime_timestamp(dt):
	time.strptime(dt,'%Y,%m,%d,%H,%M,%S')
	s = time.mktime(time.strptime(dt,'%Y,%m,%d,%H,%M,%S'))
	return str(s)
datas = open(s_data+"_V1.txt","r")
lines = datas.readlines()
data_write = open(s_data+"_V2.txt",'a')
j=0
order = 1
for line in lines:
	elements = line.split(',')
	if elements[3]=='0':
		order = order+1
		continue
	dt = str(int(float(elements[4])))+','+str(int(float(elements[5])))+','+str(int(float(elements[6])))+','+str(int(float(elements[7])))+','+str(int(float(elements[8])))+','+str(int(float(elements[9].split('\n')[0])))
	unix_time = datetime_timestamp(dt)
	
	s_format = elements[0]+','+str(order)+','+unix_time+','+elements[2]+','+elements[1]+'\n'
	data_write.write(s_format)
datas.close()
data_write.close()
print(s_data+":Step_2 OVER")

"""
1.0,327,1407029049.0,104.117814,30.654429
1.0,327,1407029080.0,104.117201,30.654178
1.0,327,1407029111.0,104.115779,30.653293
1.0,327,1407029141.0,104.115716,30.6533
1.0,327,1407029171.0,104.115532,30.65316
1.0,327,1407029197.0,104.115232,30.65302
1.0,327,1407029200.0,104.115271,30.65332
"""

#==================Step3==============
print(s_data+":Step_3...")
ftele2 = open(s_data+"_V2.txt",'r')
gps_change = open(s_data+'_V3.txt','a')
#import json
from math import radians, cos, sin, asin, sqrt

def readInChunks(fileobj,chunksize=4096):
    while 1:
        data = fileobj.read(chunksize)
        if not data:
            break
        yield data

one = ''
one_plus = ''

gps_points = ftele2.readlines()
len_of_all_gps = len(gps_points)

j=0
driver = 1
first_point = gps_points[0].split(',')
#one=first_point[0]+","+first_point[1]+","
one = str(driver) +"," + first_point[1]+","
for i in range(len_of_all_gps-1):
    point=gps_points[i].split(',')
    point_next = gps_points[i+1].split(',')

    if point[1]==point_next[1]:
        s=point[2]+','+point[3]+','+point[4].split('\n')[0]+','
        one=one+s
        j=j+1
    else:
        s=point[2]+','+point[3]+','+point[4].split('\n')[0]+','
        j=j+1
        one=one+s
        one_plus=one+str(j)+'\n'
	gps_change.writelines(str(one_plus))
        j=0
        if point[0] == point_next[0]:
        #one=point_next[0]+","+point_next[1]+","
            one = str(driver) + "," + point_next[1] + ","
        else:
            driver=driver+1
            one = str(driver) + "," + point_next[1] + ","

gps_change.close()
ftele2.close()
print(s_data+":Step_3 OVER")

"""
1,328,1407030471.0,104.109529,30.670981,1407030501.0,104.109679,30.670947,1407030532.0,104.109671,30.670889,1407030562.0,104.110799,30.672296,1407030571.0,104.109816,30.673707,1407030601.0,104.109541,30.675374,1407030632.0,104.109376,30.675315,1407030663.0,104.109213,30.675372,1407030684.0,104.109121,30.676205,1407030714.0,104.106539,30.679413,1407030745.0,104.106024,30.680333,1407030772.0,104.105795,30.680264,1407030774.0,104.105608,30.680064,1407030804.0,104.102062,30.679142,1407030833.0,104.100241,30.680456,1407030834.0,104.100271,30.680516,16
"""

#================Step_4=================
print(s_data+":Step_4...")

ftele = open(s_data+"_V3.txt","r")
lines = ftele.readlines()
gps_demo = open(s_data+"_V4.txt","a")

from math import radians, cos, sin, asin, sqrt
def get_distance(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lon1, lat1, lon2, lat2 = map(radians, map(float, [lon1, lat1, lon2, lat2]))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r



for line in lines:
	elements = line.split(',')
	length = len(elements)

	s = elements[0] + "," + elements[1] + "," + elements[2] + "," + elements[3] + "," +elements[4] + ","
	points_length = int(elements[length-1])
	i=0
	k = 1
	while i < points_length:
		j = i+1
		distance = 0.0
		while j<points_length:
			distance = distance + get_distance(float(elements[2+(j-1)*3+1]),float(elements[2+(j-1)*3+2]),float(elements[2+j*3+1]),float(elements[2+j*3+2]))
			#print(distance)
			if distance<0.3:  #distance_gap
				j=j+1
				#print("j:",j)
				continue
			else:
				s = s + elements[2+3*j] + "," + elements[3+3*j] + "," +elements[4+3*j] + ","
				k = k+1
				i = j
				#print("K:",k)
				break
		if j == points_length:
			break
	s = s + str(k) + "\n"
	#print(s)
	if k<=2:
		continue
	gps_demo.write(s)
"""
	for i  in range(int(points_length/13)):
		s = s + elements[2+3*2*i] + "," + elements[3+3*2*i] + "," +elements[4+3*2*i] + ","
	s = s + elements[length-4] + "," + elements[length-3] + "," +elements[length-2] + ","
"""
print(s_data+":Step4 OVER")
gps_demo.close()
ftele.close()

"""
ftele = open(s_data+"_V3.txt","r")
lines = ftele.readlines()
gps_demo = open(s_data+"_V4.txt","a")

for line in lines:
	elements = line.split(',')
	length = len(elements)

	s = elements[0] + "," + elements[1] + ","
	points_length = int(elements[length-1])
	i=0
	gap = 2
	for i  in range(int(points_length/gap)):
		s = s + elements[2+3*gap*i] + "," + elements[3+3*gap*i] + "," +elements[4+3*gap*i] + ","
	s = s + elements[length-4] + "," + elements[length-3] + "," +elements[-2] + ","
	s = s + str(i+2) + "\n"
	if i+2==2:
		continue
	gps_demo.write(s)
print(s_data+":Step4 OVER")
gps_demo.close()
ftele.close()
"""

"""
1,328,1407030471.0,104.109529,30.670981,1407030532.0,104.109671,30.670889,1407030571.0,104.109816,30.673707,1407030632.0,104.109376,30.675315,1407030684.0,104.109121,30.676205,1407030745.0,104.106024,30.680333,1407030774.0,104.105608,30.680064,1407030833.0,104.100241,30.680456,1407030834.0,104.100271,30.680516,9
"""

#====================Step_5===================

print(s_data+":Step_5...")
#get_distance
from math import radians, cos, sin, asin, sqrt
def get_distance(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lon1, lat1, lon2, lat2 = map(radians, map(float, [lon1, lat1, lon2, lat2]))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r


#get_time_from_unix:2016-11-01 09:46:37||2016,11,1,09,46,37
import sys,os,re
import time

def get_time_from_unix(value):
	format = '%Y,%m,%d,%H,%M,%S'
	value = time.localtime(value)
	dt = time.strftime(format,value)
	return dt


#get_week:0~6;weekID: the day of week, from 0 to 6 (Mon to Sun)||"weekID":6||"dateID":3,
from datetime import datetime
def get_week_and_dateID(line):
	string = line.split(',')
	value = int(float(string[2]))
	time_string = get_time_from_unix(value)
	time_s = time_string.split(',')

	dateID = "\"dateID\":"+str(int(time_s[2]))+','

	day_time = str(time_s[0])+str(time_s[1])+str(time_s[2])
	week = datetime.strptime(day_time,"%Y%m%d").weekday()
	week_string = "\"weekID\":"+str(week)+','
	return week_string,dateID



#get_time_difference(S) of two point,input is come from get_time_from_unix(shape is string)
def time_difference(first_point,second_point):
	s_element = first_point.split(',')
	e_element = second_point.split(',')
	s_second = int(s_element[3])*3600+int(s_element[4])*60+int(s_element[5])
	e_second = int(e_element[3])*3600+int(e_element[4])*60+int(e_element[5])
	t_d = e_second - s_second
	return t_d


#get_total_travel_time_from_start_to_end(min)
def travel_time(start,end):
	s_element = start.split(',')
	e_element = end.split(',')
	s_minute = int(s_element[3])*60+int(s_element[4])
	e_minute = int(e_element[3])*60+int(e_element[4])
	travel_time = e_minute - s_minute
	return travel_time
	

#get_minute_time:0-1439;the ID of the start time (in minute), from 0 to 1439||"timeID":1109,
def get_timeID(line):
	string = line.split(',')
	value = int(float(string[2]))
	time = get_time_from_unix(value)
	time_s = time.split(',')
	minute = int(time_s[3]) * 60 +int(time_s[4])
	minute_string = "\"timeID\":"+str(minute)
	return minute_string


#"time":1463.0,
#get_time_series_and_time:"time_gap":[0.0,40.0,80.0,120.0,291.0,322.0,360.0,561.0,680.0,821.0,892.0,930.0,950.0,971.0,1120.0,1161.0,1222.0,1230.0,1250.0,1341.0,1423.0,1463.0]
def get_time_gap_and_time(line):
	line_e = line.split(',')
	length = len(line_e)
	len_of_line = int(line_e[length-1])
	s = "\"time_gap\":[0.0,"
	start_time = get_time_from_unix(int(float(line_e[2])))
	end_time  = get_time_from_unix(int(float(line_e[2+(len_of_line-1)*3])))
	time_string = "\"time\":"+str(float(time_difference(start_time,end_time)))+','
	for i in range(len_of_line-1):
		point_time = get_time_from_unix(int(float(line_e[5+3*i])))
		time_dif = time_difference(start_time,point_time)
		if i != len_of_line -2:
			s = s + str(float(time_dif)) + ','
		else:
			s = s + str(float(time_dif)) + '],'
	return s,time_string


#get_length_of_line
def length(line):
	line_e = line.split(',')
	length = len(line_e)
	len_of_line = int(line_e[length-1])
	return len_of_line


#"lats":[30.64392,30.642129,30.64393,30.640667,30.637807,30.634062,30.630342,30.62768,3
def get_lats(line):
	line_e = line.split(',')
	length = len(line_e)
	len_of_line = int(line_e[length-1])
	s = "\"lats\":["
	for i in range(len_of_line):
		if i != len_of_line-1:
			s = s + str(line_e[4+3*i]) + ','
		else:
			s = s + str(line_e[4+3*i]) + ']'
	return s

#"lngs":[104.115353,104.113091,104.110404,104.108335,104.106304,104.104
def get_lngs(line):
	line_e = line.split(',')
	length = len(line_e)
	len_of_line = int(line_e[length-1])
	s = "\"lngs\":["
	for i in range(len_of_line):
		if i != len_of_line-1:
			s = s + str(line_e[3+3*i]) + ','
		else:
			s = s + str(line_e[3+3*i]) + ']'
	return s

#get:"dist_gap":[0.0,0.294091467,0.6199505718,1.0332595142,1.4059402503,1.8765295488,2.3477920098,2.6648681925,3.

def dist_gap_and_dist(line):
	len_line = length(line)
	lines = line.split(',')
	dis_list = [0.0]
	
	s = 0
	for i in range(len_line-1):
		lat_s = float(lines[3+3*i])
		lng_s = float(lines[4+3*i])
		lat_e = float(lines[3+3*(i+1)])
		lng_e = float(lines[4+3*(i+1)])
		dis = get_distance(lng_s,lat_s,lng_e,lat_e)
		s = s+dis
		dis_list.append(s)
	string_gap = "\"dist_gap\":"+str(dis_list)
	string_dist = "\"dist\":" + str(s)+','
	return string_gap,string_dist

#get_driverID
def get_driverID(line):
	string = line.split(',')
	return "\"driverID\":" + str(string[0])


#read_file:
def readInChunks(fileobj,chunksize=1024):
    while 1:
        data = fileobj.read(chunksize)
        if not data:
            break
        yield data

#get_random_states:
import numpy as np
def get_states(line):
	len_line = int(length(line))
	#d =  np.ones(len_line,dtype = float)
	s = "\"states\":["
	for i in range(len_line):
		if i < len_line-1:
			s = s+"1.0,"
		else:
			s = s+"1.0],"
	return str(s)

#main()
ftele = open(s_data+"_V4.txt",'r')
lines = ftele.readlines()
data_format = open(s_data+'_F','a')
file_data = ''
for line in lines:
	time_gap,time_string = get_time_gap_and_time(line)
	dist_gap,dist = dist_gap_and_dist(line)
	lats = get_lats(line)+','
	driverID = get_driverID(line)+','
	weekID,dateID= get_week_and_dateID(line)
	states = get_states(line)
   #no states
	timeID = get_timeID(line)+','
	lngs = get_lngs(line)+','
	
	one_set = "{" + time_gap + dist + lats + driverID + weekID + states + timeID + dateID + time_string + lngs + dist_gap + "}"
	file_data = one_set + '\n'
	#print(one_set)
	data_format.writelines(str(file_data))


data_format.close()
ftele.close()
print(s_data+":Step_5 OVER")
print("Formating Data Named :"+s_data+"_F")

"""
{"time_gap":[0.0,61.0,100.0,161.0,213.0,274.0,303.0,362.0,363.0],"dist":1.20631631488,"lats":[30.670981,30.670889,30.673707,30.675315,30.676205,30.680333,30.680064,30.680456,30.680516],"driverID":1,"weekID":6,"states":[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],"timeID":587,"dateID":3,"time":363.0,"lngs":[104.109529,104.109671,104.109816,104.109376,104.109121,104.106024,104.105608,104.100241,104.100271],"dist_gap":[0.0, 0.015985404526547346, 0.09405622923143381, 0.15958197565416446, 0.19681072881809253, 0.5588999108783759, 0.6057278917709679, 1.2026055660935993, 1.2063163148773803]}
"""



