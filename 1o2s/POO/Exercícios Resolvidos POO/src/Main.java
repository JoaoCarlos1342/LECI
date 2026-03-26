import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Abstração em ação: A variável é do tipo Date, não interessa se é YMD ou ND
        Date current = null;
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
                    System.out.print("Escolha a implementação (1 para YMD, 2 para ND): ");
                    int tipo = sc.nextInt();
                    System.out.print("Ano Mês Dia: ");
                    try {
                        int y = sc.nextInt();
                        int m = sc.nextInt();
                        int d = sc.nextInt();

                        // É aqui que o Polimorfismo acontece!
                        if (tipo == 1) {
                            current = new DateYMD(y, m, d);
                        } else {
                            current = new DateND(y, m, d);
                        }
                    } catch (IllegalArgumentException e) {
                        System.out.println(e.getMessage());
                    }
                    break;
                case 2:
                    // O Java sabe automaticamente qual toString() chamar
                    if (current != null)
                        System.out.println("Data atual: " + current);
                    else
                        System.out.println("Nenhuma data criada.");
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