public class Carro extends Transporte implements VeiculoEletrico {

    public Carro(String marca, String modelo) {
        super(marca, modelo);
    }

    @Override
    public void mover() {
        System.out.println("O carro " + marca + " " + modelo + " está se movendo na estrada.");
    }

    @Override
    public void carregarBateria() {
        System.out.println("O carro " + marca + " " + modelo + " está carregando a bateria.");
    }
}
