#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
stock_PLR.py
Created by Huaizheng ZHANG on 7.1.
Copyright (c) 2015 zhzHNN. All rights reserved.

"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import stock_function as sf
import numpy as np

def PLR(start, end, thd):
    global stock_data
    global global_PLR
    i = start+1
    max = 0
    temp_max = []

    while stock_data[:,0][i] < end:
        d = sf.distance(stock_data[:,0][i],
                        stock_data[:,2][i],
                        stock_data[:,0][start],
                        stock_data[:,2][start],
                        stock_data[:,0][end],
                        stock_data[:,2][end])
        if d >= max:
            max = d
            temp_max = stock_data[:,0][i]
        i = i+1

    if max >= thd:
        global_PLR.append(temp_max)
        return
    else:
        return

def PLR_sort(thd):
    global global_PLR
    temp_sort = global_PLR[:]
    temp_sort.sort()
    j = 0

    while j < len(temp_sort)-1:
        if (temp_sort[j+1] - temp_sort[j]) > 2:
            PLR(temp_sort[j], temp_sort[j+1], thd)
        j = j+1

    return

def PLR_main(thd):
    compare_global_PLR = []
    global global_PLR
    global stock_data
    global ndata
    global xdata
    global stock_code
    while len(compare_global_PLR) != len(global_PLR):
        compare_global_PLR = global_PLR[:]
        PLR_sort(thd)

    p = sorted(global_PLR)
    temp_data = stock_data[ndata[1]][-1]
    for i in np.arange(len(p)):
        temp_data = np.vstack((temp_data,stock_data[p[i]]))

    profit = 1
    m = 0
    while m < len(temp_data)-1:
        if temp_data[:,2][m] < temp_data[:,2][m+1]:
            profit = profit * (1 + (((1-0.001)*temp_data[:,2][m+1] - temp_data[:,2][m] * (1+0.001))/temp_data[:,2][m]))
            m = m+1
        else:
            m = m+1
    temp_data = np.delete(temp_data, 0, 0)

    print profit
    return profit, temp_data, xdata, ndata, stock_data, stock_code






#input stock_code
stock_code = raw_input("Please input your stockcode:")
xdata, ndata, stock_data = sf.handle_data(stock_code)

#init data
global_PLR = [stock_data[:,0][0], stock_data[:,0][-1]]


"""p = PLR_main()

print p"""
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
ax1.plot(stock_data[ndata[1],0][::-1], stock_data[ndata[1],6], lw=1, color="g", label='average_price')
ax1.plot(stock_data[ndata[1],0][::-1], stock_data[ndata[1],2][::-1], lw=2.0, color="r", label='close_price')
ax1.plot(stock_data2[:,0][::-1], stock_data2[:,2][::-1],lw=1.0, color="b",label='PLR')

props = font_manager.FontProperties(size=10)
leg = ax1.legend(loc='best', shadow=True, fancybox=True, prop=props)
leg.get_frame().set_alpha(0.5)

plt.title("%sPLR"%stock_code)
plt.show()
"""
