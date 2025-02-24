public class ContaBancaria {
    String numeroConta;
    String titular;
    double saldo;
    String agencia;

    // Construtor
    public ContaBancaria(String numero, String titular, double saldoInicial, String agencia) {
        this.numeroConta = numero;
        this.titular = titular;
        this.saldo = saldoInicial;
        this.agencia = agencia;
    }

    // Mostrar informações
    public void mostrarInfo() {
        System.out.println("Conta: " + numeroConta);
        System.out.println("Titular: " + titular);
        System.out.println("Agência: " + agencia);
        System.out.println("Saldo: R$" + saldo);
    }

    // Depositar
    public void depositar(double valor) {
        saldo += valor;
        System.out.println("Depósito de R$" + valor + " realizado.");
    }

    // Sacar
    public void sacar(double valor) {
        if (valor <= saldo) {
            saldo -= valor;
            System.out.println("Saque de R$" + valor + " realizado.");
        } else {
            System.out.println("Saldo insuficiente para saque.");
        }
    }

    // Método principal para teste
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria("12345-6", "Ana", 500.00, "001");
        conta.mostrarInfo();

        System.out.println("\nDepositando R$200...");
        conta.depositar(200);
        conta.mostrarInfo();

        System.out.println("\nSacando R$100...");
        conta.sacar(100);
        conta.mostrarInfo();

        System.out.println("\nTentando sacar R$800...");
        conta.sacar(800);
    }
}
