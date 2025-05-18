#include <stdio.h>
#include <string.h>

#define MAX_TAREFAS 100
#define TAM_NOME 100

typedef struct {
    char descricao[TAM_NOME];
    int concluida; // 0 = não, 1 = sim
} Tarefa;

void listarTarefas(Tarefa lista[], int total) {
    printf("\n--- Lista de Tarefas ---\n");
    for (int i = 0; i < total; i++) {
        printf("%d. [%c] %s\n", i + 1, lista[i].concluida ? 'X' : ' ', lista[i].descricao);
    }
    printf("-------------------------\n");
}

int main() {
    Tarefa tarefas[MAX_TAREFAS];
    int total = 0;
    int opcao;

    do {
        printf("\n1. Adicionar tarefa\n");
        printf("2. Concluir tarefa\n");
        printf("3. Listar tarefas\n");
        printf("0. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);
        getchar(); // limpar o buffer

        if (opcao == 1) {
            if (total < MAX_TAREFAS) {
                printf("Digite a descrição da tarefa: ");
                fgets(tarefas[total].descricao, TAM_NOME, stdin);
                tarefas[total].descricao[strcspn(tarefas[total].descricao, "\n")] = '\0'; // remover '\n'
                tarefas[total].concluida = 0;
                total++;
            } else {
                printf("Limite de tarefas atingido!\n");
            }
        } else if (opcao == 2) {
            int indice;
            listarTarefas(tarefas, total);
            printf("Digite o número da tarefa a concluir: ");
            scanf("%d", &indice);
            if (indice >= 1 && indice <= total) {
                tarefas[indice - 1].concluida = 1;
                printf("Tarefa marcada como concluída!\n");
            } else {
                printf("Número inválido.\n");
            }
        } else if (opcao == 3) {
            listarTarefas(tarefas, total);
        } else if (opcao == 0) {
            printf("Saindo...\n");
        } else {
            printf("Opção inválida!\n");
        }

    } while (opcao != 0);

    return 0;
}
