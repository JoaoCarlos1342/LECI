import java.time.LocalDate;
import java.util.Scanner;

public class CalendarioAnual {
    private int year;
    private int[][] events; // vetor bidimensional 

    // Alínea iii) Construtor modificado para calcular automaticamente o dia da semana
    public CalendarioAnual(int year) { // [cite: 31]
        this.year = year;
        this.events = new int[13][32];
    }

    public int year() { return year; } // [cite: 32]

    public int firstWeekdayOfYear() { // [cite: 32]
        return firstWeekdayOfMonth(1);
    }

    public int firstWeekdayOfMonth(int month) { // 
        // Usa LocalDate para determinar o dia da semana (alínea iii)
        int dayOfWeek = LocalDate.of(this.year, month, 1).getDayOfWeek().getValue();
        // Mapeia de 1=Segunda...7=Domingo (Java) para 1=Domingo...7=Sábado (Exercício) [cite: 31]
        return (dayOfWeek % 7) + 1;
    }

    public void addEvent(DateYMD date) { // 
        if (date.getYear() == this.year) {
            events[date.getMonth()][date.getDay()]++;
        }
    }

    public void removeEvent(DateYMD date) { // 
        if (date.getYear() == this.year && events[date.getMonth()][date.getDay()] > 0) {
            events[date.getMonth()][date.getDay()]--;
        }
    }

    public String printMonth(int month) { // [cite: 36]
        String[] monthNames = {"", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("%s %d\n", monthNames[month], year)); // [cite: 38, 40]
        sb.append("Su Mo Tu We Th Fr Sa\n"); // [cite: 39, 41]

        int firstDay = firstWeekdayOfMonth(month);
        int daysInMonth = DateYMD.monthDays(month, year);

        // Preenche espaços em branco iniciais
        for (int i = 1; i < firstDay; i++) {
            sb.append("   ");
        }

        for (int day = 1; day <= daysInMonth; day++) {
            if (events[month][day] > 0) {
                sb.append(String.format("*%2d", day)); // Precedido de * se tiver eventos [cite: 36, 42]
            } else {
                sb.append(String.format("%3d", day)); // [cite: 39]
            }

            if ((day + firstDay - 1) % 7 == 0 || day == daysInMonth) {
                sb.append("\n");
            }
        }
        return sb.toString();
    }

    @Override
    public String toString() { // [cite: 37]
        StringBuilder sb = new StringBuilder();
        for (int m = 1; m <= 12; m++) {
            sb.append(printMonth(m)).append("\n");
        }
        return sb.toString();
    }

    // Programa de teste
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        CalendarioAnual cal = null;
        int op;

        do {
            System.out.println("Calendar operations:"); // [cite: 44]
            System.out.println("1 - create new calendar"); // [cite: 45]
            System.out.println("2 - print calendar month"); // [cite: 46, 47]
            System.out.println("3 - print calendar"); // [cite: 48]
            System.out.println("0 - exit"); // [cite: 49]
            System.out.print("Opção: ");
            op = sc.nextInt();

            switch (op) {
                case 1:
                    System.out.print("Indique o ano: ");
                    cal = new CalendarioAnual(sc.nextInt());
                    break;
                case 2:
                    if (cal != null) {
                        System.out.print("Mês (1-12): ");
                        System.out.println("\n" + cal.printMonth(sc.nextInt())); // [cite: 36, 47]
                    }
                    break;
                case 3:
                    if (cal != null) {
                        System.out.println("\n" + cal.toString()); // [cite: 37, 48]
                    }
                    break;
            }
        } while (op != 0);
        sc.close();
    }
}