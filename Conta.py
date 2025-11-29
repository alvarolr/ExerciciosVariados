class Conta:
    def __init__(self, titular, agencia, conta):
        self.titular = titular
        self.agencia = agencia
        self.conta = conta
        self.saldo = 0
        
    def mostrarInfomacoesConta(self):
        print('-----------------------------------')
        print(f'Nome do titular:{self.titular}')
        print(f'Agencia do Titular:{self.agencia}')
        print(f'Conta do Titular:{self.conta}')
        print(f'Saldo do titular:{self.saldo}')
        
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Deposito de {valor} realizado')
            print('-----------------------------------')
        else:
            print('Valor invalido para deposito')
            print('-----------------------------------')
    
    def sacar(self, valor):
        if valor > self.saldo or valor <= 0:
            print('Valor invalido para saque')
            print('-----------------------------------')
        else:
            self.saldo -= valor
            print(f'Saque de {valor} realizado')
            print('-----------------------------------')
            
    
    def transferir(self, valor, Conta):
        if valor > self.saldo or valor <= 0:
            print('Transfarencia é invalida')
            print('-------------------------')
        else:
            self.saldo -= valor
            Conta.saldo += valor
            print(f'Valor de {valor} transferido!')
    
        

conta1 = Conta("Alvaro Lopes Rios", 1234, 4321)
conta1.mostrarInfomacoesConta()
conta1.sacar(50)
conta1.sacar(-2)
conta1.depositar(-50)
conta1.depositar(50)
conta1.mostrarInfomacoesConta()

conta2 = Conta('Ricardo', 1234, 7777)
conta2.mostrarInfomacoesConta()
conta2.transferir(50, conta1)
conta2.transferir(-2, conta1)
conta2.depositar(50)
conta2.mostrarInfomacoesConta()
conta2.transferir(50, conta1)
conta2.mostrarInfomacoesConta()
conta1.mostrarInfomacoesConta()