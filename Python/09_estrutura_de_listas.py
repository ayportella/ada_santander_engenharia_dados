# > LISTAS

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 9.7, 8.2]

# Criando listas
lista = []
lista = list()
lista = [26, 'Walisson', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e slices (fatiamento)

lista = [10, 'Walisson', 3.14159, False]

print(lista[0])
print(lista[1])

print(lista[-1])

# slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])

# > Iterações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices

print('Comprimento da lista:', len(lista))

for i in range(len(lista)):
    print(i)
