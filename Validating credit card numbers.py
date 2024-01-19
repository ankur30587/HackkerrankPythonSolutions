import re

def validate_credit_card(string):
    pattern = re.compile(
        r'^'
        r'(?!\d*(\d)(-?\1){3})'
        r'[456]\d{3}(-?\d{4}){3}'
        r'$'
    )
    return 'Valid' if re.match(pattern, string) else 'Invalid'

def main():
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        card_number = input().strip()
        result = validate_credit_card(card_number)
        print(result)

if __name__ == "__main__":
    main()
