#Class named BankAccount with private attribute balance
#Include deposit() and withdraw() methods
#balance cannot be accessed outside class
# encapsulation allows you to restrict access to certain attributes or methods
# within a class.

#Class creation
class BankAccount:
    #Constructor
        def __init__(self, balance):
            #Using Double Underscore Prefix with getter-setter method
            self.__balance = balance

        #Deposit method
        def deposit(self, amount):
            self.__balance += amount
            print(f"You have deposited {amount}\n Balance: {self.__balance}")
            return self

        #Withdraw Method
        def withdraw(self, amount):
            if self.__balance <= amount:
                print("You have insufficient funds.")
                return self.__balance - amount
            else:
                self.__balance -= amount
                return print(f"You have withdrawed {amount}\n Balance: {self.__balance}")
#Instance
Account1=BankAccount(0)
print(Account1.deposit(100))
print(Account1.withdraw(50))