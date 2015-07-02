#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
stock_get_data.py
Created by Huaizheng ZHANG on 7.2.
Copyright (c) 2015 zhzHNN. All rights reserved.

"""
import numpy as np
import datetime
from matplotlib.dates import strpdate2num,num2date
import math

def handle_data(filename):
    data = np.loadtxt('Data/%s/%strainData.csv'%(filename,filename), delimiter=',', skiprows=1, converters = {0: strpdate2num("%Y-%m-%d")})
    temp = data[:,0].tolist()
    ndays = np.unique(temp, return_index=True)
    xdays =  []
    for n in np.arange(len(ndays[0])):
        xdays.append(datetime.date.isoformat(num2date(data[ndays[1],0][n])))
    data_new = np.hstack([np.arange(data[:,0].size)[:, np.newaxis], data[:,1:][::-1]])
    for c in np.arange(len(ndays[0])):
        data_new[c][2], data_new[c][3] = data_new[c][3], data_new[c][2]
        data_new[c][6] = (data[c][1]+data[c][2]+data[c][3]+data[c][4])/4
    return xdays,ndays,data_new

def distance(x, y, Ax, Ay, Bx, By):
    dis = (math.fabs((By-Ay)*x + (Ax-Bx)*y + ((Bx*Ay)-(Ax*By)))) / math.hypot((By-Ay),(Ax-Bx))
    return dis


def PLR(arr,start,end,thd):
    i = start
    j = start
    k = end
    temp_left = arr[start]
    temp_right = arr[end]

    while arr[:,0][i] < end:
        max = 0
        temp_max = arr[:,0][start]
        d = distance(arr[:,0][i], arr[:,2][i], arr[:,0][start], arr[:,2][start], arr[:,0][end], arr[:,2][end])
        if d > max:
            max = d
            temp_max = arr[:,0][i]
        i = i+1

    while arr[:,0][j] <= temp_max:
        temp_left = np.vstack((temp_left, arr[j]))
        j = j+1

    while arr[:,0][k] > temp_max:
        tem_right = np.vstack((arr[k], temp_right))
        k = k-1

    if max >= thd:
        PLR(temp_left, start, temp_max, thd)
        PLR(temp_right, temp_max, end, thd)
    else:
        return temp_max
