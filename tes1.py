#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 08:28:07 2021

@author: pyong
"""

import matplotlib.pyplot as plt;
import numpy as np;

import scipy.signal as sg;
from FreqResp import plotFreqResp

x = np.logspace(1,8,1000);

wn = 2*np.pi *1.5e3
num, den = sg.butter(4,wn,btype="low", analog=True, output="ba")

num2, den2 = sg.bessel(4,wn,btype="low", analog=True, output="ba")

num1, den1 = sg.cheby1(4,1.0,wn,btype="low", analog=True, output="ba")

plt.legend(["butter", "bessel", "cheby"], loc=3)

a,b = sg.step2((num,den))
plt.plot(a, b)
plt.xlabel("time")
plt.ylabel("am")
c,d =sg.step2((num1,den1))
plt.plot(c,d)
e,f =sg.step2((num2,den2))
plt.plot(e, f)