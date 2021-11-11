#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:47:15 2021

@author: pyong
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg



def myfreqz(b,a):
    plt.figure()
    w,h = sg.freqz(b,a)
    h_db = 20 * np.log10 (abs(h))
    plt.subplot(211)
    plt.plot(w/max(w),h_db)
    plt.ylim(-60,5)
    plt.ylabel('Magnitude (db)')
    plt.title('frequency response')
    plt.grid()
    plt.subplot(211)
    h_Phase = np.unwrap(np.arctan2(np.imag(h),np.real(h)))
    plt.plot(w/max(w),h_Phase)
    plt.ylabel('Phase (radians)')
    plt.xlabel(r'Normalized frequency (x$\pi$rad/sample)')
    plt.title(r'Phase response')
    plt.subplots_adjust(hspace=0.5)
    plt.grid()