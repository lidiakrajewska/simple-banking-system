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
        pin = "%04d" % random.randint(0, 9999)
        return pin

    def generate_card_num(self):
        """Generate a card number that satisfies given conditions"""

        # Bank Identification Number
        bin_num = "400000"

        while True:
            # Creating Account Identifier number
            random.seed()
            ai_number = "%09d" % random.randint(0, 999999999)

            # Card number
            card_number = bin_num + ai_number
            checksum = self.__luhn(card_number)
            card_number += checksum

            # Checking if it's not in use already
            card_number = int(card_number)
            for account in Account.accounts:
                if account.card_number == card_number:
                    break
            else:
                break

        return card_number

    def check_balance(self):
        """Check the balance of the account"""

        print("Balance:", self.balance)

    def __luhn(self, card_number):
        """Calculates the checksum according to Luhn algorithm"""

        card_number = list(card_number)

        card_number = [int(i) for i in card_number]

        for i in range(len(card_number)):
            if i % 2 == 0:
                card_number[i] = card_number[i] * 2

            if card_number[i] > 9:
                card_number[i] -= 9

        control_num = sum(card_number)

        checksum = 10 - (control_num % 10)

        return str(checksum)
