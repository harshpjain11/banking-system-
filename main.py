import time

class BankAccount:
    def __init__(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return
        self.balance += amount
        self.history.append(f"Deposited: ₹{amount}")
        print(f"₹{amount} deposited successfully!")

    def withdraw(self, amount):
        if amount > self.balance:
            print(" Insufficient balance!")
        elif amount <= 0:
            print(" Invalid amount!")
        else:
            self.balance -= amount
            self.history.append(f"Withdrawn: ₹{amount}")
            print(f"₹{amount} withdrawn successfully!")

    def check_balance(self):
        print(f" Current Balance: ₹{self.balance}")

    def show_history(self):
        print("\n Transaction History:")
        if not self.history:
            print("No transactions yet.")
        else:
            for i, h in enumerate(self.history, 1):
                print(f"{i}. {h}")


def loading():
    print(" Processing ", end=" ")
     for _ in range(3):
        print(". ", end=" ",flush =True)
        time.sleep(0.5)
     print()


def main():
    print(" Welcome to Python Banking System 🏦")

    name = input("Enter your name: ")
    acc_no = input("Enter account number: ")

    user = BankAccount(name, acc_no)

    while True:
        print("\n===== MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            loading()
            user.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            loading()
            user.withdraw(amount)
        elif choice == '3':
            loading()
            user.check_balance()

        elif choice == '4':
            user.show_history()

        elif choice == '5':
            print(" Thank you for using our banking system!")
            break
        else:
            print(" Invalid choice! Try again.")
if __name__ == "__main__":
    main()
