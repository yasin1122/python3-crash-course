class Bird():
    def __init__(self, breed) -> None:
        self.breed = breed

my_bird = Bird(breed='Parakeet')
print(my_bird.breed)