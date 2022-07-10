import os
import sys
import shutil
import time as t
import manimupation
import start_simulation

params  = list(filter(lambda val: not '-' in val, sys.argv[1:]))
flags   = list(filter(lambda val: '-' in val, sys.argv[1:]))

alphas  = params[1:] if params[1].isnumeric() else params[2:]
alphas  = [float(alpha) for alpha in alphas]

destiny = 'CASES' if params[1].isnumeric() else params[1]

aPath   = os.getcwd()

for alpha in alphas:
    alpha_run   = True
    alphaPath   = start_simulation.create_tree(params[0], alpha, destiny)
    endtime     = manimupation.endTime(f'{destiny}/{alphaPath}')
    os.chdir(f'{destiny}/{alphaPath}')
    os.system('pwd')
    os.system(f'mpirun -np {4} simpleFoam -parallel >> log.txt &  ')
    os.chdir(aPath)

    upWind2gauss = list( filter(lambda val: '-upWind2gauss' in val, flags) )
    if len( upWind2gauss ):
        upWind2gauss = int( (upWind2gauss[0].split('-'))[-1] )
    else:
        upWind2gauss = 0
        
    
    while(alpha_run):
        time         = manimupation.timeNow(f'{destiny}/{alphaPath}')
        
        if upWind2gauss:
            start_simulation.upwind2gauss_linear(f'{destiny}/{alphaPath}', upWind2gauss)

        if time >= endtime:
            alpha_run = False
            
        t.sleep(1)
