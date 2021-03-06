#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
stock_PLR_plot.py
Created by Huaizheng ZHANG on 7.9.
Copyright (c) 2015 zhzHNN. All rights reserved.

"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import stock_GA_multi as sGm

if __name__ == '__main__':
    # 种群的个体数量为 50，染色体长度为 23，交叉概率为 0.9，变异概率为 0.5,进化最大世代数为 50
    pop = sGm.GA (50, 23, 0.9, 0.4, 50)
    stock_data2, xdata, ndata, stock_data, stock_code = pop.run ()


plt.rc('axes', grid=True)
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
