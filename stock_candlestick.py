#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
stock_get_data.py
Created by Huaizheng ZHANG on 7.1.
Copyright (c) 2015 zhzHNN. All rights reserved.

"""
import numpy as np
import matplotlib.pyplot as plt
import datetime
from matplotlib.finance import candlestick
from matplotlib.dates import strpdate2num,num2date
import matplotlib.font_manager as font_manager


data = np.loadtxt('Data/000024/000024trainData.csv', delimiter=',', skiprows=1, converters = {0: strpdate2num("%Y-%m-%d")})
temp = data[:,0].tolist()

# determine number of days and create a list of those days
ndays = np.unique(temp, return_index=True)
xdays =  []
for n in np.arange(len(ndays[0])):
    xdays.append(datetime.date.isoformat(num2date(data[ndays[1],0][n])))

# creation of new data by replacing the time array with equally spaced values.

# this will allow to remove the gap between the days, when plotting the data
data2 = np.hstack([np.arange(data[:,0].size)[:, np.newaxis], data[:,1:-1][::-1]])
for c in np.arange(len(ndays[0])):
    data2[c][2], data2[c][3] = data2[c][3], data2[c][2]


plt.rc('axes', grid=True)
plt.rc('grid', color='0.75', linestyle='-', linewidth=0.5)
textsize = 9
left, width = 0.1, 0.8
rect1 = [left, 0.4, width, 0.5]
rect2 = [left, 0.1, width, 0.3]

fig = plt.figure(figsize=(30,10), frameon = False,facecolor='white')
axescolor  = '#f6f6f6'  # the axes background color
ax1 = fig.add_axes(rect1, axisbg=axescolor)  #left, bottom, width, height
ax2 = fig.add_axes(rect2, axisbg=axescolor, sharex=ax1)

for ax in ax1, ax2:
    if ax!=ax2:
        for label in ax.get_xticklabels():
            label.set_visible(False)
    else:
        ax.set_xticklabels(xdays[::20], rotation=45, horizontalalignment='right')
    ax.set_xticks(data2[ndays[1],0][::-20])

candlestick(ax1, data2, width=0.5, colorup='r', colordown='g')
ax2.plot(data2[ndays[1],0][::-1], (data2[ndays[1],1][::-1]+data2[ndays[1],2][::-1]+data2[ndays[1],3][::-1]+data2[ndays[1],4][::-1])/4,
        lw=2, label='average_price')
ax2.plot(data2[ndays[1],0][::-1], data2[ndays[1],2][::-1], lw=0.5, color="r", label='close_price')

props = font_manager.FontProperties(size=10)
leg = ax2.legend(loc='best', shadow=True, fancybox=True, prop=props)
leg.get_frame().set_alpha(0.5)

plt.title("000001trainData")
plt.show()
