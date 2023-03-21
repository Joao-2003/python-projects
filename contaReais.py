#Contador de dinheiro 
din = float(input('Digite o número de reais sobre o qual deseja saber a quantidade de notas e moedas correspondentes: ($$.$$)\n'))
while True:
  if (din >= 200):
    cont_200 = din // 200
    din = din - cont_200 * 200
    print('Cédulas de 200 reais: {}' .format(cont_200))
    if (not din):
      break  
  if (din >= 100):
    cont_100 = din // 100
    din = din - cont_100 * 100
    print('Cédulas de 100 reais: {}' .format(cont_100))
    if (not din):
      break
  if (din >= 50):
    cont_50 = din // 50
    din = din - cont_50 * 50
    print('Cédulas de 50 reais: {}' .format(cont_50))
    if (not din):
      break
  if (din >= 20):
    cont_20 = din // 20
    din = din - cont_20 * 20
    print('Cédulas de 20 reais: {}' .format(cont_20))
    if (not din):
      break
  if (din >= 10):
    cont_10 = din // 10
    din = din - cont_10 * 10
    print('Cédulas de 10 reais: {}' .format(cont_10))
    if (not din):
      break      
  if (din >= 5):
    cont_5 = din // 5
    din = din - cont_5 * 5
    print('Cédulas de 5 reais: {}' .format(cont_5))
    if (not din):
      break
  if (din >= 2):
    cont_2 = din // 2
    din = din - cont_2 * 2
    print('Cédulas de 2 reais: {}' .format(cont_2))
    if (not din):
      break
  if (din >= 1):
    cont_1 = din // 1
    din = din - cont_1 * 1
    print('Moedas de 1 real: {}' .format(cont_1))
    if (not din):
      break
  if (din >= 0.5):
    cont_50c = (din*100) // 50
    din = din - cont_50c * 0.5
    print('Moedas de 50 centavos: {}' .format(cont_50c))
    if (not din):
      break
  if (din >= 0.25):
    cont_25c = (din*100) // 25
    din = din - cont_25c * 0.25
    print('Moedas de 25 centavos: {}' .format(cont_25c))
    if (not din):
      break
  if (din >= 0.10):
    cont_10c = (din*100) // 10
    din = din - cont_10c * 0.1
    print('Moedas de 10 centavos: {}' .format(cont_10c))
    if (not din):
      break
  if (din >= 0.05):
    cont_5c = (din*100) // 5
    din = din - cont_5c * 0.05
    print('Moedas de 5 centavos: {}' .format(cont_5c))
    if (not din):
      break
  if (din >= 0.01):
    cont_1c = (din*100) // 1
    print('Moedas de 1 centavos: {}' .format(cont_1c))
    break
