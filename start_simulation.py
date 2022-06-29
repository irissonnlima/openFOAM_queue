import manimupation as m
import numpy as np

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
