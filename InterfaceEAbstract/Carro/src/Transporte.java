public abstract class Transporte {
    protected String marca;
    protected String modelo;

    public Transporte(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
    }

    public abstract void mover();
}
