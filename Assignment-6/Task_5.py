class BankAccount:
    """
    A simple class to represent a bank account with basic deposit and withdrawal functionality.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount with an optional starting balance.

        :param initial_balance: The starting amount in the account (float).
        """
        # The balance attribute is where the account's state (money) is stored.
        self.balance = initial_balance
        print(f"Account created with initial balance: ${self.balance:.2f}")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        :param amount: The amount to be added (float).
        :return: A status message (str).
        """
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. New balance: ${self.balance:.2f}"
        else:
            return "Error: Deposit amount must be positive."

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        :param amount: The amount to be withdrawn (float).
        :return: A status message (str).
        """
        if amount <= 0:
            return "Error: Withdrawal amount must be positive."
        elif amount > self.balance:
            return f"Transaction failed. Insufficient funds. Current balance: ${self.balance:.2f}"
        else:
            self.balance -= amount
            return f"Withdrawal successful. New balance: ${self.balance:.2f}"

    def get_balance(self):
        """
        Returns the current balance of the account.

        :return: The current balance (float).
        """
        return f"Current Balance: ${self.balance:.2f}"

# --- Example Usage ---

# 1. Create an account
my_account = BankAccount(initial_balance=100.00)
print("-" * 30)

# 2. Deposit funds
print(my_account.deposit(50.25))
print(my_account.get_balance())
print("-" * 30)

# 3. Withdraw funds successfully
print(my_account.withdraw(75.50))
print(my_account.get_balance())
print("-" * 30)

# 4. Attempt to withdraw more than the balance (insufficient funds)
print(my_account.withdraw(200.00))
print(my_account.get_balance())
print("-" * 30)

# 5. Attempt invalid operations
print(my_account.deposit(-10.00))
print(my_account.withdraw(0.00))