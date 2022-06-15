# Journal of FLuids Engineering
import sys
import time
import numpy as np
import matplotlib.pyplot as plt

params  = sys.argv[1:]
Path    = params[0] + '/postProcessing/WallCoeffsCyl1/0/forceCoeffs.dat' 

values  = np.loadtxt(Path)

xa = values[:,0]
y1 = values[:,3]
y2 = values[:,2]

plt.ion()

figure, (ax1, ax2) = plt.subplots(1,2)
line1, = ax1.plot(xa, y1, label=r'Cl $\alpha=0°$', linewidth=0.5)
line2, = ax2.plot(xa, y2, label=r'Cd $\alpha=0°$', linewidth=0.5)

ax1.set_title('Cl evolution')
ax1.set(xlabel='Time Step', ylabel='Cl')
ax1.grid(linestyle='-.', linewidth=0.5)
ax1.legend()

ax2.set_title('Cd evolution')
ax2.set(xlabel='Time Step', ylabel='Cd')
ax2.grid(linestyle='-.', linewidth=0.5)
ax2.legend()

while(len(values) < tam):
    xa = values[:, 0]
    y1 = values[:, 3]
    y2 = values[:, 2]
    
    line1.set_xdata(xa)
    line1.set_ydata(y1)
    
    line2.set_xdata(xa)
    line2.set_ydata(y2)
    
    figure.canvas.draw()
    
    figure.canvas.flush_events()
    #time.sleep(0.01)

