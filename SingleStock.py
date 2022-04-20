# Copyright (c) 2022.
# -*-coding:utf-8 -*-
"""
@file: SingleStock.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 2022/4/20 00:38
"""
import pandas as pd
import matplotlib.pyplot as plt


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

    def find_cross_over(self):
        """
        find crossing of moving average, must use after calc_short_term_ma and calc_long_term_ma
        There are two types of cross-over: short cross over long, short cross under long
        for short cross over long, we expect the stock to rise, for short cross under long, we expect the stock to fall
        """
        pass

    def determine_rise_or_fall(self, days):
        """
        determine rise or fall the in the specified days after cross-over
        :param days: days to determine rise or fall
        """
        pass

    def plot_stock(self, start_date='2010-1-1', end_date='2023-1-1'):
        """
        plot stock data
        :param start_date: start date of plot
        :param end_date: end date of plot
        """
        plot_data = self.stock_data[(self.stock_data['Date'] >= start_date) & (self.stock_data['Date'] <= end_date)]
        plot_data.plot(x='Date', y=[self.ANALYSIS_COL, 'Short MA', 'Long MA'])
        plt.legend([self.stock_symbol + ' Price', 'Short MA', 'Long MA'])
        plt.show()
