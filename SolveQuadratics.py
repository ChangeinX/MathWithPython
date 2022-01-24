from math import sqrt


def quad(a, b, c):
    # Note equation must be in form
    # ax^2 + bx+ c = 0
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2
