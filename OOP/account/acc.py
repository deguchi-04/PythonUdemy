class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance -amount
    
    def deposit(self, amount):
        self.balance = self.balance +amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This is a example class"""
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

if __name__ == "__main__":
    jacks_check = Checking("OOP/account/jack_balance.txt",1)
    jacks_check.transfer(100)
    jacks_check.commit()
    print(jacks_check.balance)
    print(jacks_check.type)

    john_check = Checking("OOP/account/john_balance.txt",1)
    john_check.transfer(100)
    john_check.commit()
    print(john_check.balance)
    print(jacks_check.type)

    print(jacks_check.__doc__)
    # acc = Account("OOP/account/balance.txt")
    # print(acc.balance)
    # acc.withdraw(100)
    # print(acc.balance)
    # acc.commit()