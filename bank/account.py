# bank/account.py — skeleton 
class BankAccount: 
    bank_name = "PyBank"      # class attribute: shared by all objects 
    MIN_BALANCE = 0.0 

    def __init__(self, owner: str, balance: float = 0.0) -> None: 
        self.owner = owner                # instance attribute 
        self.balance = balance            # instance attribute 
        self.transactions = []            # each object needs its OWN list 
        # TODO: raise ValueError if balance < MIN_BALANCE 
        try:
            if balance < BankAccount.MIN_BALANCE:
                raise ValueError("Balance should be higher than minimum possible balance.")
        except ValueError as e:
            print("Error is: ", e)

    def deposit(self, amount: float) -> float:
        # TODO: add amount to self.balance, record it, return the new balance
        self.balance += amount
        self.transactions.append(("deposit", amount, self.balance))
        return self.balance

    def withdraw(self, amount: float) -> float:
        if self.balance-amount<BankAccount.MIN_BALANCE:
            raise ValueError("You are crossing minimun balance limit, please try again.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        self.balance-=amount
        self.transactions.append(("withdraw", amount, self.balance))
        return self.balance

    def summary(self) -> None:
        return f"{self.owner} · {self.balance:,.2f}"

    def transfer_to(self, other, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")
        if self.balance-amount<BankAccount.MIN_BALANCE:
            raise ValueError("You are crossing minimun balance limit, please try again.")
        self.withdraw(amount)
        other.deposit(amount)
