class Account:
    num_account0 = 0
    num_account1 = 0
    def __init__(self, name):
        self.name = name
        Account.num_account0 += 1
        self.num_account1 += 1
    def __del__(self):
        Account.num_account0 -= 1
        self.num_account1 -= 1

kim = Account("kim")
lee = Account("lee")

kim.name

lee.name
