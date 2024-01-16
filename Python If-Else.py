import math
import os
import random
import re
import sys

def is_weird(n):
    if n % 2 != 0:
        return "Weird"
    elif n % 2 == 0 and 2 <= n <= 5:
        return "Not Weird"
    elif n % 2 == 0 and 6 <= n <= 20:
        return "Weird"
    elif n % 2 == 0 and n > 20:
        return "Not Weird"

if __name__ == "__main__":
    # Read input from the user
    n = int(input())

    # Check conditions and print the result
    result = is_weird(n)
    print(result)
