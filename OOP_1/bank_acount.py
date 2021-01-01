class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'
        # print(f"Account owner: {self.owner}")    # print(f"Account balance: ${self.balance}")
    def deposit(self, depos):
        self.balance += depos
        print('Deposit Accepted')

    def withdraw(self, wdraw):
        if self.balance >= wdraw:
            self.balance -= wdraw
            print('Withdraw Accepted')
        else:
            print('Funds Unavaiable!')

acc1 = Account("Gio", 400)
