print('O palíndromo é quando uma palavra ao contrário é ela mesma')
palavra = str(input('Digite uma palavra e iremos verificar se é palíndromo: '))
teste = ' ' + palavra
novo = ''
for i in range(len(teste) - 1, 0, -1):
  novo = novo + teste[i]
  print('>', teste[i])
if novo == palavra:
  print(f'Sim, o palíndromo de {palavra} é {novo}')
else:
  print(f'Vish,{palavra} não é palíndromo... Olha só, fica: {novo}')
