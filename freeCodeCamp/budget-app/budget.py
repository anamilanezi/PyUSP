class Category:

    def __init__(self, category_name):
        self.category = category_name.title()
        self.ledger = []
        self.funds = self.get_balance()

    def transaction(self, amount, description=""):
        transaction = {"amount": amount, "description": description}
        self.ledger.append(transaction)
        #print(f"New transaction from {self.category}: {transaction}")

    def deposit(self, amount, description=""):
        self.transaction(amount, description)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.transaction(-amount, description)
            return True
        else:
            # print(f"Insufficient funds from {self.category}.")
            # print(f"Current funds: {self.get_balance()}, withdraw attempt: {amount}")
            return False

    def get_balance(self):
        funds = 0
        for register in self.ledger:
            funds += register["amount"]
        #print(f"Current funds: {funds}")
        return funds

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def transfer(self, amount, other_category):
        msg_withdraw = f"Transfer to {other_category.category}"
        if self.withdraw(amount, msg_withdraw):
            msg_deposit = f"Transfer from {self.category}"
            other_category.transaction(amount, msg_deposit)
            return True
        else:
            return False

    def __str__(self):
        text = ""
        text += f"{self.category:*^30}\n"
        for register in self.ledger:
            description = register["description"][:23]
            value = register["amount"]
            text += f"{description:<23}{value:>7.2f}\n"
        text += f"Total: {self.get_balance():.2f}"
        return text



def create_spend_chart(categories):
    pass