from AccountClass import Account
from sys import exit


def main():
    while True:
        choice = options()

        if choice == 1:
            create_account()
        elif choice == 2:
            account = log_in()
            if account:
                logged(account)
        elif choice == 0:
            print("Bye!")
            break


def options():
    """Print options available to the logged out user"""

    print("1. Create an account\n"
          "2. Log into account\n"
          "0. Exit")
    choice = int(input())
    return choice


def create_account():
    """Create new account and show info about it to the user"""

    account = Account()
    print("\nYour card has been created\n"
          "Your card number:\n"
          f"{account.card_number}\n"
          "Your card PIN:\n"
          f"{account.pin}\n")


def log_in():
    """Log into the account"""

    card_num = int(input("\nEnter your card number:\n"))
    pin = input("Enter your PIN:\n")

    for account in Account.accounts:
        print(account.card_number)
        if account.card_number == card_num and account.pin == pin:
            print("\nYou have successfully logged in!")
            return account

    print("\nWrong card number or PIN!\n")
    return False


def logged(account):
    """Activity when user is logged in"""

    while True:
        print("\n1. Balance\n"
              "2. Log out\n"
              "0. Exit")

        choice = int(input())
        if choice == 1:
            print("\nBalance:", account.balance)
        elif choice == 2:
            print("\nYou have successfully logged out!")
            break
        elif choice == 0:
            print("\nBye")
            exit(0)


if __name__ == '__main__':
    main()
