#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
stock_get_data.py
Created by Huaizheng ZHANG on 6.27.
Copyright (c) 2015 zhzHNN. All rights reserved.

"""

import tushare as ts
import os
import urllib2
if os.path.isdir('Data'):
	pass
else:
	os.mkdir('Data')

hs300 = ts.get_hs300s()

for i in xrange(0,281):
	dirName = hs300['code'][i]
	if os.path.isdir('Data/'+dirName):
		pass
	else:
		os.mkdir('Data/'+dirName)
	try:
		print u'当前正在获取' + dirName + u'前复权训练数据'
		trainData = ts.get_h_data(hs300['code'][i], start='2011-01-04',end='2012-12-31')
		trainName = dirName + u'trainData'.encode('utf-8') + '.csv'
		if os.path.exists('Data/'+ dirName + '/' + trainName):
			os.remove('Data/'+ dirName + '/' + trainName)
		trainData.to_csv('Data/'+ dirName + '/' + trainName, encoding='utf8')
	except urllib2.URLError, e:
		print u'当前正在获取' + dirName + u'前复权训练数据'
		trainData = ts.get_h_data(hs300['code'][i], start='2011-01-04',end='2012-12-31')
		trainName = dirName + u'trainData'.encode('utf-8') + '.csv'
		if os.path.exists('Data/'+ dirName + '/' + trainName):
			os.remove('Data/'+ dirName + '/' + trainName)
		trainData.to_csv('Data/'+ dirName + '/' + trainName, encoding='utf8')

	try:
		print u'当前正在获取' + dirName + u'前复权测试数据'
		testData = ts.get_h_data(hs300['code'][i], start='2013-01-04',end='2013-12-31')
		testName = dirName + u'testData'.encode('utf-8') + '.csv'
		if os.path.exists('Data/'+ dirName + '/' + testName):
			os.remove('Data/'+ dirName + '/' + testName)
		testData.to_csv('Data/'+ dirName + '/' + testName, encoding='utf8')
	except urllib2.URLError, e:
		print u'当前正在获取' + dirName + u'前复权测试数据'
		testData = ts.get_h_data(hs300['code'][i], start='2013-01-04',end='2013-12-31')
		testName = dirName + u'testData'.encode('utf-8') + '.csv'
		if os.path.exists('Data/'+ dirName + '/' + testName):
			os.remove('Data/'+ dirName + '/' + testName)
		testData.to_csv('Data/'+ dirName + '/' + testName, encoding='utf8')
