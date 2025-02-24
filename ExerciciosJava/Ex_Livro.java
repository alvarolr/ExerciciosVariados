public class Livro {
    String titulo;
    String autor;

    // Construtor padrão
    public Livro() {
        titulo = "Sem Título";
        autor = "Desconhecido";
    }

    // Construtor parametrizado
    public Livro(String titulo, String autor) {
        this.titulo = titulo;
        this.autor = autor;
    }

    // Método para exibir informações
    public void exibirInfo() {
        System.out.println("Título: " + titulo);
        System.out.println("Autor: " + autor);
    }

    // Método principal para teste
    public static void main(String[] args) {
        Livro livro1 = new Livro();
        Livro livro2 = new Livro("1984", "George Orwell");

        livro1.exibirInfo();
        System.out.println();
        livro2.exibirInfo();
    }
}
