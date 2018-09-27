#data_cleaning
import numpy as np
from math import radians,cos ,sin,asin,sqrt
import ujson as json
import argparse


def get_point_num(elements):

    """
    get gps points number
    :param line: a track
    :return: number of the path
    """
    #elements = json.loads(line)
    time_gap = np.array(elements["time_gap"])
    return len(time_gap)

def get_distance(lon1,lat1,lon2,lat2):

    """
    Calculate the great circle distance between two points
    :param lon1:
    :param lat1:
    :param lon2:
    :param lat2:
    :return: distance (KM)
    """
    lon1, lat1, lon2, lat2 = map(radians, map(float, [lon1, lat1, lon2, lat2]))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

def get_speed(dist , time):

    """
    get speed
    :param dist: KM
    :param time: S
    :return: Km/h
    """
    time = float(time)/3600.0
    speed = dist/time
    return speed

def average_speed(elements):

    """
    get average speed of one track
    :param line: track read in lines
    :return: average_speed(Km/h)
    """
    #elements = json.loads(line)
    time = float(elements["time"])
    dist = float(elements['dist'])
    speed = get_speed(dist, time)
    return speed

def instantaneous_speed_list(elements):

    """
    get velocity between two points
    :param line: track
    :return: list of velocity
    """

    #elements = json.loads(line)
    time_gap = np.array(elements['time_gap'])
    dist_gap = np.array(elements['dist_gap'])
    l = len(time_gap)
    time_gap = np.diff(time_gap)#l-1
    dist_gap = np.diff(dist_gap)#l-1
    speed = []
    for i in range(l-1):
        speed.append(get_speed(dist_gap[i] , time_gap[i]))
    return speed

if __name__ == '__main__':
    """
    Speed upper limited : 200 Km/h
    points limit: 8 
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type = str)
    args = parser.parse_args()
    name = args.name
    
    #name = '20140803_1_demo_F_checked'
    flete1 = open(name , 'r')
    lines = flete1.readlines()
    flete2 = open(name+"_clearing",'a')
    print("there are ",len(lines)," tracks")
    short_line = 0
    speed_over = 0

    for line in lines:
        elements = json.loads(line)
        point_num = get_point_num(elements)
        if point_num < 8:
            short_line += 1
            continue
        ave_speed = average_speed(elements)
        if ave_speed > 200 :
            print("ave_speed:",ave_speed)
            speed_over +=1
            continue
        ins_speed = instantaneous_speed_list(elements)
        plm = 0
        for i in ins_speed:
            if i > 200:
                speed_over +=1
                print("Over speed :",i," Km/h")
                plm = 1
                break
        if plm == 1 :
            continue
        flete2.write(line)
    print("Data Cleaning Finsh!")
    print("Short tracks : " ,short_line)
    print("Over speed tracks : " ,speed_over)

    flete2.close()
    flete1.close()

