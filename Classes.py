from __future__ import print_function

class BankAccount:
    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient Funds.')

    def get_balance(self):
        return self.__balance

def main():
    start_bal = float(input("Enter the starting balance: "))
    savings = BankAccount(start_bal)
    pay = float(input("How much were you paid this week?"))
    print("I will deposit that into your account.")
    savings.deposit(pay)
    print("Your account balance is", savings.get_balance())
    cash = float(input("How much would you like to withdraw? "))
    print("I will withdraw that from your account.")
    savings.withdraw(cash)
    print("Your account balance is", savings.get_balance())

main()


import random

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()
    print('This side is up:', my_coin.get_sideup())
    print('I am tossing the coin...')
    my_coin.toss()
    print('This side is up:', my_coin.get_sideup())

main()