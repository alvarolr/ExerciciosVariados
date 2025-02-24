public class Retangulo {
    double base;
    double altura;

    // Construtor para definir base e altura
    public Retangulo(double base, double a) {
        this.base = base;
        altura = a;
    }

    // Construtor para criar um quadrado
    public Retangulo(double lado) {
        base = lado;
        altura = lado;
    }

    // Método para calcular área
    public double calcularArea() {
        return base * altura;
    }

    // Método principal para teste
    public static void main(String[] args) {
        Retangulo retangulo = new Retangulo(5, 3);
        Retangulo quadrado = new Retangulo(4);

        System.out.println("Área do retângulo: " + retangulo.calcularArea());
        System.out.println("Área do quadrado: " + quadrado.calcularArea());
    }
}
