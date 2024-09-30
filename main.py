from datetime import datetime
from typing import List
from abc import ABC, abstractclassmethod, abstractproperty


## Classes

class Client:
    def __init__(self, address):
        self.address = address,
        self.accounts = List[Account] = []
        
    def perform_transaction(self, account, transaction):
        transaction.register(account)
    
    def add_account(self, account):
        self.accounts.append(account)

class IndividualAccount(Client):
    def __init__(self, cpf, name, address, birthday):
        super().__init__(address)
        self.cpf = cpf
        self.name = name
        self.birthday = birthday

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
    
    @property
    def client(self):
        return self._client
    
    @property
    def history(self):
        return self._history
    
    @classmethod
    def new_account(cls, client, number):
        return cls(number, client)
    
    def withdraw(self, value):
        value_entered = float(value.replace(",", "."))

        balance = self.balance
        balance_exceeded = value > balance

        if value_entered > 0:
            if not balance_exceeded:
                self._balance -= value_entered
                print(divisor)
                print(f'O valor de R${value} foi sacado')
                print(divisor)
            elif balance_exceeded:
                print(divisor)
                print("O valor que inserido para saque é maior do que o saldo disponível.")
                print(divisor)
        elif value_entered < 0:
            print(divisor)
            print("O valor inserido para saque é inválido.")
            print(divisor)
            
        return False
            
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
            return False
        
        return True
    
class CurrentAccount(Account):
    def __init__(self, number, client, limit=500, withdrawal_limit=3):
        super().__init__(number, client)
        self.limit = limit
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, value):
        withdraw_number = len([transaction for transaction in self._history.transactions if transaction["type"] == Withdraw.__name__])
        
        withdraw_exceeded = withdraw_number > self.withdrawal_limit
        limit_exceeded = value > self.limit
        
        if withdraw_exceeded:
            print(divisor)
            print("O limite de saque foi excedido.")
            print(divisor)
        
        if limit_exceeded:
            print(divisor)
            print("O valor limite de saque foi excedido.")
            print(divisor)
            
        if not limit_exceeded and not withdraw_exceeded:
            super().withdraw(value)
            
        return False
            
    def __str__(self):
        return(f"""
               Agência: {self.branch}
               Conta: {self.number}
               Conta: {self.client.name}
               """)

class History:
    def __init__(self):
        self._transactions: List[Transaction] = []
        
    @property
    def transactions(self):
        return self._transactions
    
    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            }
        )
        
class Transaction(ABC):
    @property
    @abstractproperty
    def value(self):
        pass
    
    @abstractclassmethod
    def register(self, account):
        pass

class Withdraw(Transaction):
    def __init__(self, value):
        self._value = value
        
    @property
    def value(self):
        return self._value
    
    def register(self, account):
        transaction_success = account.withdraw(self.value)
        
        if transaction_success:
            account.history.add_transaction(self)

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value
        
    @property
    def value(self):
        return self._value
    
    def register(self, account):
        transaction_success = account.deposit(self.value)
        
        if transaction_success:
            account.history.add_transaction(self)