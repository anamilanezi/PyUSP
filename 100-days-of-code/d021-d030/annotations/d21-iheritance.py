class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    # The call to super() in the initialiser is recommended, but not strictly required.
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this under water")

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.breathe()
