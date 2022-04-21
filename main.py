# Copyright (c) 2022.
# -*-coding:utf-8 -*-
"""
@file: ReadCsv.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 2022/4/19 22:14
"""
import numpy as np

import ReadCsv
import SingleStock
import pandas as pd
import StockAnalysis
import time

if __name__ == '__main__':
    start_time = time.time()
    stock_analysis = StockAnalysis.StockAnalysis()
    print("--- %s seconds ---" % (time.time() - start_time))