import java.util.Scanner;

public class Ex2_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Distância em km: ");
        double km = sc.nextDouble();
        double milhas = km / 1.609;

        System.out.printf("%.2f km equivalem a %.2f milhas.\n", km, milhas);
        sc.close();
    }
}