import numpy as np;
import matplotlib.pyplot as plt;
import scipy.signal as sg;

def plotFreqResp(x,b,a):
    w,h=sg.freqs(b,a,worN=x,plot=None);
    plt.subplot(211);
    plt.semilogx(w, 20 * np.log10(abs(h)));
    plt.ylabel("Amplitude [dB]");
    plt.grid();
    plt.subplot(2,1 ,2);
    phase=np.arctan2(np.imag(h),np.real(h));
    phaseDeg = np.rad2deg(phase);
    plt.semilogx(w, phaseDeg);
    plt.xlabel("Frequency [rad/s");
    plt.ylabel("phase [degree]");
    plt.grid();
    plt.show();