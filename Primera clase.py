# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:20:40 2020

@author: itotono
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import matplotlib.pyplot as plt
import importlib
from scipy.stats import skew, kurtosis, chi2

'''
Gool: create a normality test e.g. Jarque-Bera

step 1: simulate random variable
step 2: visualise histogram
step 3: what is Jarque-Bera
'''

# is_normal = True
# counter = 0
# while is_normal and counter < 3:
    # generate random variable
x_size = 10**6
degrees_freedom = 500
type_random_variable = "normal"

if type_random_variable == "normal":
    x = np.random.standard_normal(x_size)
    x_str = type_random_variable
elif type_random_variable == "exponential":
    x = np.random.standard_exponential(x_size)
    x_str = type_random_variable
elif type_random_variable == "chi-squared":
    x = np.random.chisquare(size=x_size, df=degrees_freedom)
    x_str = type_random_variable + "(df=" + str(degrees_freedom) + ")" 
else:
    x = np.random.standard_t(size=x_size, df=degrees_freedom)
    x_str = type_random_variable + "(df=" + str(degrees_freedom) + ")" 

# compute "risk metrics"
x_mean = np.mean(x)
x_stdev = np.std(x)
x_skew = skew(x)
x_kurt = kurtosis(x)  #excess kurtosis (cuando se restan 3)
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
print("VaR 95% " + str(x_var_95))
print("CVaR 95% " + str(x_cvar_95))
print("Jarque-Bera " + str(jb))
print("is normal " + str(is_normal))


# plot histogram
plt.figure()
plt.hist(x,bins=100)
plt.title("histogram " + x_str)
plt.show()

# counter +=1
# print(str(counter))
# print("----------")




