import re

def is_valid_uid(uid):
    # Rule 1: At least 2 uppercase English alphabet characters
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False

    # Rule 2: At least 3 digits
    if len(re.findall(r'\d', uid)) < 3:
        return False

    # Rule 3: Only alphanumeric characters, no repeating characters
    if len(set(uid)) != len(uid):
        return False

    # Rule 4: Exactly 10 characters in a valid UID
    if len(uid) != 10:
        return False

    return True

def main():
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        uid = input().strip()
        result = "Valid" if is_valid_uid(uid) else "Invalid"
        print(result)

if __name__ == "__main__":
    main()
