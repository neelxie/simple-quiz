class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def __repr__(self):
        return f"Name: {self.name} \n Color: {self.color} \n Age: {self.age} "

    def eat(self):
        print("{} is eating.".format(self.name))

    def sleep(self):
        print("{} is sleeping.".format(self.name))

    def make_sound(self):
        print("{} is making a sound".format(self.name))

class my_dog(Animal):
    def __init__(self, name, color, age, breed):
        self.breed = breed
        super().__init__(name, color, age)

    def bark(self):
        print("{} is barking.".format(self.name))

my_dog = my_dog("Puppy", "black", "1 year", "Bull dog")
my_dog.eat()
my_dog.sleep()
my_dog.bark()
my_dog.make_sound()
