import java.util.Scanner;

public class Ex2_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Montante investido: ");
        double investimento = sc.nextDouble(); // [cite: 23]

        System.out.print("Taxa de juro mensal (em %): ");
        double taxa = sc.nextDouble() / 100; // Converte p.ex. 1 para 0.01 [cite: 23]

        // Cálculo mês a mês (juro composto)
        double mes1 = investimento + (investimento * taxa);
        double mes2 = mes1 + (mes1 * taxa);
        double mes3 = mes2 + (mes2 * taxa); // Valor ao final de 3 meses [cite: 24]

        System.out.printf("Valor total após 3 meses: %.3f euros\n", mes3);
        // Exemplo do guião: 5000€ a 1% -> 5151.505€ [cite: 25]

        sc.close();
    }
}