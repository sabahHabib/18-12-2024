class Dog:
    species ="Canine"
    def __init__(self,name,age):
        self.name=name
        self.age=age
dog1 = Dog("Bob", 3)
dog2 = Dog("buddy", 4)

print(dog1.name)
print(dog2.name)
print(dog1.species)

class Person:
    def __init__(self,name,gender,profession):
        self.name=name
        self.gender=gender
        self.profession=profession
    def show(self):
        print("Name:",self.name,"Gender:",self.gender,"Profession:",self.profession)
    def work(self):
        print(self.name,"Working as a",self.profession)

person1=Person("Emma","Female","Doctor")
person1.show()
person1.work()


class Vehicle:
    def __init__(self,engine):
        print("inside vehicle constructor")
        self.engine=engine
class Car (Vehicle):
    def __init__(self,engine,max_speed):
        super().__init__(engine)
        print("inside Car constructor")
        self.max_speed=max_speed

class Electric_Car(Car):
    def __init__(self,engine,max_speed,km_range):
        super().__init__(engine,max_speed)
        print("inside Electric Car constructor")
        self.km_range=km_range

ev=Electric_Car("1500 CC",200,740)
print(f"Engine={ev.engine} Max_Speed={ev.max_speed} Range={ev.km_range}")


class Employee:
    count = 0
    def __init__(self):
        Employee.count =Employee.count+1

e1=Employee()
e2=Employee()
e3=Employee()
print("number of employee is:",Employee.count)

class SoftwareEngineer:
    #class attribute
    alice="Keyboard Magician"
    #instance attribute
    def __init__(self,name,age,experience,salary):
        self.name=name
        self.age=age
        self.experience=experience
        self.salary=salary
s1=SoftwareEngineer("max",35,10,10000)
print(s1.name)

