import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

if __name__ == "__main__":
    # Input: number of test cases
    t = int(input())

    for _ in range(t):
        # Input: regular expression pattern
        pattern = input().strip()
        result = is_valid_regex(pattern)
        print(result)
