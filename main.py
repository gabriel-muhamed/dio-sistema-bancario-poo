import random
from datetime import date

divisor = "============================="

home_menu = """
=============================

[e] Entrar
[c] Cadastrar

=============================

=> """

login_cpf_menu = """
=============================

Insira o CPF para entrar!

=============================

=> """

options_menu = """
=============================

[d] Depósito
[s] Sacar
[e] Extrato
[q] Sair

=============================

=> """

## Classes

class Account:
    def __init__(self):
        self._balance = 0.00
        self._number = 0
        self._branch = "0001"
        self._client = Client()
        self._history = History()

    @property
    def balance(self):
        return self._balance
    
    @property
    def number(self):
        return self._number
    
    @property
    def branch(self):
        return self._branch
    
    @classmethod
    def new_account(cls, client, number):
        return cls(number, client)
    
    def withdraw(self, value):
        value_entered = float(value.replace(",", "."))

        if value_entered > 0:
            if self._balance >= value_entered:
                self._balance -= value_entered
                print(divisor)
                print(f'O valor de R${value} foi sacado')
                print(divisor)
            elif self._balance < value_entered:
                print(divisor)
                print("O valor que inserido para saque é maior do que o saldo disponível.")
                print(divisor)
        elif value_entered < 0:
            print(divisor)
            print("O valor que inserido para saque é inválido.")
            print(divisor)
            
    def deposit(self, value):
        value_entered = float(value.replace(",", "."))

        if value_entered > 0:
            self._balance += value_entered
            print(divisor)
            print(f'O valor de R${value} foi depositado')
            print(divisor)
        elif value_entered < 0:
            print(divisor)
            print("O valor que inserido para depósito é inválido.")
            print(divisor)

class CurrentAccount(Account):
    def __init__(self):
        self._limit = 0.00
        self._withdrawal_limit = 3

class Client:
    pass

class History:
    pass

class Transaction:
    pass

class IndividualAccount(Client):
    pass

user = Account()

while True:
    options = input(options_menu)
    # Deposit
    if options ==  'd':
        deposit_value = input("Insira o valor que deseja depositar => ")
        user.deposit(deposit_value)
    elif options == 's':
        withdraw_value = input("Insira o valor de saque => ")
        user.withdraw(withdraw_value)
    else:
        print("Comando não identificado")     