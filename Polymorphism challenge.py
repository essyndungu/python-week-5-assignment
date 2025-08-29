class Animal:
    def move(self):
        print("This animal moves somehow...")

class Kangaroo(Animal):
    def move(self):
        print("Kangaroo is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")


# Demonstrating Polymorphism
animals = [Kangaroo(), Bird(), Fish()]

for animal in animals:
    animal.move()

