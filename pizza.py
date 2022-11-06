class Pizza:
    def __init__(self):
        self.toppings = []

    def view_toppings(self):
        print('The toppings are: ')
        for i in self.toppings:
            print(i)

class Pineapple:
    def add_pineapple(self):
        print('Adding pineapple!')
        self.toppings += ['pineapple']

class Pepperoni:
    def add_pepperoni(self):
        print('Adding pepperoni!')
        self.toppings += ['pepperoni']

class Olives:
    def add_olives(self):
        print('Adding olives!')
        self.toppings += ['olives']

class MothersPizza(Pineapple, Olives, Pizza):
    def prepare_pizza(self):
        self.add_pineapple()
        self.add_olives()

class MyPizza(Pepperoni, Pizza):
    def prepare_pizza(self):
        self.add_pepperoni()

class DadsPizza(MothersPizza, MyPizza):
    def prepare_pizza(self):
        return MothersPizza.prepare_pizza(self) or MyPizza.prepare_pizza(self)


# p = MothersPizza()
# p.prepare_pizza()

# p2 = MyPizza()
# p2.prepare_pizza()

slices = lambda s : s*2

p3 = DadsPizza()
p3.prepare_pizza()
p3.view_toppings()
print(slices(4))




