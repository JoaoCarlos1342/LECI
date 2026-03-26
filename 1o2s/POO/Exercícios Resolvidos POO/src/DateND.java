public class DateND extends Date {
    private int daysFrom2000;

    public DateND(int year, int month, int day) {
        if (!valid(year, month, day)) {
            throw new IllegalArgumentException("Data inválida!");
        }
        this.daysFrom2000 = dateToDays(year, month, day);
    }

    private int dateToDays(int year, int month, int day) {
        int days = 0;
        int y = 2000;
        while (y < year) {
            days += leapYear(y) ? 366 : 365;
            y++;
        }
        while (y > year) {
            y--;
            days -= leapYear(y) ? 366 : 365;
        }
        for (int m = 1; m < month; m++) {
            days += monthDays(m, year);
        }
        days += (day - 1);
        return days;
    }

    private int[] getYMD() {
        int d = daysFrom2000;
        int y = 2000;

        if (d >= 0) {
            while (true) {
                int daysInYear = leapYear(y) ? 366 : 365;
                if (d < daysInYear)
                    break;
                d -= daysInYear;
                y++;
            }
        } else {
            while (d < 0) {
                y--;
                int daysInYear = leapYear(y) ? 366 : 365;
                d += daysInYear;
            }
        }

        int m = 1;
        while (true) {
            int daysInMonth = monthDays(m, y);
            if (d < daysInMonth)
                break;
            d -= daysInMonth;
            m++;
        }
        return new int[] { y, m, d + 1 };
    }

    @Override
    public int getYear() {
        return getYMD()[0];
    }

    @Override
    public int getMonth() {
        return getYMD()[1];
    }

    @Override
    public int getDay() {
        return getYMD()[2];
    }

    // O seu incremento/decremento de vários dias fica super simples aqui!
    @Override
    public void increment(int days) {
        daysFrom2000 += days;
    }

    @Override
    public void decrement(int days) {
        daysFrom2000 -= days;
    }
}