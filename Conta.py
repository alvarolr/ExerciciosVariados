class Conta:
    def __init__(self, titular, agencia, conta):
        self.titular = titular
        self.agencia = agencia
        self.conta = conta
        self.saldo = 0
        
    def mostrarInfomacoesConta(self):
        print(f'Nome do titular:{self.titular}')
        print(f'Agencia do Titular:{self.agencia}')
        print(f'Conta do Titular:{self.conta}')
        print(f'Saldo do titular:{self.saldo}')
        print('-----------------------------------')
        
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
            
    
    def transferir():
        pass
    
        

conta1 = Conta("Alvaro Lopes Rios", 1234, 4321)
conta1.mostrarInfomacoesConta()
conta1.sacar(50)
conta1.sacar(-2)
conta1.depositar(-50)
conta1.depositar(50)
conta1.mostrarInfomacoesConta()
