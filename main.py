import os
import sys
import shutil
import manimupation

params  = sys.argv[1:]

assert len(params) >= 2, 'ERROR: Quantidade de Parâmetros insuficiente'
assert os.path.isdir(params[0]), 'ERROR: Diretório não encontrado'

aPath   = os.getcwd()
destiny = 'CASES' if (params[1]).isnumeric() else params[1]
cases   = 1 if (params[1]).isnumeric() else 2
alphas  = [float(param) for param in params[cases:]]


