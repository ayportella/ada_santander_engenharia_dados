# > MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# append (sempre no final)

print('Antes do append:', lista)

lista.append(3)

print('Depois do append:', lista)

# insert (indica onde vai ser inserido)

lista.insert(2, 10)

print('Depois do insert:', lista)

# extend

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Depois do extend:', lista)

# pop

lista.pop()

print('Lista após o pop:', lista)

lista.pop(0)

print('Lista após o pop:', lista)


# remove

lista.remove(3)

print('Depois do remove', lista)

# obs: removeu apenas o primeiro 3

# count

print('Quantidade de 2 na lista:', lista.count(2))

# index

print('Índice do elemento 12:', lista.index(12))

# sort

lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)

# FUNÇÕES PARA LISTAS

# len

print(len(lista))

# sum

print(sum(lista))

# max

print('Maior elemento da lista:', max(lista))

# min

print('Menor elemento da lista:', min(lista))
