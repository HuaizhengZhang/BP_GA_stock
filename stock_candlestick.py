#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
stock_get_data.py
Created by Huaizheng ZHANG on 7.1.
Copyright (c) 2015 zhzHNN. All rights reserved.

"""

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick
import matplotlib.font_manager as font_manager
import stock_function as sf


stock_code = raw_input("Please input your stockcode:")
xdata, ndata, stock_data = sf.handle_data(stock_code)

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
        ax.set_xticklabels(xdata[::20], rotation=45, horizontalalignment='right')
    ax.set_xticks(stock_data[ndata[1],0][::-20])

candlestick(ax1, stock_data, width=0.5, colorup='r', colordown='g')
ax2.plot(stock_data[ndata[1],0][::-1], stock_data[ndata[1],6],lw=2, label='average_price')
ax2.plot(stock_data[ndata[1],0][::-1], stock_data[ndata[1],2][::-1], lw=0.5, color="r", label='close_price')

props = font_manager.FontProperties(size=10)
leg = ax2.legend(loc='best', shadow=True, fancybox=True, prop=props)
leg.get_frame().set_alpha(0.5)

plt.title("%strainData"%stock_code)
plt.show()
