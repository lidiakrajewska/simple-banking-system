import random


class Account:
    """This class stores info about users' accounts and create new ones"""
    accounts = []

    def __init__(self):
        self.card_number = self.generate_card_num()
        self.pin = self.generate_pin()
        self.balance = 0
        Account.accounts.append(self)

    def generate_pin(self):
        """Generate 4 digit PIN"""
        random.seed()
        pin = ""
        for _ in range(4):
            n = random.randint(0, 9)
            pin += str(n)
        return pin

    def generate_card_num(self):
        """Generate a card number that satisfies given conditions"""

        while True:
            random.seed()
            number = "400000"
            for _ in range(10):
                number += str(random.randint(0, 9))

            for account in Account.accounts:
                if account.card_number == number:
                    break
            else:
                break

        return number

    def check_balance(self):
        """Check the balance of the account"""

        print("Balance:", self.balance)
