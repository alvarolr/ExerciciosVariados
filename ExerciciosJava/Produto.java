public class Produto {
    String nome;
    String categoria;
    double preco;
    int estoque;

    // Construtor
    public Produto(String nome, String categoria, double preco, int estoque) {
        this.nome = nome;
        this.categoria = categoria;
        this.preco = preco;
        this.estoque = estoque;
    }

    // Mostrar informações
    public void mostrarInfo() {
        System.out.println("Produto: " + nome);
        System.out.println("Categoria: " + categoria);
        System.out.println("Preço: R$" + preco);
        System.out.println("Estoque: " + estoque + " unidades");
    }

    // Aplicar desconto
    public void aplicarDesconto(double percentual) {
        preco = preco - (preco * percentual / 100);
    }

    // Atualizar estoque
    public void atualizarEstoque(int quantidadeVendida) {
        if (quantidadeVendida <= estoque) {
            estoque -= quantidadeVendida;
            System.out.println(quantidadeVendida + " unidades vendidas.");
        } else {
            System.out.println("Estoque insuficiente.");
        }
    }

    // Método principal para teste
    public static void main(String[] args) {
        Produto prod1 = new Produto("Notebook", "Eletrônicos", 3000.00, 10);
        prod1.mostrarInfo();

        System.out.println("\nAplicando 10% de desconto...");
        prod1.aplicarDesconto(10);
        prod1.mostrarInfo();

        System.out.println("\nVendendo 3 unidades...");
        prod1.atualizarEstoque(3);
        prod1.mostrarInfo();
    }
}
