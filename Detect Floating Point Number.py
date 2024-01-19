import re

def is_valid_float(s):
    # Define the pattern for a valid float
    pattern = r'^[+-]?[0-9]*\.[0-9]+$'
    # Use re.match to check if the string matches the pattern
    return bool(re.match(pattern, s))

if __name__ == '__main__':
    # Input the number of test cases
    t = int(input().strip())
    
    for _ in range(t):
        # Input the string for each test case
        s = input().strip()
        # Check if it's a valid float and print the result
        print(is_valid_float(s))
