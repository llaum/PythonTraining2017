# Exercice 4:  polynôme du second degré
"""
a x² + b x + c =0
delta = b²-4ac
delta<0 => pas de soll
delta=0 => x1 = -b/2a
delta>0 => x1=(-b+sqr(delta))/2a x2=(-b-sqr(delta))/2a
"""


def polynome_second_degre(a, b, c=0):
    """ return tuple (nbsolution, {sol1, sol2, ...}) """
    delta = b**2 - 4 * a * c
    if delta == 0:
        return (1, {-(b / (2 * a))})
    elif delta > 0:
        return (2, {(-b + delta**0.5) / (2 * a) , (-b - delta**0.5) / (2 * a)})
    else:  # delta < 0
        return (0, {})


print(polynome_second_degre(2, 4))
print(polynome_second_degre(1, 2, 1))
print(polynome_second_degre(1, 0, 1))
