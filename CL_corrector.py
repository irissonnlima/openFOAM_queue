# Journal of FLuids Engineering
import numpy as np
import matplotlib.pyplot as plt

def curva_derivada(x:np.array,y:np.array):
    d = []
    for i in range(1, len(x)):
        d.append((y[i]-y[i-1])/(x[i]-x[i-1]))
    return np.array(d)
 
def start_cl_dcl_watch (file_path:str, lim:int, last:int=-500) -> tuple:
    Path    = file_path + '/postProcessing/WallCoeffsCyl1/0/forceCoeffs.dat'
    values  = np.loadtxt(Path)
    time    = values[:, 0]
    cd      = values[:, 2]
    cl      = values[:, 3]
    dcl     = curva_derivada(time,cl)
    dcd     = curva_derivada(time,cd)
    print(len(values))
    figure, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
    
    ax1.plot(time[last:], cl[last:], label=r'Cl $\alpha=°$', linewidth=1)
    ax1.set_title('Cl evolution')
    ax1.grid(linestyle='-.', linewidth=0.5)
    ax1.legend()
    
    ax2.plot(time[last:], cd[last:], label=r'Cd $\alpha=°$', linewidth=1)
    ax2.set_title('Cd evolution')
    ax2.grid(linestyle='-.', linewidth=0.5)
    ax2.legend()
    
    ax3.plot(time[last:], dcl[last:], label=r'dCl $\alpha=°$', linewidth=1)
    ax3.set_title('Cl derivation evolution')
    ax3.grid(linestyle='-.', linewidth=0.5)
    ax3.legend()
    
    ax4.plot(time[last:], dcd[last:], label=r'dCd $\alpha=°$', linewidth=1)
    ax4.set_title('Cd derivation evolution')
    ax4.grid(linestyle='-.', linewidth=0.5)
    ax4.legend()
    plt.show()
    return figure, ax1, ax2, ax3, ax4
    
def justWatch(case_name:str, lim:int, dark_mode = False):
    Path    = case_name + '/postProcessing/WallCoeffsCyl1/0/forceCoeffs.dat' 

    #plt.style.use('dark_background')
    values  = np.loadtxt(Path)
        
    plt.ion()
    figure, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
    
    while(len(values) < lim):
        values  = np.loadtxt(Path)
        time    = values[:, 0]
        cd      = values[:, 2]
        cl      = values[:, 3]
        dcl     = curva_derivada(time,cl)
        dcd     = curva_derivada(time,cd)
        
        ax1.cla()
        ax1.plot(time, cl, label=r'Cl $\alpha=°$', linewidth=1)
        ax1.set_title('Cl evolution')
        ax1.grid(linestyle='-.', linewidth=0.5)
        ax1.legend()
        
        ax2.cla()
        ax2.plot(time, cd, label=r'Cd $\alpha=°$', linewidth=1)
        ax2.set_title('Cd evolution')
        ax2.grid(linestyle='-.', linewidth=0.5)
        ax2.legend()
        
        ax3.cla()
        ax3.plot(time[1:], dcl, label=r'dCl $\alpha=°$', linewidth=1)
        ax3.set_title('Cl derivation evolution')
        ax3.grid(linestyle='-.', linewidth=0.5)
        ax3.legend()
        
        ax4.cla()
        ax4.plot(time[1:], dcd, label=r'dCd $\alpha=°$', linewidth=1)
        ax4.set_title('Cd derivation evolution')
        ax4.grid(linestyle='-.', linewidth=0.5)
        ax4.legend()
        
        figure.canvas.draw()
        
        figure.canvas.flush_events()
    plt.ioff()
start_cl_dcl_watch('/home/irisson/Documentos/NISUS/Brenin/Foam/aviao2022_22', 3000)
