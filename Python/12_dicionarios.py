# > Dicionários

# Criando dicionários

dicionario = {}
dicionario = dict()
dicionario = {'nome': 'Andressa', 'idade': 33, 'altura': 1.55}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionário

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 2
print(dicionario) # ou seja, sobrescreveu o que já havia

# Iterando sore um dicionário

for chave  in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)

print('altura' in dicionario)
