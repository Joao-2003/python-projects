def volumeFeijoada():       #definição da função que recebe o valume e calcula seu valor, depois retorna ao main
    while True:
        print('_____________________________________')
        print('| Volume (ml)       | Valor (R$)    |')
        print('_____________________________________')
        print('| volume < 300      | Não é aceito  |')
        print('| 300<=volume<=5000 | volume * 0.08 |')
        print('| volume > 5000     | Não é aceito  |')
        print('_____________________________________')
        try:
            vol = int(input('Qual é o volume desejado da porção de feijoada? (em ml)\n'))
            if (300 <= vol <= 5000):
                break                                         #usamos try e except para apurar os valores
            else:
                print('Valor não aceito, digite um volume entre 300 e 5000.\n')
                continue
        except ValueError:
            print('Valor não aceito, digite um volume entre 300 e 5000.\n')
    return vol * 0.08

def opcaoFeijoada():        #definição da função que recebe a opção e multiplica devidamente ao volume
    while True:             #depois retorna ao main
        print('__________________________________________________________________________')
        print('|              Opção                                       |Multiplicador|')
        print('|___________________________________________________________|____________|')
        print('| b - Básica (Feijão + Paiol + Costelinha)                    |   1.00   |')
        print('| p - Premium (Feijão + Paiol + Costelinha + Partes de Porco) |   1.25   |')
        print('| s - Suprema (Feijão + Paiol + Costelinha + Partes de Porco  |   1.50   |')
        print('| Charque + Calabresa + Bacon)                                |          |')
        print('|________________________________________________________________________|')
        op = input('Qual é a opção desejada?\n')
        if ((op != 'b' and op != 'B') and (op != 'p' and op != 'P') and (op != 's' and op != 'S')):
            print('Valor não aceito. Digite: "b" (para "Básica"), "p" (para "Premium") e "s" (para "Suprema").\n')
            continue
        if (op == 'b' or op == 'B'):
            m = 1.00
            break
        elif (op == 'p' or op == 'P'):
            m = 1.25
            break
        else:
            m = 1.50
            break
    return m

def acompanhamentoFeijoada():
    a = 0                 #definição da função que recebe nenhum ou vários acompanhamentos e
    while True:           #retorna o valor ao main
        print('__________________________________________________________________________')
        print('|               Acompanhamento                               |   Valor   |')
        print('|___________________________________________________________ |___________|')
        print('| 0 - Não desejo mais acompanhamentos  (encerrar pedido)     |    0,00   |')
        print('| 1 - 200g de arroz                                          |    5,00   |')
        print('| 2 - 150g de farofa especial                                |    6,00   |')
        print('| 3 - 100g de couve cozida                                   |    7,00   |')
        print('| 4 - 1 laranja descascada                                   |    3,00   |')
        print('|________________________________________________________________________|')
        ac = input('Digite o código do acompanhamento:\n')
        if (ac != '0' and ac != '1' and ac != '2' and ac != '3' and ac != '4'):
            print('Valor não aceito. Digite números entre 0 e 4 para encerrar o pedido ou solicitar acompanhamentos.\n')
            continue
        if (ac == '0'):
            a += 0.00
            break
        elif (ac == '1'):
            a += 5.00
        elif (ac == '2'):
            a += 6.00
        elif (ac == '3'):
            a += 7.00
        else:
            a += 3.00
    return a

print('Bem vindo ao restaurante João Victor Guidi de Lima.\n')
vf = volumeFeijoada()          #variáveis globais que recebem os retornos (variáveis locais) da funções
of = opcaoFeijoada()
af = acompanhamentoFeijoada()
vt = vf * of + af             #cálculo do valor total e impressão de todos os gastos
print('O valor a ser pago é {} (volume = R${}, opção = {} * R${}, acompanhamento = R${}.' .format(vt, vf, of, vf, af))
