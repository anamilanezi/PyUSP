class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """The init method runs automatically whenever we create a new instance based on this class. The self parameter
        is also passed automatically when creating an instance, and should always come first. The name and age should be
        provided when creating a new instance. The variables take the value associated with the parameter name (passed
        as an argument) and assign to the variable on the left, which is then attached to the instance being created.
        Variables accessible through instances are the attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command. This is a method and any instance of dog will have the abili
        ty to perform this actions. They also need the self parameter """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# Here Python will call the __init__() method and creates an instance representing this particular dog and sets the name
# and age attributes

my_dog = Dog('Muffin', 11)
my_other_dog = Dog('Lionel', 2)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
print(f"{my_dog.name} has a brother called {my_other_dog.name}.")

# Calling methods
my_dog.sit()
my_dog.roll_over()
my_other_dog.sit()
my_other_dog.roll_over()
