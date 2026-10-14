from bank.account import BankAccount

obj1=BankAccount("Steve", 3000)
obj2=BankAccount("Joe", 8000)
obj3= BankAccount("Kane", 5000)
print(obj1.deposit(500))
print(obj1.deposit(1000))

print(obj1.summary())
print(obj1.withdraw(4000))
#print(obj1.withdraw(600))
obj1.transfer_to(obj2, 400)

print(obj1.summary())
print(obj2.summary())
