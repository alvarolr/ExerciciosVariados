public class Carro {
    String modelo;
    String marca;
    int ano;
    String cor;

    // Construtor
    public Carro(String m, String marca, int a, String c) {
        modelo = m;
        this.marca = marca;
        ano = a;
        cor = c;
    }

    // Método para mostrar informações
    public void mostrarInfo() {
        System.out.println("Modelo: " + modelo);
        System.out.println("Marca: " + marca);
        System.out.println("Ano: " + ano);
        System.out.println("Cor: " + cor);
    }

    // Método para atualizar a cor
    public void atualizarCor(String novaCor) {
        cor = novaCor;
    }

    // Método principal para teste
    public static void main(String[] args) {
        Carro carro1 = new Carro("Civic", "Honda", 2020, "Prata");
        carro1.mostrarInfo();

        System.out.println("\nAtualizando a cor...");
        carro1.atualizarCor("Preto");
        carro1.mostrarInfo();
    }
}
