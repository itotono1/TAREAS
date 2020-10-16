# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 09:09:42 2020

@author: itoto
"""
import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import matplotlib.pyplot as plt
import importlib
from scipy.stats import skew, kurtosis, chi2

import stream_functions
importlib.reload(stream_functions)


class jarque_bera_test():
    
    def _init_(self,x,x_str): #constructor
        self.returns = x
        self.str_name = x_str    
        self.size = len(x)
        
        
    def compute(self):
        self.mean = np.mean(self.returns)
        self.std = np.std(self.returns)
        self.skew = skew(self.returns)
        self.kurt = kurtosis(self.returns)  #eself.returnscess kurtosis (cuando se restan 3)
        self.sharpe = self.mean / self.stdev * np.sqrt(252)
        self.median = np.median(self.returns)
        self.var_95= np.percentile(self.returns,5)
        self.cvar_95 = np.mean(self.returns[self.returns<= self.var_95])
        self.jarque_bera = self.size/6*(self.skew**2 + 1/4*self.kurt**2)
        self.p_value = 1 - chi2.cdf(self.jarque_bera, df = 2)
        self.is_normal = (self.p_value > 0.05)

    def _str_(self): #para plot
        print_self = self.str_name 