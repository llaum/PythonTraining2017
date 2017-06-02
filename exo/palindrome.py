def digits(x):
    """ natural language integer x """
    digs = []
    while (x != 0):
        div, mod = divmod(x, 10)
        digs.append(mod)
        x = div
    return digs


def is_palindrome(x):
    """ natural integer x """
    if x < 0:
        return False
    digs = digits(x)
    for d in range(len(digs)):
        i, j = digs[d-1], digs[-d]
        if i != j:
            return False
    return True

if __name__ == '__main__':
    print(digits(10))
    print(digits(1234))
