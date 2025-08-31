
# -----------------------------
# Base classes are not required here,
# but we create an Animal and Vehicle parent for
 clarity.
# -----------------------------

class Animal:
    """General Animal template. Specific animals will override move()."""
    def move(self):
        raise NotImplementedError("Animals must define how they move!")


class Vehicle:
    """General Vehicle template. Specific vehicles will override move()."""
    def move(self):
        raise NotImplementedError("Vehicles must define how they move!")


# -----------------------------
# Specific Animals
# -----------------------------
class Elephant(Animal):
    def move(self):
        print("🐘 The elephant walks slowly but powerfully.")

class Cat (Animal):
    def move (self):
         print("Cat walks slowly.")

class Fish(Animal):
    def move(self):
        print("🐟 The fish swims gracefully in water.")


# Specific Vehicles
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving smoothly on the road.")


class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying high in the sky.")


# -----------------------------
# Main Demo of Polymorphism
# -----------------------------
if __name__ == "__main__":
    # A collection of mixed objects (animals + vehicles).
    movers = [Elephant(), Fish(), Car(), Plane()]

    print("=== Demonstrating Polymorphism: Different move() behaviors ===\n")
    
    for thing in movers:
        # Notice: We don’t care *what* the object is.
        # As long as it has a .move(), we can call it.
        thing.move()
