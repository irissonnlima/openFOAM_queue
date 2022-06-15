import os
import sys
import shutil
import manimupation

params  = sys.argv[1:]

assert len(params) >= 2, 'ERROR: Quantidade de Parâmetros insuficiente'
assert os.path.isdir(params[0]), 'ERROR: Diretório não encontrado'

aPath       = os.getcwd()
file_tree   = params[0]
destiny     = 'CASES' if (params[1]).isnumeric() else params[1]
cases       = 1 if (params[1]).isnumeric() else 2
alphas      = [float(param) for param in params[cases:]]

n_process   = manimupation.number_of_process(file_tree)

for alpha in alphas:
    alp     = str(alpha).replace('.', '_')
    subPath = f'{destiny}/{file_tree}_{alp}'
    
    shutil.copytree(file_tree, subPath)
    
    manimupation.alphaCalc_change(subPath, alpha)
    
    os.chdir(subPath)
    result = os.system('decomposePar')
    if result:
        print('ERRO: Nao foi possivel decompor o dominio')
        break
    result = os.system(f'mpirun -np {n_process} simpleFoam -parallel >> log.txt &')
    print('===========================================================================================')
    print(result)
    print('===========================================================================================')
    if result:
        print(f'ERRO: Erro ao rodar o caso {alpha}')
        break
    os.chdir(aPath)
    
