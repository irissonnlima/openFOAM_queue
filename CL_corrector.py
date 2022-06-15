# Journal of FLuids Engineering
import sys
import time
import numpy as np
import matplotlib.pyplot as plt

def justWatch(case_name:str, lim:int, dark_mode = False):
    Path    = case_name + '/postProcessing/WallCoeffsCyl1/0/forceCoeffs.dat' 

    #plt.style.use('dark_background')

    plt.ion()
    figure, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
    line1, = ax1.plot(xa, y1, label=r'Cl $\alpha=0°$', linewidth=1)
    line2, = ax2.plot(xa, y2, label=r'Cd $\alpha=0°$', linewidth=1)

    ax1.set_title('Cl evolution')
    ax1.grid(linestyle='-.', linewidth=0.5)
    ax1.legend()

    ax2.set_title('Cd evolution')
    ax2.grid(linestyle='-.', linewidth=0.5)
    ax2.legend()

    while(len(values) < lim):
        values  = np.loadtxt(Path)
        time    = values[:, 0]
        cd      = values[:, 2]
        cl      = values[:, 3]
        
        line1.set_xdata(time)
        line1.set_ydata(cl)
        
        line2.set_xdata(time)
        line2.set_ydata(cd)
        
        figure.canvas.draw()
        
        figure.canvas.flush_events()


