# Copyright (c) 2022.
# -*-coding:utf-8 -*-
"""
@file: StockAnalysis.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 2022/4/21 18:40
"""
import ReadCsv
import SingleStock
from os import path


class StockAnalysis:
    """
    Analysis all the stocks with the given parameters and get the result.
    """

    def __init__(self, short_term_days=20, long_term_days=100, days_after_cross=10):
        """
        Initialize the analysis with the set of given parameters
        :param short_term_days: the length of short term moving average
        :param long_term_days: the length of long term moving average
        :param days_after_cross: x days after crossing to determine rise or fall
        """
        self.short_term_days = short_term_days
        self.long_term_days = long_term_days
        self.days_after_cross = days_after_cross
        read_csv = ReadCsv.ReadCsv()
        if not path.exists(read_csv.FOLDER_PATH + "T.csv"):
            read_csv.generate_csv()
        self.sp500_list = read_csv.sp500_list
        analysis_result = self.analysis()
        print(sum(analysis_result.values())/len(analysis_result))

    def analysis(self):
        """
        Analysis all the stocks with the given parameters and get the result.
        :return: the result of analysis
        """
        result = {}
        for stock in self.sp500_list:
            single_stock = SingleStock.SingleStock(stock)
            result[stock] = self.analysis_single_stock(single_stock)
            print(f'{stock}: {result[stock]}')
        return result

    def analysis_single_stock(self, single_stock):
        """
        do the analysis process for one stock and calculate the accuracy
        :param single_stock: an instance of SingleStock.py
        :return: the prediction accuracy of this stock
        """
        single_stock.calc_short_term_ma(self.short_term_days)
        single_stock.calc_long_term_ma(self.long_term_days)
        single_stock.find_cross_over()
        single_stock.determine_rise_or_fall(self.days_after_cross)
        result = single_stock.cross_list
        accuracy = round(result[result['Position'] == result['RF']].count()['Date'] / result.count()['Date'], 4)
        return accuracy
