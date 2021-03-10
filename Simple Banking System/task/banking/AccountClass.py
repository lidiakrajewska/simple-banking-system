import random


class Account:
    """This class stores info about users' accounts and create new ones"""
    accounts = {}  # store list of objects not {number : pin}

    def __init__(self):
        self.pin = None
        self.card_number = self.generate_card_num()
        self.balance = 0

    def generate_pin(self):
        """It generates 4 digit PIN"""
        random.seed()
        self.pin = ""
        for _ in range(4):
            n = random.randint(0, 9)
            self.pin += str(n)

    def generate_card_num(self):
        """It generates a card number that satisfies given conditions"""

        while True:
            random.seed()
            number = "400000"
            for _ in range(10):
                n = random.randint(0, 9)
                number += str(n)

            if number not in Account.accounts:  # how to check it in a list?
                self.generate_pin()
                Account.accounts[number] = self.pin
                break

        return int(number)

    def check_balance(self):
        """Checking the balance of the account"""
        print("Balance:", self.balance)
