class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        print("\n-Personal Details-\n")
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')

class Athlete(Person):
    def __init__(self, name, age, gender, sport, coach):
        super().__init__(name, age, gender)
        self.sport = sport
        self.coach = coach

    def get_sport(self):
        print('The sport is:', self.sport)


class Subject:
    def __init__(self, namesub, grade):
        self.namesub = namesub
        self.grade = grade

    def get_grade(self):
        return self.grade

class Student(Person):
    def __init__(self, name, age, gender, max_sub):
        super().__init__(name, age, gender)
        self.max_sub = max_sub
        self.subjects = []

    def add_sub(self, subject):
        if len(self.subjects) < self.max_sub:
            self.subjects.append(subject)
        else:
            print('You passed the maximum number of subject in a student.')

    def get_ave_grade(self):
        value = 0
        for subject in self.subjects:
            value += subject.get_grade()
        return value / len(self.subjects)

p = Athlete('Fatima', 20, 'female', 'tennis', 'coach mike')
p.get_details()
p.get_sport()



sub1 = Subject('AdvComProg', 90)
sub2 = Subject('Physics', 100)
sub3 = Subject('Litr', 80)

stud = Student('Missy', 20, 'female', 3)
stud.add_sub(sub1)
stud.add_sub(sub2)
stud.add_sub(sub3)
stud.get_details()
# stud.get_sport()
print(stud.get_ave_grade())