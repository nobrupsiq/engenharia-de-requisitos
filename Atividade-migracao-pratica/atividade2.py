class Atividade:
  def __init__(self, descricao):
    self.descricao = descricao
    self.concluida = False

  def marcar_como_concluida(self):
    self.concluida = True;

  def status(self):
    return '[X]' if self.concluida else '[ ]'

def sistema_de_atividades():
  lista = []
  while True:
    print('\n=== SISTEMA DE GESTÃO DE ATIVIDADES ===\n')
    print('1 - Adicionar atividade')
    print('2 - Listar atividades')
    print('3 - Concluir atividade')
    print('0 - Sair\n')

    opcao = input('Escolha uma opçao: ')

    if opcao == '1':
      descricao = input('Digite a descrição da atividade: ')
      nova_atividade = Atividade(descricao)
      lista.append(nova_atividade)
      print('Atividade adicionada!')

    elif opcao == '2':
      print('\n--- Lista de atividades ---')
      for index, atividade in enumerate(lista):
        print(f'{index + 1}. {atividade.status()} {atividade.descricao}')

    elif opcao == '3':
      print('\n--- Lista de atividades ---')
      for index, atividade in enumerate(lista):
        print(f'{index + 1}. {atividade.status()} {atividade.descricao}')
      escolher_atividade = int(input('\nDigite o número da atividade a concluir: '))
      if escolher_atividade >= 1 and escolher_atividade <= len(lista):
        lista[escolher_atividade - 1].marcar_como_concluida()
        print('Atividade concluida!')
      else:
        print('Número inválido.')

    elif opcao == '0':
      print('Encerrando sistema...')
      break
    else:
      print('Opção inválida!')

sistema_de_atividades()