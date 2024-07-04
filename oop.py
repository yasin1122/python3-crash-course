class Animal():

    def __init__(self) -> None:
        print("Animal Created")
    
    def eat(self):
        print("I am eating!")


class Bird(Animal):
    # class object attribute
    wings = 2

    def __init__(self, breed='unidentified') -> None:
        Animal.__init__(self)
        self.breed = breed

    def fly(self, name):
        print(f"{name}, a {self.breed}," + 
              " is flying with its {Bird.wings} wings.")

my_bird = Bird(breed='Parakeet')
print(my_bird.breed)
my_bird.fly("Tombik")
my_bird.eat()