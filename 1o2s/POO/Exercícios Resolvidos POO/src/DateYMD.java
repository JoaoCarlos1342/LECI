import java.util.Scanner;

public class DateYMD {
    private int year, month, day;

    // Construtor alterado para Ano, Mês, Dia
    public DateYMD(int year, int month, int day) {
        if (!valid(year, month, day)) {
            throw new IllegalArgumentException("Data inválida!");
        }
        this.year = year;
        this.month = month;
        this.day = day;
    }

    public static boolean validMonth(int month) {
        return month >= 1 && month <= 12;
    }

    public static boolean leapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }

    public static int monthDays(int month, int year) {
        if (!validMonth(month)) return 0;
        int[] days = {0, 31, leapYear(year) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        return days[month];
    }

    // Assinatura do método valid atualizada para Ano, Mês, Dia
    public static boolean valid(int year, int month, int day) {
        return validMonth(month) && day >= 1 && day <= monthDays(month, year);
    }

    // Assinatura do método set atualizada para Ano, Mês, Dia
    public void set(int year, int month, int day) {
        if (valid(year, month, day)) {
            this.year = year;
            this.month = month;
            this.day = day;
        } else {
            System.out.println("Data inválida ignorada.");
        }
    }

    public int getYear() { return year; }
    public int getMonth() { return month; }
    public int getDay() { return day; }

    // Incremento Corrigido (soma ao dia, não ao ano)
    public void increment(int days) {
        this.day += days;
        while (this.day > monthDays(this.month, this.year)) {
            this.day -= monthDays(this.month, this.year);
            this.month++;
            if (this.month > 12) {
                this.month = 1;
                this.year++;
            }
        }
    }

    // Decremento Corrigido (subtrai ao dia, não ao ano)
    public void decrement(int days) {
        this.day -= days;
        while (this.day < 1) {
            this.month--;
            if (this.month < 1) {
                this.month = 12;
                this.year--;
            }
            this.day += monthDays(this.month, this.year);
        }
    }

    public void increment() { increment(1); }
    public void decrement() { decrement(1); }

    @Override
    public String toString() {
        return String.format("%04d-%02d-%02d", year, month, day);
    }

    // Programa de teste
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        DateYMD current = null;
        int op;

        do {
            System.out.println("\nDate operations:");
            System.out.println("1 - create new date");
            System.out.println("2 - show current date");
            System.out.println("3 - increment date");
            System.out.println("4 - decrement date");
            System.out.println("0 - exit");
            System.out.print("Opção: ");
            op = sc.nextInt();

            switch (op) {
                case 1:
                    System.out.print("Ano Mês Dia: ");
                    try {
                        current = new DateYMD(sc.nextInt(), sc.nextInt(), sc.nextInt());
                    } catch (IllegalArgumentException e) {
                        System.out.println(e.getMessage());
                    }
                    break;
                case 2:
                    if (current != null) System.out.println("Data atual: " + current);
                    else System.out.println("Nenhuma data criada.");
                    break;
                case 3:
                    if (current != null) {
                        System.out.print("Quantos dias a incrementar? ");
                        current.increment(sc.nextInt());
                    }
                    break;
                case 4:
                    if (current != null) {
                        System.out.print("Quantos dias a decrementar? ");
                        current.decrement(sc.nextInt());
                    }
                    break;
            }
        } while (op != 0);
        sc.close();
    }
}