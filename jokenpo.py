import random
resultados = []
resultado = []
while True:
  print('Jokenpo')
  print('r - Rock')
  print('p - Paper ')
  print('s - Scissors')
  print('o - Encerrar Jogo')
  p1 = input('Digite sua jogada: ')
  p1 = p1.lower()
  if p1 == 'o':
    print('Jogo encerrado.')
    break
  if p1 not in 'rps':
    print('Jogada inválida.')
    continue
  jokenpo = ['r', 'p', 's']
  p2 = random.choice(jokenpo)
  jogadas = [p1, p2]
  resultado.append(jogadas)
  if p1 == 'r' and p2 == 'r':
    decision = 'Empate'
  elif p1 == 'r' and p2 == 'p':
    decision = 'Máquina vence'
  elif p1 == 'r' and p2 == 's':
    decision = 'Humano vence'
  elif p1 == 'p' and p2 == 'r':
    decision = 'Humano vence'  
  elif p1 == 'p' and p2 == 'p':
    decision = 'Empate' 
  elif p1 == 'p' and p2 == 's':
    decision = 'Máquina vence' 
  elif p1 == 's' and p2 == 'r':
    decision = 'Máquina vence' 
  elif p1 == 's' and p2 == 'p':
    decision = 'Humano vence'     
  elif p1 == 's' and p2 == 's':
    decision = 'Empate'
  print(decision)
  resultado.append(decision)
  resultados.append(resultado)
  resultado = []
print(resultados)

   
