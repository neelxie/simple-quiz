class Animal:
    def _init_(self,name):
        self.name = name
#inheritance
class Dog(Animal):
    def _init_(self,name):
        super()._init_(name)

    def bark(self):
      return print("bow wow wow")

my_dog = Dog("Puppy")
my_dog.bark();