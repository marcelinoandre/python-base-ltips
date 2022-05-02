#! /usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Andre Marcelino"
__license__ = "Unlicense"

import os

current_language = os.getenv('LANG', 'en_LANG')[:5]

message = 'Hello, World!'

# Aqui aplicamos uma condicional

if current_language == 'pt_BR':
    message = 'Olá, mundo!'
elif current_language == 'it_IT':
    message = 'Ciao, Mondo!'    
elif current_language == 'fr_FR':
    message = 'Bonjour, Monde!'

print (message)        
    
