public class Bolseiro extends Aluno {
    private Professor orientador;
    private double bolsa;

    public Bolseiro(String nome, int cc, DateYMD dataNasc, Professor orientador, double bolsa) {
        // Usamos o construtor do Aluno que assume a data de inscrição atual
        super(nome, cc, dataNasc);
        this.orientador = orientador;
        this.bolsa = bolsa;
    }

    public Professor getOrientador() {
        return orientador;
    }

    public void setOrientador(Professor orientador) {
        this.orientador = orientador;
    }

    public double getBolsa() {
        return bolsa;
    }

    public void setBolsa(double bolsa) {
        this.bolsa = bolsa;
    }

    @Override
    public String toString() {
        return super.toString() + "; Orientador: " + orientador.getNome() + "; Bolsa: " + bolsa;
    }
}