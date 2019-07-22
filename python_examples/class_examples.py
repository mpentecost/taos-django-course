"""
Simple class examples
"""

# Start by creating a base class
class Car:
    """A car object"""

    def __init__(self, model, year, color):
        """Initialze our instance variables"""

        self.model = model
        self.year = year
        self.color = color

    
    def print_info(self):
        """Instance method - prints a car's information"""
        print(f"I'm a {self.color} {self.model} built in {self.year}")

    @classmethod
    def print_speed_limit(cls):
        """A class method, this function works without creating an instance"""
        print("Speed limit is 65!")
    
    @property
    def engine(self):
        """a 'property' can be accessed by dot notation"""
        return "5.0L V8"

    
# we can create instanes with the class now and use the methods.
mustang = Car(model="Mustang", year="2019", color="graphite")

# we can view the attributes
print(mustang.model)
print(mustang.year)
print(mustang.color)

# and use the methods
mustang.print_info()

# and look a the property: notice we don't have to call a property like a function
print(mustang.engine)

# we can use the classmethod without creating an instance
Car.print_speed_limit()

# We can create a new class and base it on the Car class


class Truck(Car):
    """A truck object"""

    @property
    def max_load(self):
        """The max load of the truck"""
        return "2 tons"

    def print_info(self):
        """Override print_info from the parent class"""
        # call the print statement from the parent class
        super().print_info()
        # add another print statement
        print(f"I'm also a truck with a max load of {self.max_load}")

# let's create some instances
raptor = Truck(model="raptor", year="2019", color="blue")

print(raptor.max_load)
raptor.print_info()
