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


class ReadCsv:
    """
    Read S&P500 data from csv file, clean data and save each stock to a separate csv file.
    """

    FOLDER_PATH = 'sp500/'  # relative folder path for all csvs
    COMPANY_LIST = 'sp500_companies.csv'  # csv name for s&p500 companies
    STOCK_PRICE_LIST = 'sp500_stocks.csv'  # csv name for s&p500 stock price data
    SP500_INDEX = 'sp500_index.csv'  # csv name for s&p500 index data

    def __init__(self):
        """
        Initialize the class.
        """
        self.sp500_list = self.read_sp500_list()

    def read_sp500_list(self):
        """
        Read the S&P500 list from csv file.
        :return: a list of S&P500 symbols.
        """
        sp500_list = []
        with open(self.FOLDER_PATH+self.COMPANY_LIST, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                sp500_list.append(row[1])
        return sp500_list[1:]

    def generate_stock_csv(self, stock_symbol):
        """
        Generate a csv file for the specified stock. Calculate the daily average price and save it to a csv file.
        :param stock_symbol: the symbol of the stock.
        """
        stock_data = pd.read_csv(self.folder_path+"/"+stock_symbol+".csv")
        stock_data.to_csv(self.folder_path+"/"+stock_symbol+".csv")

