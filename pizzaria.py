p = 0
while True:                                                     #inicia o loop, que itera ate que o cliente encerre com break
    print('                   PIZZARIA JOÃO VICTOR GUIDI DE LIMA                    ')
    print('_________________________________________________________________________')
    print('|Código | Descrição | Pizza Média - M | Pizza Grande – G(30 % mais cara)|')
    print('-------------------------------------------------------------------------')
    print('|21     |Napolitana |R$ 20, 00        |R$ 26, 00                        |')
    print('|22     |Margherita |R$ 20, 00        |R$ 26, 00                        |')
    print('|23     |Calabresa  |R$ 25, 00        |R$ 32, 50                        |')
    print('|24     |Toscana    |R$ 30, 00        |R$ 39, 00                        |')
    print('|25     |Portuguesa |R$ 30, 00        |R$ 39, 00                        |')
    print('-------------------------------------------------------------------------')
    t = input('Qual o tamanho de pizza que deseja? [M/G]\n')
    if (t != 'm' and t != 'M' and t != 'g' and t != 'G'):   #valida o valor do tamanho
        print('Opção inválida.\n')
        continue
    c = int(input('Qual o código da pizza que deseja?\n'))  #valida o tamanho do codigo
    if (c < 21 or c > 25):                                  #altera o gasto do cliente com base no pedido
        print('Opção inválida.\n')
        continue
    if ((t == 'm' or t == 'M') and c == 21):
        p += 20
    elif ((t == 'g' or t == 'G') and c == 21):
        p += 26
    elif ((t == 'm' or t == 'M') and c == 22):
        p += 20
    elif ((t == 'g' or t == 'G') and c == 22):
        p += 26
    elif ((t == 'm' or t == 'M') and c == 23):
        p += 25
    elif ((t == 'g' or t == 'G') and c == 23):
        p += 32.50
    elif ((t == 'm' or t == 'M') and c == 24):
        p += 30
    elif ((t == 'g' or t == 'G') and c == 24):
        p += 39
    elif ((t == 'm' or t == 'M') and c == 25):
        p += 30
    else:
        p += 39
    r = input('Deseja continuar ou encerrar o pedido? Digite qualquer coisa para continuar e o número 0 para encerrar.')
    if (r == '0'):                                     #encerra o loop com o 0
        break
print('O total a ser pago é: R${:.2f}' .format(p))     #exibe o gasto ao fim do pedido
