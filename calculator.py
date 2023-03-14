#calculadora simples
while True:
    try:
        a = float(input("Digite o valor do primeiro número:\n"))
    except:
        print("Valor inválido: digite apenas valores numéricos inteiros ou decimais com .")
        continue
    op = input("Digite a operação que deseja realizar:\n")
    if op not in '+-*x/%':
        print('Operação inválida, digite apenas os operadores +, -, *, /, ou ainda x e % para multiplicação e divisão.\n')
        continue
    try:
        b = float(input("Digite o valor do segundo número:\n"))
    except:
        print("Valor inválido: digite apenas valores numéricos inteiros ou decimais com .")
        continue
    if op == '+':
        print("A soma de {} com {} é {}." .format(a,b,a+b))
    elif op == '-':
        print("A subtração de {} com {} é {}." .format(a,b,a-b))
    elif op == '*' or op == 'x':
        print("A multiplicação de {} por {} é {}." .format(a,b,a*b))
    else:
        print("A divisão de {} por {} é {}." .format(a,b,a/b))
