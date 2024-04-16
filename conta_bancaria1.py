#objeto é uma única coleção de dados(atributos) e comportamentos (métodos)
class ContaBancaria:
    #atributos são variaveis internas dentro do objeto
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    #métodos são funções dentro do objeto que produzem algum comportamento
    def depositar(self,valor):
        self.saldo += valor  

    def exibir_detalhes(self):
        print("Número da Conta", self.numero)
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)
    
    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente, você está miserável")

def exibir_menu():
    print("/nMENU:")
    print("1 - Exibir detalhes da conta")
    print("2 - Realizar Depósito")
    print("3 - Realizar Saque")
    print("4 - Sair do Programa")



#aqui estou criando um instância do objeto ContaBancaria
#com o nome conta_da_maki
numero_conta = input("Digite o número da conta")
titular_conta = input("Digite o titular da conta")
saldo_inicial = float (input("Digite o saldo inicial da conta").replace(",","."))

conta_do_usuario = ContaBancaria(numero_conta, titular_conta, saldo_inicial)

opcao = None

while opcao != 0:
    exibir_menu()
    opcao = int(input("Digite o número da opção desejada:"))

    if opcao == 1:
        conta_do_usuario.exibir_detalhes()
    elif opcao == 2:
        valor_deposito = float(input("Digite o valor a ser depositado").replace(",","."))
        conta_do_usuario.depositar(7000)
    elif opcao == 3:
        valor_saque = float (input("Digite o valor a ser sacado").replace(",","."))
        conta_do_usuario.sacar(7200)






 