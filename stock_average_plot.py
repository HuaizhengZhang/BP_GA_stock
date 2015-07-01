"""
stock_matplot.py
Created by Huaizheng ZHANG on 6.27.
Copyright (c) 2015 zhzHNN. All rights reserved.

"""
import numpy as np
from matplotlib.mlab import csv2rec
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.ticker import Formatter
from datetime import datetime

d,close = np.loadtxt('Data/000001/000001trainData.csv', delimiter=',', skiprows=1, usecols=(0,3), unpack=True, dtype=str)

class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%Y-%m-%d'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(round(x))
        if ind>=len(self.dates) or ind<0: return ''

        return self.dates[ind].strftime(self.fmt)

formatter = MyFormatter(d)

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(formatter)
ax.plot(np.arange(len(d)), close, 'o-')
fig.autofmt_xdate()
plt.show()
