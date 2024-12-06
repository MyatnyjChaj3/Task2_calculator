import math


class Calculator:
    def __init__(self):
        self.memory = 0  # Значение памяти
        self.current_value = 0  # Текущее значение калькулятора

    # Операция сложения
    def add(self, value):
        self.current_value += value
        return self.current_value

    # Операция вычитания
    def subtract(self, value):
        self.current_value -= value
        return self.current_value

    # Операция умножения
    def multiply(self, value):
        self.current_value *= value
        return self.current_value

    # Операция деления
    def divide(self, value):
        if value == 0:
            raise ValueError("На ноль делить нельзя.")
        self.current_value /= value
        return self.current_value

    # Округление в большую сторону
    def ceil(self):
        self.current_value = math.ceil(self.current_value)
        return self.current_value

    # Сброс текущего значения
    def clear(self):
        self.current_value = 0
        return self.current_value

    # Работа с памятью: добавить к памяти
    def memory_add(self, value):
        self.memory += value
        return self.memory

    # Работа с памятью: вычесть из памяти
    def memory_subtract(self, value):
        self.memory -= value
        return self.memory

    # Работа с памятью: очистить память
    def memory_clear(self):
        self.memory = 0
        return self.memory

    # Работа с памятью: вернуть значение из памяти
    def memory_recall(self):
        self.current_value = self.memory
        return self.current_value

    def remainder(a, b):
        try:
            return a % b 
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

    def sinus(a):
        if a <= 360 or a >= 0:
            a = a * math.pi() // 180
            return math.sin(a)
        else:
            print('Число должно находиться в диапазоне от 0 до 360')
    
    def cosinus(a, b):
        if a <= 360 or a >= 0:
            a = a * math.pi() // 180
            return math.cos(a)
        else:
            print('Число должно находиться в диапазоне от 0 до 360')
   
    def pow(a, b):
        return a**b
    
    def sqrt(a):
        if a == 0:
            return 1
        elif a > 0:
            return a**(1/2) 
        else:
            print('Число должно быть больше нуля!')
    
    def floor(a):
        return math.floor(a)


