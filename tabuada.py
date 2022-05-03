# /usr/bim/env python3
"""Imprime a tabuada do 1 ao 10.
Tabuada do número: 1
1  x 1 = 1
1  x 2 = 2
1  x 3 = 3
...
____________________
Tabuada do número: 2
2  x 1 = 2
2  x 2 = 4
2  x 3 = 6
...
____________________
"""
__version__ = '0.1.0'
__autor__ = 'Andre Marcelino'

numeros = list(range(1, 11))

for numero in numeros:
    print('Tabuada do número:', numero)
    for outro_numero in numeros:
        print(f'{numero}  x {outro_numero} = {numero * outro_numero}')

    print('____________________')
