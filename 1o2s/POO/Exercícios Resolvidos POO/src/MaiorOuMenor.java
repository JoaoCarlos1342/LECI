import java.util.Scanner;
import java.util.Random;

public class MaiorOuMenor {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("=== Jogo: Adivinha o Número Secreto ===");
        System.out.println("1 - Eu (Humano) tento adivinhar o número do PC");
        System.out.println("2 - O PC tenta adivinhar o meu número");
        System.out.print("Escolhe quem vai adivinhar (1 ou 2): ");
        int modo = scanner.nextInt();

        System.out.println("----------------------------------------------");

        if (modo == 1) {
            // MODO 1: Humano adivinha o número do PC
            int numeroPC = random.nextInt(100) + 1;
            int palpite = 0;
            int tentativas = 0;

            System.out.println("Pensei num número entre 1 e 100. Tenta adivinhar!");

            while (palpite != numeroPC) {
                System.out.print("O teu palpite: ");
                palpite = scanner.nextInt();
                tentativas++;

                if (palpite < numeroPC) {
                    System.out.println("O meu número é MAIOR!");
                } else if (palpite > numeroPC) {
                    System.out.println("O meu número é MENOR!");
                } else {
                    System.out.println("Parabéns! Acertaste no número " + numeroPC + " em " + tentativas + " tentativas.");
                }
            }

        } else if (modo == 2) {
            // MODO 2: PC adivinha o número do Humano
            int min = 1;
            int max = 100;
            int tentativas = 0;
            boolean acertou = false;

            System.out.println("Pensa num número entre 1 e 100.");
            System.out.println("Responde com:");
            System.out.println(" 'M' se o teu número for Maior que o meu palpite");
            System.out.println(" 'N' se o teu número for Menor que o meu palpite");
            System.out.println(" 'C' se eu tiver acertado (Certo)");
            System.out.println("----------------------------------------------");

            while (!acertou && min <= max) {
                // O PC dá o palpite exatamente no meio do intervalo possível (Pesquisa Binária)
                int palpitePC = (min + max) / 2;
                tentativas++;

                System.out.print("O teu número é o " + palpitePC + "? (M/N/C): ");
                String resposta = scanner.next().trim().toUpperCase();

                if (resposta.equals("C")) {
                    System.out.println("Ah! Sou uma máquina inteligente! Acertei em " + tentativas + " tentativas.");
                    acertou = true;
                } else if (resposta.equals("M")) {
                    min = palpitePC + 1; // O número é maior, logo o novo mínimo passa a ser o palpite + 1
                } else if (resposta.equals("N")) {
                    max = palpitePC - 1; // O número é menor, logo o novo máximo passa a ser o palpite - 1
                } else {
                    System.out.println("Opção inválida. Por favor, usa M, N ou C.");
                    tentativas--; // Não conta como tentativa se o utilizador se enganar na letra
                }
            }

            // Uma pequena brincadeira caso o utilizador minta nas respostas e as opções se esgotem
            if (min > max) {
                System.out.println("Espera aí... as contas não batem certo. Tu mentiste-me nas dicas!");
            }

        } else {
            System.out.println("Opção inválida! Fim de jogo.");
        }

        scanner.close();
    }
}