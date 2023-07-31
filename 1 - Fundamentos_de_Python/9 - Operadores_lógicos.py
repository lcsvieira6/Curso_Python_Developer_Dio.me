"""
São operadores utilizados em conjunto com os operadores de comparação,
para montar uma expressão lógica.
"""

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite) # >>> False

print(saldo >= saque or saque <= limite) # >>> True

# Operador de negação

contatos_emergebcia = []

not 100 > 1500 # >>> True

not contatos_emergebcia # >>> True

not "saque 1500;" # >>> False

not "" # False