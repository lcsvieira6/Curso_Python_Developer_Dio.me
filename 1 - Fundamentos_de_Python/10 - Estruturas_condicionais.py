'''
A estrutura condicional permite o desvio de fluxo de controle,
quando determinadas expresões lógicas são atendidas.
'''


# 1° Exemplo: Utilizando apenas o IF

"""
idade = int(input("Informe a sua idade: "))


if idade >= 18:
    print("Você é maior de idade!")

if idade < 18:
    print("Você é menor de idade!")

"""


# 2° Exemplo: Utilizando if / else
"""
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))


if saldo >= saque:
    saldo -= saque
    print('Saque realizado com sucesso.')
    print(f'Seu saldo disponível é de R${saldo}.')

else:
    print('Não é possível continuar a transação.\nLimite indisponível!')

"""


# 3° Exemplo: Utilizando if / elif / else

"""
saldo = 2000.00

menu =int(input('''
########## MENU ########## 
1 - Sacar
2 - Depositar
3 - Saldo
4 - Cancelar

Digite uma opção:
'''))

if menu == 1:
    valor = float(input('Informe o valor do saque: ' ))
    saldo -= valor
    print(f'Saque realizado no valor de R${valor}')

elif menu == 2:
    valor = float(input('Informe o valor do deposito: '))
    saldo -= valor
    print(f"O valor de {valor} foi depositado com sucesso!")

elif menu == 3:
    print(f'O saldo disponível é de R${saldo}')

elif menu == 4:
    print('Obrigado pela preferência\nVolte sempre !!')

else:
    print('Opção inválida, tente novamente.') 
"""


# 4° Exemplo: Utilizando if aninhado (If dentro de if)

"""
saldo = 2000.00

menu =int(input('''
########## MENU ########## 
1 - Sacar
2 - Depositar
3 - Saldo
4 - Cancelar

Digite uma opção:
'''))

if menu == 1:
    valor = float(input('Informe o valor do saque: ' ))    
    if saldo >= valor:
        saldo -= valor
        print(f'Saque realizado no valor de R${valor}')
    
    else:
        print("Saldo indisponível!")

elif menu == 2:
    valor = float(input('Informe o valor do deposito: '))
    saldo -= valor
    print(f"O valor de {valor} foi depositado com sucesso!")

elif menu == 3:
    print(f'O saldo disponível é de R${saldo}')

elif menu == 4:
    print('Obrigado pela preferência\nVolte sempre !!')

else:
    print('Opção inválida, tente novamente.')

"""


# 5° Exemplo: Utilizando if ternário

"""
saldo = 2000.00
saque = float(input("Informe o valor do saque: "))

status = "Sucesso" if saldo >= saque else "Falha"
print(f'{status} ao realizar o saque!')
"""
