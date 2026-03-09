import java.util.Scanner;

public class Ex2_5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double v1, d1, v2, d2;

        // Validação para o primeiro trajeto
        do {
            System.out.print("Velocidade 1 (v1) e Distância 1 (d1): ");
            v1 = sc.nextDouble();
            d1 = sc.nextDouble();
            if (v1 <= 0 || d1 <= 0) System.out.println("Erro: Use valores positivos!");
        } while (v1 <= 0 || d1 <= 0); // Repete se for inválido [cite: 8, 30]

        // Validação para o segundo trajeto
        do {
            System.out.print("Velocidade 2 (v2) e Distância 2 (d2): ");
            v2 = sc.nextDouble();
            d2 = sc.nextDouble();
            if (v2 <= 0 || d2 <= 0) System.out.println("Erro: Use valores positivos!");
        } while (v2 <= 0 || d2 <= 0);

        // Velocidade Média = Distância Total / Tempo Total [cite: 29]
        // Tempo = Distância / Velocidade
        double tempoTotal = (d1 / v1) + (d2 / v2);
        double vmFinal = (d1 + d2) / tempoTotal;

        System.out.printf("A velocidade média final é: %.2f\n", vmFinal);
        sc.close();
    }
}