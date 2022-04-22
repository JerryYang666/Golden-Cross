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
import StockAnalysis
import time

if __name__ == '__main__':
    i = 0
    result = pd.DataFrame(columns=['run', 'short', 'long', 'days', 'accuracy'])
    read_csv = ReadCsv.ReadCsv()
    sp500_list = read_csv.sp500_list
    del read_csv
    for short in range(10, 21):
        for long in range(60, 101, 4):
            for days in range(4, 13):
                stock_analysis = StockAnalysis.StockAnalysis(short, long, days, sp500_list)
                accuracy = stock_analysis.accuracy
                i += 1
                result.loc[len(result.index)] = [i, short, long, days, accuracy]
                print('run ' + str(i) + ' finished with accuracy: ' + str(accuracy))
            break
        break
    print(result)
    result.to_csv("result" + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + ".csv", index=False)

    """
    single_stock = SingleStock.SingleStock("OGN")
    single_stock.calc_short_term_ma(20)
    single_stock.calc_long_term_ma(100)
    single_stock.find_cross_over()
    single_stock.plot_cross_over()
    single_stock.plot_stock()
    """
