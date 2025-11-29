from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, titular, agencia, conta):
        super().__init__(titular, agencia, conta)
        self.taxaRendimento = 0.005


    def mostrarInfomacoesConta(self):
        super().mostrarInfomacoesConta()
        print(f'Taxa de Rendimento: {self.taxaRendimento}')
        print('-----------------------------------')

    def rendimento(self):
        self.saldo += (self.saldo * self.taxaRendimento)
        print('A conta rendeu!!')
        print('----------------')



contap1 = ContaPoupanca('Alvaro', 1234, 7891)
contap1.mostrarInfomacoesConta()
contap1.depositar(1000000)
contap1.rendimento()
contap1.mostrarInfomacoesConta()
contap1.rendimento()
contap1.mostrarInfomacoesConta()
contap1.rendimento()
contap1.mostrarInfomacoesConta()
contap1.rendimento()
contap1.mostrarInfomacoesConta()
contap1.rendimento()
contap1.mostrarInfomacoesConta()
contap1.rendimento()
contap1.mostrarInfomacoesConta()
contap1.rendimento()
contap1.mostrarInfomacoesConta()