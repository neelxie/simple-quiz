class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name} \n Age: {self.age} \n Salary: {self.salary}"

    def eat(self):
        print("{} is eating".format(self.name))

    def sleep(self):
        print("{} is sleeping.".format(self.name))

    def work(self):
        print("{} is working.".format(self.name))

class Programmer(Employee):
    def __init__(self, name, age, salary, programming_language):
        self.programming_language = programming_language
        super().__init__(name, age, salary)

    def code(self):
        print("{} is writing code in {}".format(self.name, self.programming_language))

my_programmer = Programmer("Derrick", 25, 99999999, "Javascript")
my_programmer.eat()
my_programmer.sleep()
my_programmer.work()
my_programmer.code()