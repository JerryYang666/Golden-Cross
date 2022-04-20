# Copyright (c) 2022.
# -*-coding:utf-8 -*-
"""
@file: ReadCsv.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 2022/4/19 22:14
"""
import ReadCsv
import pandas as pd

if __name__ == '__main__':
    ReadCsv = ReadCsv.ReadCsv()
    ReadCsv.plot_stock_price("T")
