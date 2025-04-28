public abstract class Animal {
    String nome;

    Animal(String nome) {
        this.nome = nome;
    }

    void dormir() {
        System.out.println(nome + " está dormindo...");
    }

    abstract void emitirSom();
}

