import os
import numpy as np

def alphaCalc_change (file_path:str, value:float) -> None:
    new_file = ''
    with open(f'{file_path}/system/alphaCalc','r') as file:
        for line in file:
            line = line.strip()
            
            if 'aoa' in line[:5]:
                new_file += f'aoa {value}; \n'
            else:
                new_file += line + '\n'
    
    with open(f'{file_path}/system/alphaCalc', 'w') as file:
        file.write(new_file)

def number_of_process (file_path:str) -> int:
    
    with open(f'{file_path}/system/decomposeParDict', 'r') as file:
        for line in file:
            line = line.strip()
            if 'numberOfSubdomains' in line:
                line = line.strip(';')
                line = line.split(' ')
                return int(line[-1])
            
def fvSchemes (file_path:str, scheme_to_ignore:str, new_scheme) -> int:
    
    new_file    = ''
    ignore_line = 0
    added       = False
    
    with open(f'{file_path}/system/fvSchemes', 'r') as file:
        for line in file:
            line = line.strip()
            
            if scheme_to_ignore in line:
                ignore_line += 1
            elif ignore_line and '}' in line:
                ignore_line -= 1

            if not ignore_line and not added:
                new_file += line + '\n'
            elif not added:
                new_file += new_scheme + '\n'
                added     = True
            elif not ignore_line and added:
                added = False
    
    with open(f'{file_path}/system/fvSchemes', 'w') as file:
        file.write(new_file)
    
    return 0      
                
def timeNow (file_path:str) -> int:
    path        =  f'{file_path}/postProcessing/WallCoeffsCyl1/0/forceCoeffs.dat'
    #directories = list(filter(lambda x: os.path.isdir(x) and x != 'yPlus', os.listdir(path))) 
    
    try:
        data = np.loadtxt(path)
        return data[-1, 0]
    except:
        return -1

def endTime (file_path:str) -> int:
    path =  f'{file_path}/system/controlDict'
    
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if 'endTime' in line[:12]:
                line     = line.split(' ')
                line[-1] = line[-1].strip(';')
                return int(line[-1]) 