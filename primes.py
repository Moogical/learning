"""
How this works:
    Every number n that is not prime has at least one prime divisor p
    such 1 < p < square_root(n)
"""


def is_prime(num):
    if num in [2, 3]:
        return True
    elif num < 2 or num % 2 == 0:
        return False
    else:
        # no need to iterate over even numbers, only prime even number is 2
        # this improves performance
        for divisor in range(3, int((num ** 0.5)+1), 2):
            if num != divisor and num % divisor == 0:
                return False
        return True
