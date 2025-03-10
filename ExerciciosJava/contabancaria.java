class ContaBancaria {
    private int numeroConta;
    private String titular;
    private double saldo;

    // Construtor da classe
    public ContaBancaria(int numeroConta, String titular) {
        this.numeroConta = numeroConta;
        this.titular = titular;
        this.saldo = 0.0; // Conta inicia com saldo zero
    }

    // Getter para número da conta
    public int getNumeroConta() {
        return numeroConta;
    }

    // Setter para número da conta
    public void setNumeroConta(int numeroConta) {
        this.numeroConta = numeroConta;
    }

    // Getter para titular da conta
    public String getTitular() {
        return titular;
    }

    // Setter para titular da conta
    public void setTitular(String titular) {
        this.titular = titular;
    }

    // Getter para saldo
    public double getSaldo() {
        return saldo;
    }

    // Método para depositar dinheiro
    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
            System.out.println("Depósito de R$ " + valor + " realizado com sucesso.");
        } else {
            System.out.println("Erro: O valor do depósito deve ser maior que zero.");
        }
    }

    // Método para sacar dinheiro
    public void sacar(double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            System.out.println("Saque de R$ " + valor + " realizado com sucesso.");
        } else {
            System.out.println("Erro: Saldo insuficiente ou valor inválido.");
        }
    }
}

// Classe principal para testar
public class Main {
    public static void main(String[] args) {
        // Criando um objeto da classe ContaBancaria
        ContaBancaria conta = new ContaBancaria(12345, "João Silva");

        // Exibindo informações iniciais
        System.out.println("Conta criada para: " + conta.getTitular());
        System.out.println("Número da Conta: " + conta.getNumeroConta());
        System.out.println("Saldo inicial: R$ " + conta.getSaldo());

        // Realizando operações
        conta.depositar(1500.00);
        conta.sacar(500.00);

        // Exibindo saldo final
        System.out.println("Saldo final: R$ " + conta.getSaldo());
    }
}
