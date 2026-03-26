public class DateYMD extends Date {
    private int year, month, day;

    public DateYMD(int year, int month, int day) {
        // Agora o método valid() existe na classe Date, por isso isto vai funcionar
        if (!valid(year, month, day)) {
            throw new IllegalArgumentException("Data inválida!");
        }
        this.year = year;
        this.month = month;
        this.day = day;
    }

    @Override
    public int getYear() {
        return year;
    }

    @Override
    public int getMonth() {
        return month;
    }

    @Override
    public int getDay() {
        return day;
    }

    // O Override agora bate certo com o que está definido no ficheiro Date.java
    @Override
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

    @Override
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
}