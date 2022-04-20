# Copyright (c) 2022.
# -*-coding:utf-8 -*-
"""
@file: ReadCsv.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 2022/4/19 22:14
"""
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class ReadCsv:
    """
    Read S&P500 data from csv file, clean data and save each stock to a separate csv file.
    """

    FOLDER_PATH = 'sp500/'  # relative folder path for all csvs
    COMPANY_LIST = 'sp500_companies.csv'  # csv name for s&p500 companies
    STOCK_PRICE_LIST = 'sp500_stocks.csv'  # csv name for s&p500 stock price data
    SP500_INDEX = 'sp500_index.csv'  # csv name for s&p500 index data
    ANALYSIS_COL = 'Close'  # column name for analysis (Adj Close/Close)

    def __init__(self):
        """
        Initialize the class.
        """
        if self.ANALYSIS_COL == 'Adj Close':
            self.NOT_ANA_COL = 'Close'
        else:
            self.NOT_ANA_COL = 'Adj Close'
        self.sp500_list = self.read_sp500_list()
        self.all_stock_data = pd.read_csv(self.FOLDER_PATH + self.STOCK_PRICE_LIST, header=0, parse_dates=['Date'])
        self.all_stock_data.drop(['Open', 'High', 'Low', 'Volume', self.NOT_ANA_COL], axis=1, inplace=True)

    def read_sp500_list(self):
        """
        Read the S&P500 list from csv file.
        :return: a list of S&P500 symbols.
        """
        sp500_list = []
        with open(self.FOLDER_PATH + self.COMPANY_LIST, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                sp500_list.append(row[1])
        return sp500_list[1:]

    def generate_stock_csv(self, stock_symbol):
        """
        Generate a csv file for the specified stock. Calculate the daily average price and save it to a csv file.
        :param stock_symbol: the symbol of the stock.
        """
        stock_data = self.all_stock_data[self.all_stock_data['Symbol'] == stock_symbol]
        stock_data1 = stock_data[stock_data[self.ANALYSIS_COL].notna()]
        print(stock_data1)
        # stock_data['Average'] = stock_data['Close'].rolling(window=20).mean()

    def plot_stock_price(self, stock_symbol):
        """
        Plot the stock price for the specified stock.
        :param stock_symbol: the symbol of the stock.
        """
        stock_data = self.all_stock_data[self.all_stock_data['Symbol'] == stock_symbol]
        stock_data = stock_data[stock_data[self.ANALYSIS_COL].notna()]
        stock_data.plot(x='Date', y=self.ANALYSIS_COL)
        plt.show()
