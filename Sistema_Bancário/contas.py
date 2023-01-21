import abc 

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:  # Definimos 0 como valor incial para não ter que ficar mandando essa informação sempre
        self.agencia = agencia
        self.conta = conta  # consigo observar aqui que podemos ter varios selfs
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
        self.saldo
    
    def detalhes(self, msg: str = '') -> None:  # método para dar detalhes sobre o saldo 
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')  # Apenas quebra de linha visual.

    def __repr__(self):  # colocamos ele aqui por conta da herança, uma vez que as classes abaixo herdan dela não temos pq repetir código
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, { self.saldo!r})'
        return f'{class_name} {attrs}'

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_por_saque = self.saldo - valor

        if valor_por_saque >= 0:  # Diferente de conta corrente aqui não queremos que o saldo seja menor que zero
            self.saldo -= valor
            self.detalhes(f'(SAQUE) {valor})')
            return self.saldo
        
        print('Não foi possivel efetuar o saque do valor desejado')
        self.detalhes(F'(SAQUE NEGADO,  {valor})')
        return self.saldo
        


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):  # Ao definirmos o inicio como zero não precisamos ficar mandando o saldo nem o limite durante os testes
        super().__init__(agencia, conta, saldo)
        self.limite = limite  # colocamos aqui pois o limite é algo apenas dessa classe

    def sacar(self, valor: float) -> float:
        valor_por_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_por_saque >= limite_maximo:  # Dessa forma conseguimos fazer com que o programa não ultrapasse o limite estabelecido.
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print('Não foi possivel efetuar o saque do valor desejado')
        print(f'Seu limite é de {-self.limite:.2f}')
        self.detalhes(F'(SAQUE NEGADO,  {valor})')
        return self.saldo

    def __repr__(self):  # Aqui acabamos definindo novamente pois como aqui possui limite, precisamos fazer manualmente o código e definir o limite
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, { self.saldo!r}, '\
            f'{self.limite!r})'  # Como quebramos a linha precisamos por novamente o f de f strings, quebramos a linha por que a mesma passou de 80 caracteres
        return f'{class_name} {attrs}'



if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)  # Aqui não precisamos passar o valor do saldo visto que definimos ele já como zero.
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(111, 22, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
    print('##')