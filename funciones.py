# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:39:56 2020

@author: itoto
"""
import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import matplotlib.pyplot as plt
import importlib
from scipy.stats import skew, kurtosis, chi2


def load_timeseries(ric, file_extension):
    # input
    path = "C:\\Users\\itoto\\Documents\\Python Scripts\\Seminario de Finanzas\\" + ric + file_extension
    table_row = pd.read_csv(path)
    
    # table or returns
    t = pd.DataFrame()
    t["Date"] = pd.to_datetime(table_row["Date"])
    t["Close"] = table_row["Close"]
    t["Close_previous"] = table_row["Close"].shift(1)
    t["return_close"] = t["Close"]/t["Close_previous"] -1
    t = t.dropna()
    t = t.reset_index(drop=True)
    
    plt.figure()
    plt.plot(t["Date"],t["Close"])
    plt.title("Time series real prices "+ric)
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()
    
    # get market data
    
    x = t["return_close"].values
    x_str = "Real returns " + ric
    x_size = len(x)
    
    return x, x_str, t
    
