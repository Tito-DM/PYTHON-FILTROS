#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:53:09 2021

@author: pyong
"""

import matplotlib.pyplot as plt;
import numpy  as np

import scipy.signal as sg

from FreqResp import plotFreqResp


n,wn = sg.buttord([1e4,1e5], [5e2,2e5], 1, 30,analog=True, fs=None)

x = np.logspace(1,8,1000)
num, den = sg.butter(n,wn,btype="band", analog=True, output="ba")

t = np.linspace(0,4e-3,2000)


plotFreqResp(x,num, den)


plt.show()
