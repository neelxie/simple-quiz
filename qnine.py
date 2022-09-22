class Cities:
    def __init__(self, name, temp, population, park):
        self.name = name
        self.temp = temp
        self.population = population
        self.park = park
        self.__country = "Uganda"

    def __repr__(self):
        return f"Name: {self.name} \n Temperature: {self.temp} \n Population: {self.population} \
         \n Park: {self.park}"
    #static 
    def area(a, b):
        return a * b
    
#abstraction
    def naming(self):
        print("Cities of {}".format(self.__country))

    def setCountry(self, countryy):
        self.__country = countryy

    def getCountry(self):
        return self.__country
        
    def name_to_initial(self, initial):
        self.name = initial
        print("Initial is created: ")
        return self.name

class Central(Cities):
    def __init__(self, name, temp, population, park):
        super().__init__(name, temp, population, park)
    
    def popun(self):
        print("The central cities are densely populated.")

    def get_name(self):
        return self.name

    def get_detail(self):
        return 0

#Polymorphism
class Kampala(Central):
    def __init__(self, name, temp, population, park, num):
        super().__init__(name, temp, population, park)
        self.num = num

    def get_detail(self):
        return self.num

class Mukono(Central):
    def __init__(self, name, temp, population, park, weather):
        super().__init__(name, temp, population, park)
        self.weather = weather

    def get_detail(self):
        return self.weather

city_name = input("Enter name of city: ")
city_temp = input("Enter temperature of city: ")
city_popn = input("Enter population of city: ")
city_park = input("Enter park name of city: ")        

print("Area is:")
print(Cities.area(9, 98766542))
central = Central(city_name, city_temp, city_popn, city_park)
city = Cities(city_name, city_temp, city_popn, city_park)

print(central) 

initial = central.name_to_initial(input("Enter initials for city: "))
print(initial)


central.setCountry("Ghana")

#inheritance
central.naming() 
central.popun()

#polymorphism
def print_detail(Central):
    print("{}'s details: {}".format(Central.get_name(), Central.get_detail()))

my_kampala = Kampala("Kampala", 20, 200000, "Nakasero", "Nakivubo")
Seeta = Mukono("Mukono", 15, 300000, "Katosi", "Kayunga")

print(my_kampala)
print_detail(my_kampala)

print(Seeta)
print_detail(Seeta)