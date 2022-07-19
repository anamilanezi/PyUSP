class Calculator:

    def __init__(self):
        self.calc_memory = []
        self.result_memory = []

    def add(self):
        """Return the sum of two given numbers"""
        ab = self.ask_number()
        result = ab[0] + ab[1]
        self.add_to_memory([ab[0], "+", ab[1]], result)

        return result

    def subtract(self):
        """Return the difference of two given numbers"""
        ab = self.ask_number()
        result = ab[0] - ab[1]
        self.add_to_memory([ab[0], "-", ab[1]], result)
        return result

    def multiply(self):
        """Return the product of two given numbers"""
        ab = self.ask_number()
        result = ab[0] * ab[1]
        self.add_to_memory([ab[0], "x", ab[1]], result)
        return result


    def divide(self):
        """Return the division of two given numbers"""
        ab = self.ask_number()
        result = ab[0] / ab[1]
        self.add_to_memory([ab[0], "/", ab[1]], result)
        return result

    def modulus(self):
        """Returns the remainder of dividing two given numbers"""
        ab = self.ask_number()
        result = ab[0] % ab[1]
        self.add_to_memory([ab[0], "mod", ab[1]], result)
        return result


    def square_root(self):
        """Return the square root of given number"""
        n = float(input("Type the number: "))
        sqr_n = n ** 0.5
        self.add_to_memory([n, 'sqr'], sqr_n)
        return sqr_n


    def ask_number(self):
        a = float(input("First number: "))
        b = float(input("Second number: "))
        ab = [a, b]
        return ab


    def add_to_memory(self, n1, n2):
        self.calc_memory.append(n1)
        self.result_memory.append(n2)


# TODO: use last result for next calculation
# TODO: Retrieve a number from memory
# TODO: Print memory as a table