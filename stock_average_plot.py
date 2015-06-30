"""
stock_matplot.py
Created by Huaizheng ZHANG on 6.27.
Copyright (c) 2015 zhzHNN. All rights reserved.

"""
import string
import matplotlib.pyplot as plt
import numpy as np


Data = np.loadtxt('Data/000001/000001testData.csv', skiprows = 1, dtype=str)


years = [Data['date'][x] for x in length(Data['date'])]
print(years)
price = [Data['close'][x] for x in linesList(Data['close'])]
print(price)
plt.plot(years, price, 'b*')#,label=$cos(x^2)$)
plt.plot(years, price, 'r')
plt.xlabel(years(+2000))
plt.ylabel('housing average price(*2000 yuan)')
plt.ylim(0, 15)
plt.title('line_regression & gradient decrease')
plt.legend()
plt.show()
