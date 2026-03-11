import java.util.Scanner;

public class KmToMiles {
    public static void main(String[] args) {
        double km, miles;
        Scanner sc = new Scanner(System.in);
        System.out.println("Km? ");
        km = sc.nextDouble();
        miles = km / 1.689;
        System.out.println("A disância em milhas é " + miles);
        sc.close();
    }
}
