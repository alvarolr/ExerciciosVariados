public class Pato extends Animal implements Voar, Nadar {
  
    Pato(String nome) {
        super(nome);
    }

    @Override
    public void nadar(){
        System.out.println("Pato Esta nadando");
    }

    @Override
    public void voar(){
        System.out.println("Pato Esta voando");
    }

    @Override
    void emitirSom() {
        System.out.println(nome + " faz: Quack Quack!");
    }
    
}
