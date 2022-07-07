import os
import sys
import shutil
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
    endtime     = manimupation.endTime(alphaPath)
    
    os.chdir(f'{aPath}/{alphaPath}')
    os.system(f'mpirun -np {4} simpleFoam -parallel >> log.txt &  ')
    os.chdir(aPath)
    
    while(alpha_run):
        time    = manimupation.timeNow(alphaPath)
        if '-gauss_linear2upWind' in flags:
            start_simulation.gauss_linear2upwind(alphaPath, 400)
        
        if time >= endtime:
            alpha_run = False
        
