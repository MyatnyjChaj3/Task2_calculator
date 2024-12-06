import math


class Calculator:
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
    
    def cosinus(a,b):
        if a <= 360 or a >= 0:
            a = a * math.pi() // 180
            return math.cos(a)
        else:
            print('Число должно находиться в диапазоне от 0 до 360')
    def pow(a,b):
        return a**b

