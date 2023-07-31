#Variaveis
#Valores armazenados que podem ser modificados.

age = 28
name = 'Lucas'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

age, name = (28, 'Lucas Vieira')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

"""
Constantes.
Valores que uma vez armazenados não podem ser modificados.

Em Python não temos constantes. Podemos utilizar a convenção para dizer ao
programador que a variável é uma constate. Para isso se faz necessário criar
a variável com letras MAÍUSCULAS.
"""

ABS_PATH = '/home/guilherme/Documents/python_course/'
DEBUG = True
STATES = [
    'SP'
    'RJ'
    'MG'
]
AMOUNT = 30.2
