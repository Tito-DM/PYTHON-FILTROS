import numpy as np;
import matplotlib.pyplot as plt;
from numpy.core.numeric import convolve;

y= [0,1,-1,1,-1];
h = [1,-1,0,0,0];
convolution = np.convolve(y,h);

x = np.arange(len(convolution));

plt.stem(x,convolution,use_line_collection = True);
plt.show();