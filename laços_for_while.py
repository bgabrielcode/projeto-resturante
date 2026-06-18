# #Compreendendo laços

# clientes = ['João', 'Maria', 'Carlos', 'Ana', 'Beatriz']

# for cliente in clientes:
#     print(cliente)


# O que é um loop infinito?

# contador = 0 

# while contador < 10:
#     print('Processando dados')
#     contador += 1 # Atualiza o contador para evitar o loop infinito


# Quantas vezes a mensagem será exibida?

# for i in range(5): #  Esta linha inicia um "laço de repetição" (ou loop).
#     print('Bem-vindo ao Buscante!')

# """
# A função range(5) gera uma sequência de números que vai de 0 até 4 
# (ou seja, 0, 1, 2, 3, 4). O for vai executar o que está dentro dele 
# para cada um desses números.

# Alguns exemplos de como utilizar o i in range

# """


# for i in range(1, 6):
#     print(f'Contagem {i}')

# # Aqui, range(1, 6) gera os números 1, 2, 3, 4, 5.


# """
# Exemplo 3: Contando com um "passo" (pulando números)

# Você também pode definir um passo para o range. range(início, fim, passo):

# """

# for i in range(0, 10, 2): # # Começa em 0, vai até 9, pulando de 2 em 2
#     print(f'Numero par {i}')

# Neste exemplo, range(0, 10, 2) gera 0, 2, 4, 6, 8.


# """
# Exemplo 4: Contagem regressiva

# Você pode usar um passo negativo para contar para trás:

# """

# for i in range(5, 0, -1):
#     print(f'Contagem regressiva: {i}')
# print('Lançar!')

# Aqui, range(5, 0, -1) gera 5, 4, 3, 2, 1.




# Calculando a soma de números

# numeros = [10, 20, 30, 40, 50]

# soma = 0

# for numero in numeros:
#     soma += numero
    
# print(f'A soma total das receitas é: {soma}')


# """
# Exemplo 1: Percorrendo uma lista de frutas

# Imagine que você tem uma lista de frutas e quer imprimir cada uma delas:


# """


# frutas = ["maçã", "banana", "laranja", "uva"]

# for fruta in frutas:
#     print(f"Eu gosto de {fruta}.")


# """
# Saída esperada:

# Eu gosto de maçã.
# Eu gosto de banana.
# Eu gosto de laranja.
# Eu gosto de uva.

# """

# notas = [7.5, 8.0, 6.5, 9.0]

# soma_notas = 0
# quantidade_notas = 0

# for nota in notas:
#     soma_notas += nota
#     quantidade_notas += 1

# media = soma_notas / quantidade_notas
# print(f'A média das notas é: {media:.2f}')


# """
# Saída esperada:

# A média das notas é: 7.75

# """



# """
# Exemplo 3: Percorrendo uma string (que também é uma sequência de caracteres)

# Você pode até percorrer cada letra de uma palavra:

# """

# palavra = 'Python'

# for letra in palavra:
#     print(letra)


# """
# Saída esperada:

# P
# y
# t
# h
# o
# n


# """

# projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

# for projeto in projetos:
#     if projeto is None:
#         print('Projeto ausente')
#     else:
#         print(projeto)


# """
# Exemplo 1: Verificando se uma variável é None

# Este é o caso do nosso exercício. Queremos saber se um projeto está ausente, ou seja, se ele é None.

# """

# projeto_atual = None

# if projeto_atual is None:
#     print('Nenhum projeto selicionado')
# else:
#     print(f'Projeto: {projeto_atual}')

# """
# Exemplo 2: Comparando a identidade de objetos

# Aqui, is verifica se lista1 e lista2 são o mesmo objeto na memória.

# """

# lista1 = [1, 2, 3]
# lista2 = [1, 2, 3]
# lista3 = lista1

# print(lista1 is lista2) # Saída: False (são objetos diferentes, mesmo com o mesmo conteúdo)
# print(lista1 is lista3) # Saída: True (lista3 aponta para o mesmo objeto que lista1)


# Entendendo o uso do break

# livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

# for livro in livros:
#     if livro == "O Hobbit":
#         print(f'Livro encontrado: {livro}')
#         break


# Controle de estoque

# for i in range(5, 0, -1):
#     print(f'Venda realizada! Estoque restante: {i}')

# print('Estoque esgotado')
        

# estoque = 5

# while estoque > 0:
#     estoque -= 1
#     print(f'Venda realizada! Estoque restante: {estoque}')

# print('Estoque esgotado!')


# Contagem Regressiva

# for segundos in range(10, 0, -1):
#     if segundos % 2 == 0:
#         print(f'Faltam apenas {segundos} segundos - Não perca essa oportunidade!')
#     else:
#         print(f'A contagem continua {segundos} segundos restantes')

# print('Aproveite a promoção agora!')

# livros = [

#     {"nome": "1984", "estoque": 5},

#     {"nome": "Dom Casmurro", "estoque": 0},

#     {"nome": "O Pequeno Príncipe", "estoque": 3},

#     {"nome": "O Hobbit", "estoque": 0},

#     {"nome": "Orgulho e Preconceito", "estoque": 2}

# ]

# for livro in livros:
#     if livro['estoque'] == 0:
#         continue
# print(f'Livro disponível: {livro['nome']}')


# Validação de entrada para login

# while True:
#     nome_usuario = input('Digite seu nome de usuário: ')
#     senha = input('Digite sua senha: ')

#     if len(nome_usuario) < 5:
#         print('O nome de usuário deve ter pelo menos 5 caracteres.')
#         continue

#     if len(senha) < 8:
#         print('A senha deve ter pelo menos 8 caracteres.')
#         continue

#     print('Cadastro realizado com sucesso!')
#     break
   

