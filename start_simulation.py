import os
import sys
import shutil
import numpy as np
import manimupation as m

def gauss_linear2upwind(file_path:str, time2change:int) -> int:
    
    gradSchemes  = 'gradSchemes\n'
    gradSchemes += '{\n'
    gradSchemes += 'grad(U) cellMDLimited Gauss linear 1.0; // 1.0\n'
    gradSchemes += 'grad(k) cellLimited Gauss linear 1;\n'
    gradSchemes += 'grad(omega) cellLimited Gauss linear 1;\n'
    gradSchemes += 'default         Gauss linear;\n'
    gradSchemes += '}'

    divSchemes  = 'divSchemes\n'
    divSchemes += '{\n'
    divSchemes += 'default         none;\n'
    divSchemes += '//div(phi,U)      bounded Gauss linearUpwind grad(U);\n'
    divSchemes += 'div(phi,U)      bounded Gauss upwind;\n'
    divSchemes += '//div(phi,k) bounded Gauss limitedLinear 1;\n'
    divSchemes += 'div(phi,k) bounded Gauss upwind;\n'
    divSchemes += '//div(phi,omega) bounded Gauss limitedLinear 1;\n'
    divSchemes += 'div(phi,omega) bounded Gauss upwind;\n'
    divSchemes += '\n'
    divSchemes += 'div((nuEff*dev2(T(grad(U))))) Gauss linear;\n'
    divSchemes += '}'
    

    t = m.timeNow(file_path)
    if t > time2change:
        m.fvSchemes(file_path, 'gradSchemes', gradSchemes)
        m.fvSchemes(file_path, 'divSchemes', divSchemes)

def create_tree (file_path:str, alpha:list, destiny:str = 'CASES') -> str:
    aPath     = os.getcwd()

    alp     = str(alpha).replace('.', '_')
    subPath = f'{destiny}/{file_path}_{alp}'
    
    shutil.copytree(file_path, subPath)
    
    m.alphaCalc_change(subPath, alpha)
    
    os.chdir(subPath)
    result = os.system('decomposePar')
    if result:
        print('ERRO: Nao foi possivel decompor o dominio')
    os.chdir(aPath)
    
    return f'{file_path}_{alp}'