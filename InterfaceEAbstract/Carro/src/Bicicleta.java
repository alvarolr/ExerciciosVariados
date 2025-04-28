public class Bicicleta extends Transporte {

    public Bicicleta(String marca, String modelo) {
        super(marca, modelo);
    }

    @Override
    public void mover() {
        System.out.println("A bicicleta " + marca + " " + modelo + " está sendo pedalada.");
    }
}
