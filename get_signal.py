import h5py
import matplotlib.pyplot as plt
import numpy as np
import copy


h5fy_name = '0905_unspedific.fast5'
h5        = h5py.File(h5fy_name)

path_signal = 'Raw/Reads/Read_247/Signal'
path_fastq  = 'Analyses/Basecall_1D_000/BaseCalled_template/Fastq'

signal   = h5[path_signal].value
sequence = h5[path_fastq].value

np.save('current_signal.npy',signal)
print(len(signal))
print(len(sequence))

interval = 3000
start_1  = 3000
start_2  = 73000

signal_show  = [0]*4
axis_x       = [0]*4

for i in range(0,2):
    end = start_1 + interval    
    signal_show[i] = signal[start_1:end]
    axis_x[i]      = np.linspace(start_1,end,interval)    
    start_1 += interval
for i in range(2,4):
    end = start_2 + interval    
    signal_show[i] = signal[start_2:end]
    axis_x[i]      = np.linspace(start_2,end,interval)    
    start_2 += interval    

fig = plt.figure("Current Value")

ax  = fig.add_subplot(4,1,1)
bx  = fig.add_subplot(4,1,2)
cx  = fig.add_subplot(4,1,3)
dx  = fig.add_subplot(4,1,4)

ax.scatter(axis_x[0],signal_show[0], marker = 'x', color = 'r', label='1', s = 1)
bx.scatter(axis_x[1],signal_show[1], marker = 'x', color = 'r', label='1', s = 1)
cx.scatter(axis_x[2],signal_show[2], marker = 'x', color = 'r', label='1', s = 1)
dx.scatter(axis_x[3],signal_show[3], marker = 'x', color = 'r', label='1', s = 1)

plt.show()








