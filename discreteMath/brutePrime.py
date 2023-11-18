# This script solve prime numbers by brute force.
# It is not efficient, but it is easy to understand.

import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def main():
    for i in range(1000000):
        if is_prime(i):
            print(f'{i} is prime')


if __name__ == '__main__':
    main()
