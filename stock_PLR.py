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

stock_code = raw_input("Please input your stockcode:")
xdata, ndata, stock_data = sf.handle_data(stock_code)
#print stock_data[ndata[1],0][0]
print sf.PLR(stock_data, stock_data[ndata[1],0][-1], stock_data[ndata[1],0][0], 10)
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
