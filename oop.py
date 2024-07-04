class Bird():
    # class object attribute
    has_wings = True

    def __init__(self, breed) -> None:
        self.breed = breed

    def fly(self, name):
        print(f"{name}, a {self.breed}, is flying!")

my_bird = Bird(breed='Parakeet')
print(my_bird.breed)
my_bird.fly("Tombik")