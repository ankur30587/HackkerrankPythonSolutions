import math
import os
import random
import re
import sys

if __name__ == "__main__":
    # Read input from the user
    n = int(input())

    # Print the square of each non-negative integer less than n
    for i in range(n):
        print(i ** 2)
