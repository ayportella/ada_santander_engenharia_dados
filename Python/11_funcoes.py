# > Funções

# 1. O que são funções e por que utilizá-las?

"""
print()
input()
len()
max()"""

# 2. Criação de funções

# Função inicial

def saudacao():
    print('Seja bem-vinda(o)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()
saudacao()
saudacao()

# Função com parâmetros

def saudacao(nome, curso):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Andressa', 'Python')
saudacao('Aline', 'Javascript')

# Função com parâmetros default

def saudacao(nome, curso='Python'):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Andressa')

def saudacao(nome, curso='Python'):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Andressa', 'C++')

# Funções com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5,7)

print('O resultado da soma é', resultado)


