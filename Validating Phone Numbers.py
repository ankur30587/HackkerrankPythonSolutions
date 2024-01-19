import re

def is_valid_mobile_number(number):
    # Define the regex pattern for a valid mobile number
    pattern = r'^[789]\d{9}$'
    
    # Check if the number matches the pattern
    if re.match(pattern, number):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    # Input the number of test cases
    t = int(input())
    
    # Iterate through each test case
    for _ in range(t):
        mobile_number = input().strip()
        result = is_valid_mobile_number(mobile_number)
        print(result)
