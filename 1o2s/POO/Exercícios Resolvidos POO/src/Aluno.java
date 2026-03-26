public class Aluno extends Pessoa {

    private static int proximoNMec = 100; // Começa em 100
    private int nMec;
    private DateYMD dataInsc;

    public Aluno(String iNome, int iBI, DateYMD iDataNasc, DateYMD iDataInsc) {
        super(iNome, iBI, iDataNasc); // Chama o construtor da superclasse Pessoa
        this.nMec = proximoNMec++;
        this.dataInsc = iDataInsc;
    }

    public Aluno(String iNome, int iBI, DateYMD iDataNasc) {
        super(iNome, iBI, iDataNasc);
        this.nMec = proximoNMec++;
        // Idealmente, extrairias a data do sistema aqui [cite: 32]
        // Exemplo simplificado: this.dataInsc = new DateYMD(19, 3, 2026);
    }

    public int getNMec() {
        return nMec;
    }

    @Override
    public String toString() {
        return super.toString() + "; NMec: " + nMec + "; Inscrito em: " + dataInsc;
    }
}