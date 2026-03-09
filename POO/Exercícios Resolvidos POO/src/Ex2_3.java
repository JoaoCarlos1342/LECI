import java.util.Scanner;

public class Ex2_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantidade de água (M em kg): ");
        double m = sc.nextDouble(); // Massa em kg 

        System.out.print("Temperatura inicial (Celsius): ");
        double tempInicial = sc.nextDouble(); // 

        System.out.print("Temperatura final (Celsius): ");
        double tempFinal = sc.nextDouble(); // 

        // Cálculo da energia Q em Joules [cite: 21]
        double q = m * (tempFinal - tempInicial) * 4184;

        System.out.printf("A energia necessária é de %.2f Joules.\n", q);
        sc.close();
    }
}