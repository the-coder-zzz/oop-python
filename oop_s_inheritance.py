#single inheritance

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print("\n-Personal Details-\n")
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f'Hi {self.name}, your account has now: ${self.balance}')

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print('Insufficient Funds | Your balance is: $', self.balance)
        else:
            self.balance = self.balance - self.amount
            print(f'Hi {self.name}, your account has currently ${self.balance} balance')
            if self.balance == 0:
                print(f"Hi {self.name}, your balance is now $0. Goodbye!")
                quit()

    def view_balance(self):
        self.show_user_details()
        print('Balance is: $', self.balance)

missy = Bank('Missy', 20, 'Female')
# missy.deposit(500)
# missy.deposit(200)
# missy.withdraw(300)
# missy.withdraw(400)
missy.deposit(300)
missy.withdraw(100)
missy.view_balance()

reji = Bank('Reji', 23, 'Male')
reji.deposit(500)
reji.withdraw(200)
reji.view_balance()

