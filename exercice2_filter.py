#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 23:47:54 2021

@author: pyong
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg
import plotFreqResp

import math

wc1 = 30*np.pi #30pi
wc2 = 45*np.pi #40pi
fs=1e2 # eq 100

#normalized frequency
w1 = wc1/fs
w2 = wc2/fs

print('w1=',w1)
print('w2=',w2)
A1=50 #bd
window='Hamming'
M=8*np.pi/w2-w1
M1=math.ceil(M)
if M1%2==0:
    M1=M1+1

a=sg.firwin(M1,cutoff=w1,window="hamming")
plotFreqResp.myfreqz(a, 1)


