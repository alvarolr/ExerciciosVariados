public class App {
    public static void main(String[] args) throws Exception {
        Pato pato = new Pato("Donald");

        pato.dormir();        // método herdado da classe abstrata
        pato.emitirSom();     // método sobrescrito da classe abstrata
        pato.voar();          // método da interface Voar
        pato.nadar();         // método da interface Nadar
    }
}
