import random
from sys import exit
import database


def main():
    connection = database.connect()
    database.create_tables(connection)

    while True:
        print("1. Create an account\n"
              "2. Log into account\n"
              "0. Exit")
        choice = int(input())

        if choice == 1:
            create_account(connection)
        elif choice == 2:
            account = log_in(connection)
            if account:
                logged(connection, account)
        elif choice == 0:
            print("Bye!")
            break


def create_account(connection):
    """Create new account and show info about it to the user"""

    card_number = generate_card_num(connection)
    pin = generate_pin()

    # Adding new card to database
    database.add_card(connection, card_number, pin)

    print("\nYour card has been created\n"
          "Your card number:\n"
          f"{card_number}\n"
          "Your card PIN:\n"
          f"{pin}\n")


def generate_card_num(connection):
    """Generate a card number that satisfies given conditions"""

    # Bank Identification Number
    bin_num = "400000"

    while True:
        # Creating Account Identifier number
        random.seed()
        ai_number = "%09d" % random.randint(0, 999999999)

        # Card number
        card_number = bin_num + ai_number
        checksum = luhn(card_number)
        card_number += checksum

        # Checking if it's not in use already
        if not database.check_card(connection, card_number):
            break

    return card_number


def luhn(card_number):
    """Calculates the checksum according to Luhn algorithm"""

    card_number = list(card_number)

    card_number = [int(i) for i in card_number]

    for i in range(len(card_number)):
        if i % 2 == 0:
            card_number[i] = card_number[i] * 2

        if card_number[i] > 9:
            card_number[i] -= 9

    control_num = sum(card_number)

    if control_num % 10 == 0:
        checksum = 0
    else:
        checksum = 10 - (control_num % 10)

    return str(checksum)


def generate_pin():
    """Generate 4 digit PIN"""

    random.seed()
    pin = "%04d" % random.randint(0, 9999)
    return pin


def log_in(connection):
    """Log into the account"""

    card_num = int(input("\nEnter your card number:\n"))
    pin = input("Enter your PIN:\n")

    account = database.log_in(connection, card_num, pin)
    if account:
        print("\nYou have successfully logged in!")
        return account[1]

    print("\nWrong card number or PIN!\n")
    return False


def logged(connection, card_number):
    """Activity when user is logged in"""

    while True:
        print("\n1. Balance\n"
              "2. Log out\n"
              "0. Exit")

        choice = int(input())
        if choice == 1:
            check_balance(connection, card_number)
        elif choice == 2:
            print("\nYou have successfully logged out!")
            break
        elif choice == 0:
            print("\nBye")
            exit(0)


def check_balance(connection, card_number):
    """Check the balance of the account"""

    print("Balance:", database.balance(connection, card_number)[0])


if __name__ == '__main__':
    main()
