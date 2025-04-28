public class App {
    public static void main(String[] args) throws Exception {
        Carro carro = new Carro("Tesla", "Model 3");
        Bicicleta bicicleta = new Bicicleta("Caloi", "Elite");

        System.out.println("--- Carro ---");
        carro.mover();
        carro.carregarBateria();

        System.out.println("\n--- Bicicleta ---");
        bicicleta.mover();
    }
}
