def cadastrarProduto(x): #definimos a função que cadastra os produtos
    produto = {}         #com dicionários e parâmetro codigo
    print('Função *Cadastrar Produto* selecionada!\n')
    print('Código do produto: {}' .format(x))
    produto['codigo'] = x
    produto['nome'] = input('Digite o NOME do produto: ')
    produto['fabricante'] = input('Digite o FABRICANTE do produto: ')
    produto['valor'] = input('Digite o VALOR (R$) do produto: ')
    produtos.append(produto.copy())

def consultarProduto():  #definimos a função que consulta produtos
    while True:          #em loop e sem parametro
        print('Função *Consultar Produto* selecionada!')
        print('|--------------------------------------|')
        print('| Código |             Ação            |')
        print('|--------------------------------------|')
        print('|   1    | Consultar Todos os Produtos |')
        print('|   2    | Consultar por Código        |')
        print('|   3    | Consultar por Fabricante    |')
        print('|   4    | Retornar                    |')
        print('|--------------------------------------|')
        r = input('Qual a opção desejada?\n')
        if r == '1':
            for produto in produtos:
                for key, value in produto.items():
                    print('{}: {}' .format(key, value))
        elif r == '2':
            cod = int(input('Digite o código do produto que procura: '))
            for produto in produtos:
                for key, value in produto.items():
                    if produto.get('codigo') == cod:
                        print('{}: {}' .format(key, value))
        elif r == '3':
            fab = input('Digite o nome do fabricante que procura: ')
            for produto in produtos:
                for key, value in produto.items():
                    if produto.get('fabricante') == fab:
                        print('{}: {}' .format(key, value))
        elif r == '4':
            break
        else:
            print('Opção inválida, digite somente os valores: 1, 2, 3 e 4.\n')

def removerProduto(): #definimos a função que remove produtos
    print('Função *Remover Produto* selecionada!')
    rem = int(input('Digite o código do produto que deseja remover: '))
    for produto in produtos:
        if produto.get('codigo') == rem:
            del produtos[rem-1]

produtos = []  #no main, criamos a lista que armazena os dicionários
codigo = 0     #e iniciamos o contador código
while True:
    print('Bem vindo ao controle de estoque da mercearia João Victor Guidi de Lima')
    print('|-------------------------------|')
    print('| Código |         Ação         |')
    print('|-------------------------------|')
    print('|   1    | Cadastrar Produto(s) |')
    print('|   2    | Consultar Produto(s) |')
    print('|   3    | Remover Produto(s)   |')
    print('|   4    | Sair                 |')
    print('|-------------------------------|')
    op = input('Qual a opção desejada?\n')  #dependendo do input, chamamos funções
    if op == '1':
        codigo += 1
        cadastrarProduto(codigo)
    elif op == '2':
        consultarProduto()
    elif op == '3':
        removerProduto()
    elif op == '4':
        break
    else:
        print('Opção inválida, digite somente os valores: 1, 2, 3 e 4.\n')
