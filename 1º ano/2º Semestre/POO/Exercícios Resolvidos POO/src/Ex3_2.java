import java.util.Scanner;

public class Ex3_2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String continuar;

        System.out.println("Bem-vindo ao jogo AltoBaixo!");

        // Ciclo externo para controlar se o utilizador quer jogar novamente
        do {
            // Gera um número aleatório entre 1 e 100
            int numeroSecreto = (int) (Math.random() * 100) + 1;
            int tentativas = 0;
            int palpite = 0;

            System.out.println("\nPensei num número entre 1 e 100. Tente adivinhar!");

            // Ciclo interno para as tentativas de adivinhar o número
            while (palpite != numeroSecreto) {
                System.out.print("Introduza a sua tentativa: ");

                // Validação simples para evitar erros se o utilizador escrever letras
                while (!sc.hasNextInt()) {
                    System.out.println("Isso não é um número válido. Tente de novo.");
                    sc.next(); // Descarta a entrada inválida
                }
                palpite = sc.nextInt();
                tentativas++; // Incrementa o contador de tentativas

                // Verifica o palpite
                if (palpite < numeroSecreto) {
                    System.out.println("Demasiado baixa!");
                } else if (palpite > numeroSecreto) {
                    System.out.println("Demasiado alta!");
                } else {
                    System.out.println("Parabéns! Acertou no número em " + tentativas + " tentativas.");
                }
            }

            // Pergunta se quer jogar de novo
            System.out.print("Pretende continuar? Prima (S)im: ");
            continuar = sc.next();

            // O ciclo repete-se se o utilizador escrever "S" ou "Sim" (ignorando maiúsculas/minúsculas)
        } while (continuar.equalsIgnoreCase("S") || continuar.equalsIgnoreCase("Sim"));

        System.out.println("Obrigado por jogar! Até à próxima.");
        sc.close();
    }
}