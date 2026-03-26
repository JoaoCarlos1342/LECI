public abstract class Date {
    
    // Métodos estáticos auxiliares
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

    // Método corrigido para "valid" e com a ordem (year, month, day)
    public static boolean valid(int year, int month, int day) {
        return validMonth(month) && day >= 1 && day <= monthDays(month, year);
    }

    // Métodos que as classes filhas são OBRIGADAS a ter
    public abstract int getYear();
    public abstract int getMonth();
    public abstract int getDay();

    // O contrato agora exige parâmetros (int days)
    public abstract void increment(int days);
    public abstract void decrement(int days);

    // Métodos de atalho (se não passar dias, soma/subtrai 1)
    public void increment() { increment(1); }
    public void decrement() { decrement(1); }

    @Override
    public String toString() {
        return String.format("%04d-%02d-%02d", getYear(), getMonth(), getDay());
    }
}