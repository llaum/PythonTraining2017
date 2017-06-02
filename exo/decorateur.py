# decorateur definition

import time


def timed_sum(a_function):
    def effective_function(n):
        t_0 = time.time()
        a_function(n)
        t_1 = time.time()
        return (n, t_1 - t_0, a_function.__name__)
    return effective_function


def sum_of_int_by_method_1(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


# sans decorateur
print(timed_sum(sum_of_int_by_method_1(1000000000)))


# avec decorateur
@timed_sum
def timed_sum_of_int_by_method_1(n):
    sum_of_int_by_method_1(n)

#sum_of_int_by_method_1(1000000000)
print(sum_of_int_by_method_1(4))
