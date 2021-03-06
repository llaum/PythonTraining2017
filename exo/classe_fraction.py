# Exercice 1: une classe de base
# implementer une classe Fraction ...


class Fraction():
    """ ma doc """

    def __init__(self, n, d):
        if d == 0:
            raise ValueError('Le denominateur ne peut pas etre zero')
        elif n == 0:
            self.num = 0
            self.den = 1
        else:
            self.num = n
            self.den = d

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    # def __repr__(self):
    #     return self.__str__() + 'repr'

    def __add__(self, autre):  # F1 + F2
        return Fraction((self.num * autre.den) + (self.den * autre.num), self.den * autre.den)

    def __sub__(self, autre):  # F1 - F2
        return Fraction((self.num * autre.den) - (self.den * autre.num), self.den * autre.den)

    def __mul__(self, autre):  # F1 * F2
        return Fraction(self.num * autre.num, self.den * autre.den)

    def __truediv__(self, autre):  # F1 / F2
        return Fraction(self.num * autre.den, self.den * autre.num)

    def coucou(self):
        return "Coucou" + str(self.num)

    def inverse(self):
        return Fraction(self.den, self.num)


F1 = Fraction(3, 4)
print(type(F1))
print(F1)
print(F1.coucou())
print(F1.inverse())
F2 = Fraction(1, 2)

# (3/4) + (1/2)
print(F1 + F2)
# (3/4) - (1/2)
print(F1 - F2)
# (3/4) * (1/2)
print(F1 * F2)
# (3/4) / (1/2)
print(F1 / F2)
