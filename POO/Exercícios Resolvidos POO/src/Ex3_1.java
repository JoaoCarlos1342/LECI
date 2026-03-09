import java.util.Scanner;

public class Ex3_1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero = 0;

        // Validação da entrada: repete até o valor ser um inteiro positivo
        do {
            System.out.print("Introduza um número inteiro positivo: ");
            // Verifica se o que foi introduzido é sequer um número inteiro
            while (!sc.hasNextInt()) {
                System.out.println("Isso não é um número inteiro válido.");
                System.out.print("Introduza um número inteiro positivo: ");
                sc.next(); // Descarta a entrada inválida
            }
            numero = sc.nextInt();

            if (numero <= 0) {
                System.out.println("O número tem de ser positivo (maior que zero).");
            }
        } while (numero <= 0);

        // Cálculo da soma dos números primos até ao valor introduzido
        int soma = 0;
        for (int i = 1; i <= numero; i++) {
            if (ePrimo(i)) {
                soma += i;
            }
        }

        System.out.println("A soma dos números primos até " + numero + " é: " + soma);
        sc.close();
    }

    /**
     * Função que verifica se um número é primo.
     * @param n Número a verificar
     * @return true se for primo, false caso contrário
     */
    public static boolean ePrimo(int n) {
        // O número 1 não é primo (não tem dois divisores distintos) e números menores que 1 também não
        if (n <= 1) {
            return false;
        }

        // Verifica divisibilidade de 2 até à raiz quadrada do número (para otimização)
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false; // Se for divisível por outro número, não é primo
            }
        }

        return true;
    }
}