
"""for variavel in range(5):
    print(variavel)"""

# de um até 9 pulando 3:

"""for variavel in range(1, 11, 3):
    print(variavel)"""


# média de 3 notas

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}: '))

    soma = soma + nota
print(soma/3)

