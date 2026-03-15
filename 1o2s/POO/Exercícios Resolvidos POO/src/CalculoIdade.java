import java.time.LocalDate;
import java.time.Period;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class CalculoIdade {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Cálculo de Idade ===");
        System.out.print("Introduza o ano de nascimento: ");
        int ano = sc.nextInt();
        System.out.print("Introduza o mês de nascimento (1-12): ");
        int mes = sc.nextInt();
        System.out.print("Introduza o dia de nascimento: ");
        int dia = sc.nextInt();

        LocalDate dataNascimento = LocalDate.of(ano, mes, dia);
        LocalDate dataAtual = LocalDate.now();

        if (dataNascimento.isAfter(dataAtual)) {
            System.out.println("A data de nascimento não pode ser no futuro.");
        } else {
            Period idade = Period.between(dataNascimento, dataAtual);
            long totalMeses = ChronoUnit.MONTHS.between(dataNascimento, dataAtual);
            long totalDias = ChronoUnit.DAYS.between(dataNascimento, dataAtual);

            System.out.println("\nResultados:");
            System.out.printf("Idade exata: %d anos, %d meses e %d dias\n", idade.getYears(), idade.getMonths(), idade.getDays());
            System.out.println("Idade em anos: " + idade.getYears());
            System.out.println("Total equivalente em meses: " + totalMeses);
            System.out.println("Total equivalente em dias: " + totalDias);
        }
        sc.close();
    }
}