# Copyright (c) 2022.
# -*-coding:utf-8 -*-
"""
@file: SingleStock.py
@author: Jerry(Ruihuang)Yang, Vivian Luu
@email: rxy216@case.edu, nhl16@case.edu
@time: 2022/4/20 00:38
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class SingleStock:
    """
    load data from csv file of a single stock for analysis
    """

    FOLDER_PATH = 'sp500/'  # relative folder path for all csvs
    ANALYSIS_COL = 'Close'  # column name for analysis (Adj Close/Close)
    RF_AVG_RANGE = 5  # average calculation range for determining rise or fall

    def __init__(self, stock_symbol):
        """
        init a single stock object, load data from csv file
        :param stock_symbol: stock symbol
        """
        self.cross_list = None
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
        position represents trading signal.
        when position = 1, signal change 0 -> 1 or short cross above long and stock expect to rise or buy call
        when position = -1, signal change 1 -> 0 or short cross under long and stock expect to fall or sell call
        """
        self.stock_data['Signal'] = 0.0
        self.stock_data['Signal'] = np.where(self.stock_data['Short MA'] > self.stock_data['Long MA'], 1.0, 0.0)
        self.stock_data['Position'] = self.stock_data['Signal'].diff()
        self.cross_list = self.stock_data[
            (self.stock_data['Position'] != 0.0) & (self.stock_data['Position'].notna())].copy()

    def determine_rise_or_fall(self, days):
        """
        determine rise or fall the in the specified days after cross-over
        create a new column called 'RF' to indicate rise or fall, 1 for rise, -1 for fall
        :param days: days after cross-over to determine rise or fall
        """
        s_offset = days - self.RF_AVG_RANGE  # offset from crossing day to start of average
        e_offset = days + self.RF_AVG_RANGE + 1  # offset from crossing day to end of average
        self.cross_list['RF'] = 0.0
        for i in self.cross_list.index:
            if self.stock_data[self.ANALYSIS_COL][i+s_offset:i+e_offset].mean() > self.cross_list[self.ANALYSIS_COL][i]:
                self.cross_list.loc[i, 'RF'] = 1.0
            elif self.stock_data[self.ANALYSIS_COL][i+s_offset:i+e_offset].mean() < self.cross_list[self.ANALYSIS_COL][i]:
                self.cross_list.loc[i, 'RF'] = -1.0

    def plot_cross_over(self, start_date='2010-1-1', end_date='2023-1-1'):
        """
        plot cross over signal
        """
        plot_data = self.filter_date(start_date, end_date)
        plt.figure(figsize=(20, 10))
        plot_data.plot(x='Date',
                       y=[self.ANALYSIS_COL, 'Short MA', 'Long MA'],
                       color=['k', 'b', 'c'],
                       label=[self.ANALYSIS_COL + ' Price', 'Short MA', 'Long MA'])
        plt.plot(plot_data['Date'][plot_data['Position'] == 1],
                 plot_data['Short MA'][plot_data['Position'] == 1],
                 '^',
                 markersize=7,
                 color='g',
                 label='buy')
        plt.plot(plot_data['Date'][plot_data['Position'] == -1],
                 plot_data['Short MA'][plot_data['Position'] == -1],
                 'v',
                 markersize=7,
                 color='r',
                 label='sell')
        plt.ylabel('Price in USD', fontsize=15)
        plt.xlabel('Date', fontsize=15)
        plt.legend()
        plt.grid()
        plt.show()

    def plot_stock(self, start_date='2010-1-1', end_date='2023-1-1'):
        """
        plot stock data
        :param start_date: start date of plot
        :param end_date: end date of plot
        """
        plot_data = self.filter_date(start_date, end_date)
        plot_data.plot(x='Date', y=[self.ANALYSIS_COL, 'Short MA', 'Long MA'])
        plt.legend([self.stock_symbol + ' Price', 'Short MA', 'Long MA'])
        plt.show()

    def filter_date(self, start_date='2010-1-1', end_date='2023-1-1'):
        """
        filter data by date
        :param start_date: start date of plot
        :param end_date: end date of plot
        """
        return self.stock_data[(self.stock_data['Date'] >= start_date) & (self.stock_data['Date'] <= end_date)]
