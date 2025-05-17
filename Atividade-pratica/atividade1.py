# Aqui define o tamanho maximo de caracteres da minha tarefa e do tamanho do nome da tarefa
#define MAX_TAREFAS 100
#define TAM_NOME 100
max_tarefas = 100
tamanho_da_descricao = 100

# Crio minha variaveis
descricao = ''
total_de_tarefas = 0
tarefas = [] # Lista com dicionarios pois temos uma descrição e um verificador de concluida

def adicionar_tarefa(tarefa):
  item = {
    'descricao': tarefa,
    'concluida': 0
  }
  tarefas.append(item)


def listar_tarefas(lista):
  print('\n--- Lista de tarefas ---')
  if len(lista) > 0:
    for index, tarefa in enumerate(lista):
      print(f'{index + 1}. [{"X" if tarefa['concluida'] != 0 else ' '}] {tarefa['descricao']}')
  else:
    print('-------------------------\n')

while True:
  print('\n1. Adicionar tarefa')
  print('\n2. Concluir tarefa')
  print('\n3. Listar tarefas')
  print('\n0. Sair\n')
  opcao = input('Escolha uma opção: ')

  if opcao == '1':
    if total_de_tarefas < max_tarefas:
      descricao_tarefa = input('Digite a descricao da tarefa: ')
      descricao = descricao_tarefa[:tamanho_da_descricao]
      adicionar_tarefa(descricao)
      total_de_tarefas += 1
    else:
      print('Limite total de tarefas atingido!')

  elif opcao == '2':
    listar_tarefas(tarefas)
    concluir_tarefa = int(input('Digite o numero da tarefa a concluir: '))
  
    if concluir_tarefa >= 1 and concluir_tarefa <= total_de_tarefas:
      tarefas['concluida'] = 1 # PAREI AQUI, ESTA DANDO ERRO NESTA LINHA
      print('Tarefa marcada como concluída!\n')
    else:
      print('Numero inválido!')
  elif opcao == '3':
    listar_tarefas(tarefas)
  elif opcao == '0':
    print('Saindo... \n')
    break
  else:
    print('Opcao invalida!\n')