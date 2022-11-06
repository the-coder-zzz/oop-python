class Clothes:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Dry:
    
    def set_time(self):
        while True:
            self.time = input('Please select the time (1/2/3) minutes for drying: ')
            if self.time == '1':
                print('Please wait 1 minute till your clothes are dry. Thank you.')
                break
            elif self.time == '2':
                print('Please wait 2 minutes till your clothes are dry. Thank you.')
                break
            elif self.time == '3':
                print('Please wait 3 minutes till your clothes are dry. Thank you.')
                break
            else:
                print('Invalid input')

    def set_spin(self):
        if self.load == 'light':
            print('The spinning pressure is 100.')
        elif self.load == 'mid':
            print('The spinning pressure is 400.')
        else:
            print('The spinning pressure is 800.')
        
   
class Wash:
   
    def set_temp(self):
        while True:
            self.temp = input('What do you want to be the temperture of your water (warm/cold): ').lower()
            if self.temp == 'cold':
                print('Using cold water to wash.')
                break
            elif self.temp == 'warm':
                print('Using warm water to wash.')
                break
            else:
                print('Invalid input.')

    def set_time(self):
        while True:
            self.time = input('Please select the time (10/14/20) minutes for washing: ')
            if self.time == '10':
                print('Please wait 10 minutes till your clothes are washed. Thank you.')
                break
            elif self.time == '14':
                print('Please wait 14 minutes till your clothes are dry. Thank you.')
                break
            elif self.time == '20':
                print('Please wait 20 minutes till your clothes are dry. Thank you.')
                break
            else:
                print('Invalid input')

    def turbo_wash():
        return lambda a : a 

    def easy_care():
        pass



class Washing_Machine(Dry, Wash, Clothes):
    def __init__(self, name, type):
        super().__init__(name, type)
    
    def prepare_clothes(self):
        self.set_temp()
        self.set_time()
        
        

    def add_item(self, cloth):
        self.clothes = []
        self.clothes.append(cloth) 
        print('Added on the washing machine')
       


clothes = Clothes('socks', 'wool')

j = Washing_Machine('shirt', 'cotton')
j.prepare_clothes()
j.add_item(clothes)

# jacket = Clothes('jacket')
# socks = Clothes('socks')
# shirt = Clothes('shirt')
# pants = Clothes('pants')
# undies = Clothes('undies')
# gloves = Clothes('gloves')
# clothes = Washing_Machine('light', 'Cotton', 5)
# clothes.add_item(jacket)
# clothes.add_item(socks)
# clothes.add_item(shirt)
# clothes.add_item(pants)
# clothes.add_item(undies)
# clothes.add_item(gloves)
# clothes.set_time()


