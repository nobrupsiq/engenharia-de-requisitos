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
  print('2. Concluir tarefa')
  print('3. Listar tarefas')
  print('0. Sair\n')
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
  
    # Esta variavel tem o -1 pq o indice da lista começa em 0 e não em 1
    indice = concluir_tarefa -1
    if concluir_tarefa >= 1 and concluir_tarefa <= total_de_tarefas:
      tarefas[indice]['concluida'] = 1 
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