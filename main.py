import time

class BankAccount:
    def __init__(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no
        self.balance = 0
        self.history = []
        self.transactions = []   # used for ML-like analysis

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
            return
        self.balance += amount
        self.history.append(f"Deposited ₹{amount}")
        self.transactions.append(amount)
        print(f"₹{amount} has been added to your account.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.detect_unusual_transaction(amount)  # ML feature
            self.balance -= amount
            self.history.append(f"Withdrawn ₹{amount}")
            self.transactions.append(amount)
            print(f"₹{amount} has been withdrawn.")

    def detect_unusual_transaction(self, amount):
        # Simple anomaly detection using average
        if len(self.transactions) < 3:
            return  # not enough data yet

        avg = sum(self.transactions) / len(self.transactions)

        if amount > 2 * avg:
            print("Note: This transaction seems unusually high compared to your past activity.")

    def check_balance(self):
        print(f"Your current balance is ₹{self.balance}")

    def show_history(self):
        print("\nTransaction History:")
        if not self.history:
            print("No transactions yet.")
        else:
            for i, record in enumerate(self.history, 1):
                print(f"{i}. {record}")


def loading():
    print("Processing", end=" ")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()


def main():
    print("Welcome to the Python Banking System")

    name = input("Enter your name: ")
    acc_no = input("Enter your account number: ")

    user = BankAccount(name, acc_no)

    while True:
        print("\n===== MENU =====")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

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
            print("Thank you for using the banking system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
