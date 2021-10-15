import numpy as np;
import matplotlib.pyplot as plt;
import scipy.signal  as sg;
from FreqResp import plotFreqResp;

x = np.logspace(1,8,1000);
wn = 2*np.pi*1.5e3;
num, den = sg.butter(4, wn,btype="low", analog=True, output="ba");
plotFreqResp(x, num, den);
plt.show();