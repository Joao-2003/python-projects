import math

b_ou_m = input("Deseja descobrir a quantidade de bits ou o modulo? Digite 1 para bits ou 2 para o modulo\n")
if b_ou_m == "1":
    modulo = int(input("Digite o módulo.\n"))
    bits = math.log(modulo,2)
    if bits is int:
        print("A quantidade de bits eh {}." .format(bits))
    else: 
        print("Deseja continuar? O número digitado não é potencia de 2.")
        bits = math.ceil(bits)
        print("A quantidade de bits eh {}." .format(bits))
elif b_ou_m == "2":
    expoente = int(input("Digite a quantidade de bits\n2"))
    potencia = 2**expoente
    print("A potencia eh {}." .format(potencia))
else:
    print("Opção inválida.")
