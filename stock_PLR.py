#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
stock_get_data.py
Created by Huaizheng ZHANG on 7.1.
Copyright (c) 2015 zhzHNN. All rights reserved.

"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import stock_function as sf
import numpy as np

def PLR(arr,start,end,thd):
    i = start+1
    j = start+1
    k = end-1
    temp_left = arr[start]
    temp_right = arr[end]
    max = 0
    temp_max = arr[:,0][start]
    global global_PLR
    
    while arr[:,0][i] < end:
        d = sf.distance(arr[:,0][i], arr[:,2][i], arr[:,0][start], arr[:,2][start], arr[:,0][end], arr[:,2][end])
        if d > max:
            max = d
            temp_max = arr[:,0][i]
        i = i+1

    global_PLR = np.vstack((global_PLR,arr[temp_max]))

    while arr[:,0][j] < temp_max:
        temp_left = np.vstack((temp_left, arr[j]))
        j = j+1

    while arr[:,0][k] > temp_max:
        tem_right = np.vstack((arr[k], temp_right))
        k = k-1

    if max >= thd:
        PLR(temp_left, start, temp_max, thd)
        PLR(temp_right, temp_max, end, thd)
    else:
        return 

stock_code = raw_input("Please input your stockcode:")
xdata, ndata, stock_data = sf.handle_data(stock_code)

global_PLR = np.vstack((stock_data[ndata[1]][-1], stock_data[ndata[1]][0]))

PLR(stock_data, stock_data[ndata[1],0][-1], stock_data[ndata[1],0][0], 3)
print global_PLR
"""plt.rc('axes', grid=True)
plt.rc('grid', color='0.75', linestyle='-', linewidth=0.5)
textsize = 9
left, width = 0.1, 0.8
rect1 = [left, 0.4, width, 0.5]
rect2 = [left, 0.1, width, 0.3]
fig = plt.figure(figsize=(30,10), frameon = False,facecolor='white')
axescolor  = '#f6f6f6'  # the axes background color

ax1 = fig.add_axes(rect1, axisbg=axescolor)
ax1.set_xticklabels(xdata[::20], rotation=45, horizontalalignment='right')
ax1.set_xticks(stock_data[ndata[1],0][::-20])
ax1.plot(stock_data[ndata[1],0][::-1], stock_data[ndata[1],6], lw=0.5, label='average_price')
ax1.plot(stock_data[ndata[1],0][::-1], stock_data[ndata[1],2][::-1], lw=2.0, color="r", label='close_price')
ax1.plot([stock_data[ndata[1],0][-1],stock_data[ndata[1],0][0]],
         [stock_data[ndata[1],6][0],stock_data[ndata[1],6][-1]])

props = font_manager.FontProperties(size=10)
leg = ax1.legend(loc='best', shadow=True, fancybox=True, prop=props)
leg.get_frame().set_alpha(0.5)

plt.title("%sPLR"%stock_code)
plt.show()
"""
