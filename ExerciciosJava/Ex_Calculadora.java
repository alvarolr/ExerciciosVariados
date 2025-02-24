public class Calculadora {

    // Método para somar dois inteiros
    public int somar(int a, int b) {
        return a + b;
    }

    // Método para somar três inteiros
    public int somar(int a, int b, int c) {
        return a + b + c;
    }

    // Método para somar dois números de ponto flutuante
    public double somar(double a, double b) {
        return a + b;
    }

    // Método principal para teste
    public static void main(String[] args) {
        Calculadora calc = new Calculadora();

        System.out.println("Soma de 2 e 3: " + calc.somar(2, 3));
        System.out.println("Soma de 1, 2 e 3: " + calc.somar(1, 2, 3));
        System.out.println("Soma de 2.5 e 3.7: " + calc.somar(2.5, 3.7));
    }
}
