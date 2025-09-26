import datetime as dt

class Account:
    def __init__(self, bank, acc_id, holder_id, balance:float=0.0):
        self.bank = bank
        self.acc_id = acc_id
        self.holder_id = holder_id
        self.balance = balance
        self.start_date = dt.datetime.now()

    def deposit(self, amount:float):
        self.balance += amount
        
    def withdraw(self, amount:float):
        self.balance -= amount
        
    @staticmethod
    def bankphone(bank):
        '''
        imprime el número del banco
        '''
        print('1-000-1234567')

    @classmethod
    def quick(cls, string): # escribe tu código aquí
        '''
        crea una cuenta a partir de una cadena
        usando solo las identificaciones de cuenta y titular
        separadas por una barra
        '''
        acc_id, holder_id = string.split("/")
        bank = 'default_bank'
        balance = 0.0 # escribe tu código aquí
        return cls(bank, acc_id, holder_id, balance)# escribe tu código aquí
    
first = Account('old_trusty', '001', '10043', 500) # crea la primera cuenta
first.deposit(250) # llama al método deposit
first.withdraw(400) # llama al método withdraw
print(first.balance) # imprime el saldo

second = Account.quick('002/10123') # crea la segunda cuenta
print(second.start_date.year) # imprime el año