#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:09:09 2021

@author: pyong
"""
#sinc(x)=sin(pi*x)/(pi*x)
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg
from plotFreqResp import myfreqz

wc = np.pi/2 #frequêcnia de corte
fc = wc/(2*np.pi) #corverter por hz
M = 11 
n= np.arange(M)
tau =(M-1)/2
x=n-tau
hd = 2*fc* np.sinc(2*fc*(n-tau))
w=sg.windows.get_window('boxcar', 11)
plt.title('rectangular window')
plt.Figure()
plt.stem(n,w)
plt.xlabel('n')
plt.ylabel('w[n')
plt.grid()
h=hd*w
print(h)
plt.stem(n,h,'r')

myfreqz(hd,1)