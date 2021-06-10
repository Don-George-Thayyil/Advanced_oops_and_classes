
class IllegalAction(Exception):
    pass

class BankAccount:
    def __init__(self,account_number,balance = 0):
        self.__account_number = account_number
        self.__balance = balance
    @property
    def account_number(self):
        return self.__account_number
    @account_number.setter
    def account_number(self,num):
        raise IllegalAction("Cannot change an account number. Theft alarm!!!")
    @account_number.deleter
    def account_number(self):
        raise IllegalAction("Cannot delete a bank account number!!!")
    
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        if value < 0 :
            raise IllegalAction("Cannot use a negative number")
        if value > 100000:
            print("Some kind of Auditing....")
        self.__balance += value
    @balance.deleter
    def balance(self):
        if self.__balance == 0:
            self.__balance = None
        else:
            raise IllegalAction("Account Balance is not Zero, cannot delete !!!")
    def __str__(self):
        return f"The account number is {self.__account_number}, and the balance is {self.__balance}"
            
# account = BankAccount(12432412343212376543,10000)
# del account.account_number
# account.account_number = 10000000
# account.balance = 50000
# account.balance = 500000000
# account.balance = -23000
# print(account)