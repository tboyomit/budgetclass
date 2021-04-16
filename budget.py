class Budget:
    def __init__(self, category):
        self.category = category
        self.register = list([])
        self.balance = 0

    def deposit(self, amount, purpose):
        self.register.append([amount, purpose])
        self.balance += amount
        return self.balance

    def balance(self):
        sumt = 0
        for item in self.register:
            sumt += item[0]
        return sumt

    def withdrawal(self, amount, purpose):
        if amount > self.balance:
            return False
        self.balance -= amount

    def transfer(self, deduc, dest_category):
        self.deduc = deduc
        self.balance -= deduc
        if self.balance > deduc:
            result = dest_category.deposit(deduc)
            print("You have transferred {}".format(deduc))
        else:
            print("Insufficient balance for transfer operation")
        return result

    


