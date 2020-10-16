# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:07:46 2020

@author: itoto
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import matplotlib.pyplot as plt
import importlib
from scipy.stats import skew, kurtosis, chi2
import seaborn as sns

# input
ric = "DBK.DE"
path = "C:\\Users\\itoto\\Documents\\Python Scripts\\Seminario de Finanzas\\" + ric +".csv"
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

sns.distplot(x)


# compute "risk metrics"
x_mean = np.mean(x)
x_stdev = np.std(x)
x_skew = skew(x)
x_kurt = kurtosis(x)  #excess kurtosis (cuando se restan 3)
x_sharpe = x_mean / x_stdev * np.sqrt(252)
x_var_95= np.percentile(x,5)
x_cvar_95 = np.mean(x[x<= x_var_95])
jb = x_size/6*(x_skew**2 + 1/4*x_kurt**2)
p_value = 1 - chi2.cdf(jb, df = 2)
is_normal = (p_value > 0.05)

# print metrics
print("mean " + str(x_mean))
print("std " + str(x_stdev))
print("skewness " + str(x_skew))
print("kurtosis " + str(x_kurt))
print("Sharpe " + str(x_sharpe))
print("VaR 95% " + str(x_var_95))
print("CVaR 95% " + str(x_cvar_95))
print("Jarque-Bera " + str(jb))
print("is normal " + str(is_normal))


# plot histogram
plt.figure()
plt.hist(x,bins=100)
plt.title("histogram " + x_str)
plt.show()

