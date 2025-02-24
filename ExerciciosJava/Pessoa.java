public class Pessoa {
    String nome;
    int idade;
    String genero;
    String cidade;

    // Construtor usando 'this'
    public Pessoa(String nome, int idade, String genero, String cidade) {
        this.nome = nome;       // 'this' se refere ao atributo da classe
        this.idade = idade;
        this.genero = genero;
        this.cidade = cidade;
    }

    // Método para mostrar informações
    public void mostrarInfo() {
    System.out.println("Nome: " + this.nome);
    System.out.println("Idade: " + this.idade + " anos");
    System.out.println("Gênero: " + this.genero);
    System.out.println("Cidade: " + this.cidade);
    }   

    // Método para alterar a idade
    public void alterarIdade(int novaIdade) {
        this.idade = novaIdade;
    }

    // Método para alterar a cidade
    public void mudarCidade(String novaCidade) {
        this.cidade = novaCidade;
    }

    // Método principal para teste
    public static void main(String[] args) {
        Pessoa pessoa1 = new Pessoa("Ana", 25, "Feminino", "São Paulo");

        pessoa1.mostrarInfo();

        System.out.println("\nAlterando a idade...");
        pessoa1.alterarIdade(26);
        pessoa1.mostrarInfo();

        System.out.println("\nMudando a cidade...");
        pessoa1.mudarCidade("Rio de Janeiro");
        pessoa1.mostrarInfo();
    }
}
