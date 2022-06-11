
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
