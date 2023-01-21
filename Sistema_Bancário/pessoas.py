import contas

class Pessoa:
    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name
    
    @property
    def name(self):
       return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name

   
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name} {attrs}'


class Cliente(Pessoa):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.conta: contas.Conta | None = None  # Dessa forma estamos falando que a conta para a class cliente é opcional.


if __name__ == '__main__':
    # import contas  # Aqui não podemos pois irá ocasionar um erro por que lá em Cliente a conta está retornando none, então precisamos
    c1 = Cliente('Kleyon', 23)  # importar lá em cima para que a classe cliente tenha acesso a essa importação   - AULA 262
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Liandra', 24)
    c2.conta = contas.ContaPoupanca(112, 234, 100) 
    print(c2)
    print(c2.conta)