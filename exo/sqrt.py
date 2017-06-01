# Exemple: une simple fonction math -> calcul de racine carrée


def sqrt(x):
    if x < 0:
        raise ValueError('Error: square root of negative')
    guess = x
    i = 0
    while guess + guess != x and i < 20:
        try:
            guess = (guess + x / guess) / 2.0
        except ZeroDivisionError:
            print('Except ZeroDivisionError: float division by zero')
            #exit(1)
        i += 1
    return guess


sqrt(2)

sqrt(0)

sqrt(-1)
