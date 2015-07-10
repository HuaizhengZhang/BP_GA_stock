#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
stock_trading_signal.py
Created by Huaizheng ZHANG on 7.9.
Copyright (c) 2015 zhzHNN. All rights reserved.

"""
import numpy as np
class TradingSignal:
    """docstring for SRA"""
    def __init__(self, arr_stock):
        self.stockdata = arr_stock
        self.uptrend = arr_stock[0]
        self.trend = arr_stock[0]


    def updown(self):
        i = 1
        while i < len(self.stockdata):
            pass
