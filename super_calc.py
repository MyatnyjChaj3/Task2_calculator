import math


class Calculator:

    def remainder(self, value):
        try:
            return Calculator.self % value 
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

    def sin(self):
        if Calculator.self <= 360 or Calculator.self >= 0:
            a = a * math.pi() // 180
            return math.sin(Calculator.self)
        else:
            print('Число должно находиться в диапазоне от 0 до 360')
    
    def cos(self):
        if Calculator.self <= 360 or Calculator.self >= 0:
            a = a * math.pi() // 180
            return math.cos(Calculator.self)
        else:
            print('Число должно находиться в диапазоне от 0 до 360')
   
    def pow(self, value):
        return Calculator.self**value
    
    def sqrt(self):
        if Calculator.self == 0:
            return 1
        elif Calculator.self > 0:
            return Calculator.self**(1/2) 
        else:
            print('Число должно быть больше нуля!')
    
    def floor(self):
        return math.floor(Calculator.self)


