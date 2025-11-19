#!/usr/bin/env python3

class Dog:
    def __init__(self, name,breed="Mutt"):
        self.name = name
        self.breed = breed
        
if __name__ == "__main__":
    dog = Dog("Fido")
    print(dog.name)
    print(dog.breed)

dog = Dog("Fido")
dog.name     # "Fido"
dog.breed    # "Mutt"

dog2 = Dog("Snoopy", "Beagle")
dog2.breed   # "Beagle"