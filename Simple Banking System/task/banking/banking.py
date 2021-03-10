from AccountClass import Account
from sys import exit


def main():
    while True:
        choice = options()

        if choice == 1:
            create_account()
        elif choice == 2:
            log_in()
        elif choice == 0:
            print("Bye!")
            break


def options():
    print("""1. Create an account
    2. Log into account
    0. Exit""")
    return int(input())


def create_account():
    account = Account()
    print(f"""Your card has been created
    Your card number:\n{account.card_number}
    Your card PIN:\n{account.pin}""")


def log_in():
    card_num = input("Enter your card number:\n")
    pin = input("Enter your PIN:\n")

    if card_num in Account.accounts and pin == Account.accounts[card_num]:
        print("You have successfully logged in!")

        while True:
            print("""1. Balance
            2. Log out
            0. Exit""")

            choice = int(input())
            if choice == 1:
                pass
            elif choice == 2:
                print("You have successfully logged out!")
                break
            elif choice == 0:
                print("Bye")
                exit(0)
    else:
        print("Wrong card number or PIN!")


if __name__ == '__main__':
    main()
