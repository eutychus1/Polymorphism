# -------------------------
# Assignment 1: Superhero Class 🦸
# -------------------------

class Hero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
    
    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Subclass (child class)
class Superhero(Hero):
    def __init__(self, name, power, city, weapon):
        super().__init__(name, power, city)  # Call parent constructor
        self.weapon = weapon

    # Polymorphism: redefine use_power()
    def use_power(self):
        return f"{self.name} channels their {self.power} with a {self.weapon}!"

class Villain(Hero):
    def __init__(self, name, power, city, evil_plan):
        super().__init__(name, power, city)
        self.evil_plan = evil_plan

    def use_power(self):
        return f"{self.name} unleashes {self.power} to execute {self.evil_plan}!"


# -------------------------
# Activity 2: Polymorphism Challenge 🎭
# -------------------------

class Animal:
    def move(self):
        return "This animal moves in its own way."

class Dog(Animal):
    def move(self):
        return "The dog runs 🐕."

class Bird(Animal):
    def move(self):
        return "The bird flies 🐦."

class Fish(Animal):
    def move(self):
        return "The fish swims 🐟."

# Vehicles example too
class Vehicle:
    def move(self):
        return "This vehicle moves somehow."

class Car(Vehicle):
    def move(self):
        return "The car drives 🚗."

class Plane(Vehicle):
    def move(self):
        return "The plane flies ✈️."

class Boat(Vehicle):
    def move(self):
        return "The boat sails 🚤."


# -------------------------
# DEMONSTRATION
# -------------------------

if __name__ == "__main__":
    # Assignment 1 demo
    hero1 = Superhero("StarBlade", "light manipulation", "Neo City", "crystal sword")
    villain1 = Villain("DarkStorm", "shadow control", "Neo City", "eternal darkness")

    print("=== Superhero Program ===")
    print(hero1.introduce())
    print(hero1.use_power())
    print(villain1.introduce())
    print(villain1.use_power())

    # Activity 2 demo
    print("\n=== Polymorphism Challenge ===")
    animals = [Dog(), Bird(), Fish()]
    for animal in animals:
        print(animal.move())

    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        print(vehicle.move())
