import h5py
import matplotlib.pyplot as plt
import numpy as np
import copy

from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from signal_allign_DTW import end_2_end

##############################

signal = np.load('current_signal.npy')

f1  = signal[4100:5200]
f1x = np.linspace(1,len(f1),len(f1))

f2  = signal[6200:7300]
f2x = np.linspace(1,len(f2),len(f2))

f3  = signal[72900:74000]
f3x = np.linspace(1,len(f3),len(f3))

path_1,value_1 = end_2_end(f1,f2)
path_2,value_2 = end_2_end(f3,f2)

# show raw data
fig = plt.figure("signal")
ax  = fig.add_subplot(3,1,1)
bx  = fig.add_subplot(3,1,2)
cx  = fig.add_subplot(3,1,3)

ax.plot(f1x,f1)
bx.plot(f2x,f2)
cx.plot(f3x,f3)



#show f1 vs f2 align
plt.figure("align_f1_f2")

line1 = plt.plot(path_1[1],value_1[1],linewidth=1.5, linestyle=':', color='b')
line2 = plt.plot(path_1[1],value_1[0],linewidth=1.5, linestyle=':', color='r')

plt.legend([line1,line2],["1","2"])


#show f2 vs f3 align
plt.figure("align_f2_f3")
line3 = plt.plot(path_2[1],value_2[1],linewidth=1.5, linestyle=':', color='b')
line4 = plt.plot(path_2[1],value_2[0],linewidth=1.5, linestyle=':', color='r')

plt.legend([line3,line3],["3","2"])


#show f1_vs_f2 vs f3 align
plt.figure("align_f1_f2_f3")
linea = plt.plot(path_1[1],value_1[1],linewidth=1.5, linestyle=':', color='g')
lineb = plt.plot(path_1[1],value_1[0],linewidth=1.0, linestyle=':', color='r')
linec = plt.plot(path_2[1],value_2[0],linewidth=1.0, linestyle=':', color='b')

plt.legend([linea,lineb,linec],["1","2","3"])

plt.show()










