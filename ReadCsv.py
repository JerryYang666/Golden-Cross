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
        self.sp500_list = self.read_sp500_list()
        self.all_stock_data = pd.read_csv(self.FOLDER_PATH + self.STOCK_PRICE_LIST, header=0, parse_dates=['Date'])
        self.all_stock_data.drop(['Open', 'High', 'Low', 'Volume'], axis=1, inplace=True)  # drop useless columns

    def read_sp500_list(self):
        """
        Read the S&P500 list from csv file. Since 500 rows is not a large number, no need to use pandas.
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
        stock_data = self.single_stock_df(stock_symbol)
        stock_data.to_csv(self.FOLDER_PATH + stock_symbol + '.csv', index=False)

    def generate_csv(self):
        """
        Generate a csv file for each of the stocks.
        """
        for stock in self.sp500_list:  # generate csvs for each stock
            self.generate_stock_csv(stock)
            print('Generated csv file for ' + stock)

    def plot_stock_price(self, stock_symbol, start_date='2010-1-1', end_date='2023-1-1'):
        """
        Plot the stock price for the specified stock.
        :param start_date: start date of the plot.
        :param end_date: end date of the plot.
        :param stock_symbol: the symbol of the stock.
        """
        stock_data = self.single_stock_df(stock_symbol)
        stock_data = stock_data[(stock_data['Date'] >= start_date) & (stock_data['Date'] <= end_date)]
        stock_data.plot(x='Date', y=self.ANALYSIS_COL)
        plt.show()

    def single_stock_df(self, stock_symbol):
        """
        Get the dataframe of the specified stock. drop NaN rows.
        :param stock_symbol: the symbol of the stock.
        :return: the dataframe of the specified stock.
        """
        stock_data = self.all_stock_data[self.all_stock_data['Symbol'] == stock_symbol]
        stock_data = stock_data[stock_data[self.ANALYSIS_COL].notna()]  # drop NaN rows
        return stock_data
