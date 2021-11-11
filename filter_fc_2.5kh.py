#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 23:15:34 2021

@author: pyong
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg
import plotFreqResp


#filter order-N =10
#sampling fraquency-fs=20khz
#passband cut-off frequency-fc=2.5khz
#window: rectangular

wc = 2.5e3*np.pi
fs = 2e4
w1=wc/fs
print('w1=',w1)
M=11
a=sg.firwin(M, cutoff=w1,window="boxcar")
plotFreqResp.myfreqz(a, 1)