import math

class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("На ноль делить нельзя.")
        return a / b

    def remainder(self, a, b):
        if b == 0:
            raise ValueError("На ноль делить нельзя.")
        return a % b

    def pow(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Число должно быть больше или равно нулю.")
        return math.sqrt(a)

    def sin(self, a):
        if 0 <= a <= 360:
            return math.sin(math.radians(a))
        else:
            raise ValueError("Число должно находиться в диапазоне от 0 до 360.")

    def cos(self, a):
        if 0 <= a <= 360:
            return math.cos(math.radians(a))
        else:
            raise ValueError("Число должно находиться в диапазоне от 0 до 360.")

    def ceil(self, a):
        return math.ceil(a)

    def floor(self, a):
        return math.floor(a)

    # Методы для работы с памятью
    def memory_clear(self):
        self.memory = 0

    def memory_recall(self):
        return self.memory

    def memory_add(self, value):
        self.memory += value

    def memory_subtract(self, value):
        self.memory -= value

    def memory_set(self, value):
        self.memory = value
