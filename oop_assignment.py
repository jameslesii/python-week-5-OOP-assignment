# First, let's design a Superhero class with encapsulation and a constructor to initialize unique values
class Superhero:
    def __init__(self, name, power, weakness):
        self._name = name
        self._power = power
        self._weakness = weakness

    # Encapsulated attributes (private) can be accessed using getter methods
    def get_name(self):
        return self._name

    def get_power(self):
        return self._power

    def get_weakness(self):
        return self._weakness

    # Method to showcase the superhero's power
    def showcase_power(self):
        print(f"{self.get_name()} is using their {self.get_power()} power!")

    # Method to display the superhero's weakness (we won't allow direct access to it, but it can be displayed)
    def display_weakness(self):
        return f"This superhero's weakness is {self.get_weakness()}"

    # Let's create a subclass to demonstrate inheritance and polymorphism
    class Superhero_with_vehicle(Superhero):
        def __init__(self, name, power, weakness, vehicle):
            super().__init__(name, power, weakness)
            self._vehicle = vehicle

        # Overriding the move method from a conceptual base class Animal or Vehicle (not shown here)
        def move(self):
            print(f"{self.get_name()} is moving in their {self._vehicle}!")

        # Additional method to showcase the vehicle
        def showcase_vehicle(self):
            print(f"{self.get_name()} is in their {self.get_vehicle()} vehicle!")

    # Create instances of Superhero and Superhero_with_vehicle
    iron_man = Superhero_with_vehicle("Iron Man", "Repulsor Blast", "Magnetism", "Iron Suit")
    batman = Superhero("Batman", "Detective Skills", "Fear of Bats")

    # Polymorphism Challenge: Animals with different move() actions
    class Animal:
        def move(self):
            raise NotImplementedError("Subclasses must implement abstract method move()")

    class Dog(Animal):
        def move(self):
            print("Running on four legs!")

    class Bird(Animal):
        def move(self):
            print("Flying in the sky!")

    # Creating instances and calling the move method to demonstrate polymorphism
    my_dog = Dog()
    my_bird = Bird()

    print("Dog's action: ", my_dog.move())
    print("Bird's action: ", my_bird.move())

    # Showcasing Superheroes
    print("\nSuperhero Showcase:")
    iron_man.showcase_power()
    iron_man.showcase_vehicle()
    batman.display_weakness()
