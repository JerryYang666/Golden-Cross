# Copyright (c) 2022.
# -*-coding:utf-8 -*-
"""
@file: SingleStock.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 2022/4/20 00:38
"""
import pandas as pd


class SingleStock:
    """
    load data from csv file of a single stock for analysis
    """

    FOLDER_PATH = 'sp500/'  # relative folder path for all csvs
    ANALYSIS_COL = 'Close'  # column name for analysis (Adj Close/Close)

    def __init__(self, stock_symbol):
        """
        init a single stock object, load data from csv file
        :param stock_symbol: stock symbol
        """
        if self.ANALYSIS_COL == 'Adj Close':  # set which column to use for analysis and which not
            self.NOT_ANA_COL = 'Close'
        else:
            self.NOT_ANA_COL = 'Adj Close'
        self.stock_symbol = stock_symbol
        self.stock_data = pd.read_csv(self.FOLDER_PATH + stock_symbol + '.csv', header=0, parse_dates=['Date'])
        self.stock_data.drop(['Symbol', self.NOT_ANA_COL], axis=1, inplace=True)  # drop column not used for analysis

    def calc_short_term_ma(self, days):
        """
        calculate short term moving average
        :param days: moving average days
        """
        self.stock_data['Short MA'] = self.stock_data[self.ANALYSIS_COL].rolling(days).mean()

    def calc_long_term_ma(self, days):
        """
        calculate long term moving average
        :param days: moving average days
        """
        self.stock_data['Long MA'] = self.stock_data[self.ANALYSIS_COL].rolling(days).mean()
