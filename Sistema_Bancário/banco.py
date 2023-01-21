import pessoas
import contas

class Banco:
    def __init__(
        self, agencias: list[int] | None = None, 
        clientes: list[pessoas.Pessoa] | None = None, 
        contas: list[contas.Conta] | None = None
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)  # Esses prints colocamos pois o programa estava dando erro e não sabiamos onde era.
            return True
        print('_checa_agencia', False) # Então colocamos cada um com seus respectivos retornos para ver até onde estava indo.
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_conta_cliente(self, cliente, conta):
        if conta is cliente.conta: # Aqui estamos validando se a determinada conta que está sendo checada é daquele cliente. = c1.conta
            print('_checa_conta_cliente', True)
            return True
        print('_checa_conta_cliente', False)
        return False


    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_conta_cliente(cliente, conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name} {attrs}'


if __name__ == '__main__':
    c1 = pessoas.Cliente('Kleyon', 23)
    cc1 = contas.ContaCorrente(111,222,0,0)
    c1.conta = cc1
    c2 = pessoas.Cliente('liandra', 24)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222]) 

    # print(banco.autenticar(c1, cc1)) # Erro pois ele está validando uma conta a um cliente que não a possui.
    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(90) # Um outro método para usar o depósito.
        print(c1.conta)

    print(banco)