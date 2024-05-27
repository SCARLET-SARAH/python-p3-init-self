#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def sit(self):
        print(f"The {self.name} is sitting.")

    def fetch(self, item):
        print(f"{self.name} fetched the {item}.")

fido = Dog("Fido", "Dalmatian", 5)
fido.bark()  # Output: Fido says: Woof!
fido.sit()   # Output: The Fido is sitting.
fido.fetch("ball")  # Output: Fido fetched the ball.