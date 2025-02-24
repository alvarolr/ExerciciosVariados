public class Aluno {
    String nome;
    String matricula;
    String curso;
    double nota;

    // Construtor
    public Aluno(String nome, String matricula, String curso, double notaInicial) {
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
        this.nota = notaInicial;
    }

    // Mostrar informações
    public void mostrarInfo() {
        System.out.println("Nome: " + nome);
        System.out.println("Matrícula: " + matricula);
        System.out.println("Curso: " + curso);
        System.out.println("Nota: " + nota);
    }

    // Verificar aprovação
    public void verificarAprovacao() {
        if (nota >= 6) {
            System.out.println(nome + " está aprovado.");
        } else {
            System.out.println(nome + " está reprovado.");
        }
    }

    // Método principal para teste
    public static void main(String[] args) {
        Aluno aluno1 = new Aluno("Maria", "2023001", "Engenharia", 7.5);
        aluno1.mostrarInfo();
        aluno1.verificarAprovacao();

        System.out.println();
        Aluno aluno2 = new Aluno("João", "2023002", "Direito", 5.0);
        aluno2.mostrarInfo();
        aluno2.verificarAprovacao();
    }
}
