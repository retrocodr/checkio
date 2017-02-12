#  You are given a positive integer. Your function should calculate the product of the digits excluding any
#  zeroes.
#
# For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
#
# Input: A positive integer.
#
# Output: The product of the digits as an integer.


import numpy as np


def checkio(number):
    return np.product([int(i) for i in str(number) if int(i) is not 0])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1