class my_person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f"Name: {self.name} \nAge: {self.age} \nAddress: {self.address} "

    def eat(self):
        print("{} is eating.".format(self.name))

    def sleep(self):
        print("{} is sleeping.".format(self.name))

    def work(self):
        print("{} is working.".format(self.name))

my_person = my_person("Derrick", 25, "Sekidde")
print(my_person)
my_person.eat()
my_person.sleep()
my_person.work()
