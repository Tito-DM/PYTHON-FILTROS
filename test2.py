#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:02:35 2021

@author: pyong
"""

import matplotlib.pyplot as plt;
import numpy  as np

import scipy.signal as sg

wn = 2*np.pi *1.5e3
num, den = sg.butter(2,wn,btype="low", analog=True, output="ba")

t = np.linspace(0,4e-3,2000)

signal = 2.5*np.sin(2*np.pi*1e3*t) +  2.5*np.sin(2*np.pi*5e3*t) + 1.25*np.sin(2*np.pi*8e3*t) + 0.55*np.sin(15*1e3*t)

t1,x1,y1 = sg.lsim((num,den), U=signal, T=t)

plt.plot(t,signal,t1,x1)
plt.show()
