from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.enderco = endereco
        self.contas = []

    def realizar_trasacao(self, conta, transacao):
        transacao.registar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Pessoa_fisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome 
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente ):
        self._saldo = 0
        self._agencia = "0001"
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()
    @classmethod
    def nova_conta(cls, cliente, numero):
         return cls(numero, cliente)
    @property
    def saldo(self):
        return self._saldo
    @property
    def agencia(self):
        return self._agencia
    @property
    def numero(self):
        return self._numero
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
   
    def sacar(self, valor):
        saldo = self.saldo
        if valor > saldo:
            print("Saldo insuficiente!.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!.")
            return True
        else:
            print("Operação falhou, valor informado é inválido!.")
            
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito realizado com sucesso!.")
        else:
            print("Operação falhou, valor informado é inválido!.")
            return False
        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len ([
            transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self.limite:
            print("Operação falhou! O valor do saque excede o limite.")
        if numero_saques >= self.limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            return super().sacar(valor)
        return False
    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
class Historico:
    def __init__(self):
        self._transacoes = []
    @property
    def transacoes(self):
        return self._transacoes
    def adicionar_transacoes(self, transacao):
        self._transacoes.append({"tipo": transacao.__class__.__name__, 
                                 "valor": transacao.valor,
                                 "data":datetime.now().strftime("%d-%m-%Y %H:%M:%s")})
        
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, valor):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    def registar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):

    def __init__(self, valor):
            self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

