# /usr/bim/env python3
"""Imprime a tabuada do 1 ao 10.
---Tabuada do 1---
    1 X 1 = 1     
    1 X 2 = 2     
    1 X 3 = 3  
##################    
...
---Tabuada do 2---
    2 X 1 = 2     
    2 X 2 = 4     
    2 X 3 = 6  
...
##################
"""
__version__ = '0.1.1'
__autor__ = 'Andre Marcelino'

numeros = list(range(1, 11))

for n1 in numeros:
    print('{:-^18}'.format(f'Tabuada do {n1}') )
    for n2 in numeros:
        resultado = n1 * n2
        print('{:^18}'.format(f"{n1} X {n2} = {resultado}"))

    print('#' * 18)
