'''
Operadores utilizados para definir um valor inicial ou sobrescrever
o valor de uma variável
'''

saldo = 500
print(saldo) 

saldo += 200
print(saldo) # >> 700

saldo = 500
saldo -= 200
print(saldo) # >> 300

saldo = 500
saldo *= 200
print(saldo) # >> 100000

saldo = 500
saldo **= 200
print(saldo) # >> 100000


saldo = 500
saldo /= 200
print(saldo) # >> 2.5

saldo = 500
saldo //= 200

print(saldo) # >> 2

saldo = 500
saldo %= 200

print(saldo) # >> 100000
