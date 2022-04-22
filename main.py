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
    stock_analysis = StockAnalysis.StockAnalysis(17, 100, 6)
    print("--- %s seconds ---" % (time.time() - start_time))
    """
    single_stock = SingleStock.SingleStock("T")
    single_stock.calc_short_term_ma(20)
    single_stock.calc_long_term_ma(100)
    single_stock.find_cross_over()
    single_stock.plot_cross_over()
    single_stock.plot_stock()
    """