from fractions import Fraction
from functools import reduce

def product(fracs):
    # Use reduce to multiply all fractions in the list
    result_fraction = reduce(lambda x, y: x * y, fracs)
    return result_fraction.numerator, result_fraction.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)