# Copyright (c) 2022.
# -*-coding:utf-8 -*-
"""
@file: ReadCsv.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 2022/4/19 22:14
"""
import ReadCsv
import SingleStock
import pandas as pd

if __name__ == '__main__':
    # read_csv = ReadCsv.ReadCsv()
    single_stock = SingleStock.SingleStock("T")
    single_stock.calc_short_term_ma(20)
    single_stock.calc_long_term_ma(100)
    single_stock.find_cross_over()
    single_stock.plot_stock()
    single_stock.plot_cross_over('2020-01-01', '2021-01-01')

