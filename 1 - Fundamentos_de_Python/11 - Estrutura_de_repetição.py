"""
São estruturas utilizadas para repetir um trecho de código
um determinado número de vezes. Esse número pode ser conhecido
previamente ou determinado através de uma expressão lógica.
"""

# Exemplo 1: Utilizando o comando "FOR".


texto = input("Informe um texto: ")

VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")


# Exemplo 2: Utilizando o comando "FOR / ELSE"


texto = input("Informe um texto: ")

VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
    
    else:
        print() # adiciona uma quebra de linha


# Exemplo 3: Utilizando o comando "range"

# range(stop) -> range object
# range(start, stop[, setp]) -> range object
# list(range(4)) >>> [0, 1, 2, 3, 4]


for numero in range(0, 11):
    print(numero, end=" ")


# Exibindo a tabuada do 5


for numero in range(0, 51, 5):
    print(numero, end=" ")



#  Exemplo 5: Utilizando o comando "While"


# O comando while é utilizado para repetir um bloco de código
# várias vezes. Faz sentido usar while quando não sabemos o número
# exato de vezes que nosso bloco de código deve ser executado    



opcao = 1

while opcao != 3:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[3] Sair \n>> "))

    if opcao == 1:
        print("Sacando...")

    elif opcao == 2:
        print("Exibindo o extrato...")
    
    elif opcao == 3:
        print("Volte sempre !!")

    else:
        print("Opção invalida. \nTente novamente!!")


# Exemplo 6: Utilizando o comando "break"


while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)



# Exemplo 7: Utilizando o comando "continue"

# for numero in range(100):

if numero % 2 == 0:
    continue

    print(numero, end=" ")