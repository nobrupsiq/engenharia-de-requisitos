import java.util.*;

class Atividade {
    String descricao;
    boolean concluida;

    Atividade(String descricao) {
        this.descricao = descricao;
        this.concluida = false;
    }

    void marcarComoConcluida() {
        this.concluida = true;
    }

    @Override
    public String toString() {
        return (concluida ? "[X] " : "[ ] ") + descricao;
    }
}

class SistemaAtividades {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Atividade> lista = new ArrayList<>();
        int opcao;

        do {
            System.out.println("\n=== SISTEMA DE GESTÃO DE ATIVIDADES ===");
            System.out.println("1 - Adicionar atividade");
            System.out.println("2 - Listar atividades");
            System.out.println("3 - Concluir atividade");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();
            scanner.nextLine(); // limpar o buffer

            switch (opcao) {
                case 1:
                    System.out.print("Digite a descrição da atividade: ");
                    String desc = scanner.nextLine();
                    lista.add(new Atividade(desc));
                    System.out.println("Atividade adicionada.");
                    break;
                case 2:
                    System.out.println("\n--- Lista de Atividades ---");
                    for (int i = 0; i < lista.size(); i++) {
                        System.out.println((i + 1) + " - " + lista.get(i));
                    }
                    break;
                case 3:
                    System.out.print("Digite o número da atividade a concluir: ");
                    int num = scanner.nextInt();
                    if (num >= 1 && num <= lista.size()) {
                        lista.get(num - 1).marcarComoConcluida();
                        System.out.println("Atividade concluída!");
                    } else {
                        System.out.println("Número inválido.");
                    }
                    break;
                case 0:
                    System.out.println("Encerrando sistema...");
                    break;
                default:
                    System.out.println("Opção inválida.");
            }
        } while (opcao != 0);

        scanner.close();
        }
}
