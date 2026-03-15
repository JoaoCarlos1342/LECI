import java.util.Scanner;

public class CalculadoraInvestimento {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Calculadora de Juros Compostos ===");

        // 1. Valor do depósito
        System.out.print("Qual o valor que vai depositar periodicamente (€)? ");
        double depositoPeriodico = scanner.nextDouble();

        // 2. Frequência do depósito
        System.out.print("De quantos em quantos meses fará este depósito? (ex: 1 = mensal, 12 = anual): ");
        int freqDepositoMeses = scanner.nextInt();

        // 3. Taxa de rentabilidade
        System.out.print("Qual a taxa de rentabilidade anual esperada (%)? ");
        double taxaAnual = scanner.nextDouble() / 100.0; // Converte para decimal (ex: 5% -> 0.05)

        // 4. Frequência de capitalização
        System.out.print("De quantos em quantos meses os juros são capitalizados? (ex: 1 = mensal, 12 = anual): ");
        int freqCapitalizacaoMeses = scanner.nextInt();

        // 5. Tempo do investimento
        System.out.print("Durante quantos anos quer manter o investimento? ");
        double anos = scanner.nextDouble();

        int totalMeses = (int) (anos * 12);
        double saldoTotal = 0.0;
        double totalInvestido = 0.0;

        // Cálculo da taxa de juros equivalente para o período de capitalização
        // Fórmula: (1 + taxaAnual)^(meses_capitalizacao / 12) - 1
        double taxaPeriodo = Math.pow(1.0 + taxaAnual, freqCapitalizacaoMeses / 12.0) - 1.0;

        // Simulação do investimento mês a mês
        for (int mes = 1; mes <= totalMeses; mes++) {

            // 1. Rendimento: Aplica os juros sobre o saldo (se for o mês correto de capitalização)
            // É calculado antes do novo depósito (assume que depósitos são feitos no final do mês)
            if (mes % freqCapitalizacaoMeses == 0 && saldoTotal > 0) {
                saldoTotal += saldoTotal * taxaPeriodo;
            }

            // 2. Aporte: Adiciona o depósito ao saldo (se for o mês correto de depósito)
            if (mes % freqDepositoMeses == 0) {
                saldoTotal += depositoPeriodico;
                totalInvestido += depositoPeriodico;
            }
        }

        // Apresentação dos Resultados
        System.out.println("\n=== Resumo do Investimento ===");
        System.out.printf("Total Investido (do seu bolso): %.2f €\n", totalInvestido);
        System.out.printf("Juros Ganhos: %.2f €\n", (saldoTotal - totalInvestido));
        System.out.printf("Valor Total Acumulado: %.2f €\n", saldoTotal);

        scanner.close();
    }
}