print('Bem vindo(a) a loja João Victor Guidi de Lima!\n')       #identificador pessoal
v = float(input('Digite o valor do produto:\n'))                #variavel do valor
q = int(input('Digite a quantidade do produto:\n'))             #variavel da quantidade
sd = v * q                                                      #calculo do valor sem desconto
if (q <= 4):                                                    #condicionais do desconto a depender da quantidade
    d = 0
elif (q >= 5 and q <= 19):
    d = 0.03
elif (q >= 20 and q <= 99):
    d = 0.06
else:
    d = 0.1
cd = sd * (1 - d)                                               #calculo do valor com desconto
print('O valor sem desconto foi: {:.2f}.'.format(sd))           #print dos valores sem e com desconto
print('O valor com desconto foi: {:.2f}. (desconto de {}%)'.format(cd, int(d*100)))
