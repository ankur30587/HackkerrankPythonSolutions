def perform_division(a, b):
    try:
        result = int(a) // int(b)
        print(result)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error Code: {e}")

if __name__ == "__main__":
    # Input: number of test cases
    t = int(input())

    for _ in range(t):
        # Input: two values a and b
        a, b = input().split()
        perform_division(a, b)
