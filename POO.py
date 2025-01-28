class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque de {self.nome}.")

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f"{quantidade} unidades removidas do estoque de {self.nome}.")
        else:
            print(f"Estoque insuficiente para remover {quantidade} unidades de {self.nome}.")

    def exibir_detalhes(self):
        print(f"Produto: {self.nome}\nPreço: R${self.preco:.2f}\nEstoque: {self.quantidade} unidades")

# Criando objetos
produto1 = Produto("Arroz", 5.50, 100)
produto2 = Produto("Feijão", 7.20, 50)

# Testando os métodos
produto1.adicionar_estoque(20)
produto1.remover_estoque(50)
produto1.exibir_detalhes()

produto2.remover_estoque(60)
produto2.adicionar_estoque(10)
produto2.exibir_detalhes()





class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"Item '{item}' adicionado ao pedido {self.numero}.")

    def exibir_pedido(self):
        print(f"Pedido Número: {self.numero}")
        print(f"Cliente: {self.cliente}")
        print("Itens do Pedido:")
        for item in self.itens:
            print(f"- {item}")

# Criando um pedido
pedido1 = Pedido(101, "João Silva")

# Adicionando itens ao pedido
pedido1.adicionar_item("Arroz")
pedido1.adicionar_item("Feijão")
pedido1.adicionar_item("Macarrão")

# Exibindo os detalhes do pedido
pedido1.exibir_pedido()







class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, quantidade_portas):
        super().__init__(marca, modelo, ano)
        self.quantidade_portas = quantidade_portas

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Portas: {self.quantidade_portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_motor):
        super().__init__(marca, modelo, ano)
        self.tipo_motor = tipo_motor

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Tipo do Motor: {self.tipo_motor}")

# Criando objetos
carro = Carro("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "MT-07", 2019, "2 cilindros")

# Exibindo detalhes
carro.exibir_detalhes()
print()
moto.exibir_detalhes()







class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

class ContaCorrente(Conta):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente, mesmo considerando o limite.")

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, juros_mensais):
        super().__init__(titular, saldo)
        self.juros_mensais = juros_mensais

    def render_juros(self):
        self.saldo += self.saldo * (self.juros_mensais / 100)
        print(f"Juros aplicados. Saldo atual: R${self.saldo:.2f}")

# Criando contas
cc = ContaCorrente("João", 1000, 500)
cp = ContaPoupanca("Maria", 2000, 1)

# Testando as contas
cc.depositar(200)
cc.sacar(1500)
cc.sacar(2000)

cp.render_juros()
cp.sacar(500)









class Pagamento:
    def processar(self):
        print("Processando pagamento genérico.")

class CartaoCredito(Pagamento):
    def processar(self):
        print("Pagamento realizado no cartão de crédito.")

class Pix(Pagamento):
    def processar(self):
        print("Pagamento realizado via Pix.")

# Criando objetos
pagamento1 = Pagamento()
pagamento2 = CartaoCredito()
pagamento3 = Pix()

# Processando pagamentos
pagamento1.processar()
pagamento2.processar()
pagamento3.processar()








class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def fazer_som(self):
        print(f"{self.nome} faz: {self.som}")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Au Au")

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Miau")

class Passaro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Piu Piu")

# Criando objetos
cachorro = Cachorro("Rex")
gato = Gato("Mimi")
passaro = Passaro("Piu")

# Fazendo os sons
cachorro.fazer_som()
gato.fazer_som()
passaro.fazer_som()

