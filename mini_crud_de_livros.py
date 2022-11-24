controle = 'N'
livros = []


def listar():
  print('\n')
  for i in range(len(livros)):
    print(livros[i], '------- NUMERAÇÃO:', i)


while controle != 'S':
  print('\n')
  print('Biblioteca CELDS')
  print('\n')
  print('Para CADASTRAR, tecle ----- C')
  print('Para EDITAR, tecle ----- E')
  print('Para LISTAR, tecle ----- L')
  print('Para DELETAR, tecle ----- D')
  print('Para SAIR, tecle ----- S')

  entrada = input('Por favor, escolha oque fazer: ')
  controle = entrada
  if entrada == 'C':
    livro = input('Coloque o nome do livro: ')
    livros.append(livro)
  if entrada == 'E':
    for i in range(len(livros)):
      print('Numeração dos livros:', livros[i], '-----', i)
    indice = int(input('qual livro quer editar? '))

    livro = input('Digite um novo livro: ')
    livros[indice] = livro
    print('\n')
  if entrada == 'L':
    print('\n')
    listar()
    print('\n')
  if entrada == 'D':
    for i in range(len(livros)):
      print('Numeração dos livros:', livros[i], '-----', i)
    indice = int(input('qual livro quer deletar? '))

    livros.pop(indice)
    listar()
    print('\n')

print('Obrigada pela visita! Volte sempre <3')
