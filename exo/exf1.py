# Fonctions: Exercice 1 : exécution et interprétation des résultats

# Définition


def f(a, b, c=10):
    """ f doc """
    
    a ** b + c


print(f(2, 31, 2))
#f(a=2, 31, 2)  # SyntaxError: positional argument follows keyword argument
#f(2, c=31, a=2)  # TypeError: f() got multiple values for argument 'a'

f(2, c=31, b=2)  # ok
f(c=3, a=31, b=2)  # ok
f(3, 2)  # ok
#f(3)  # TypeError: f() missing 1 required positional argument: 'b'
