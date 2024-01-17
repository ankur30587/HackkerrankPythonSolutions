if __name__ == "__main__":
    # Read the number of integers
    n = int(input())

    # Read the list of integers
    integers = list(map(int, input().split()))

    # Check if all integers are positive and at least one is palindromic
    condition_satisfied = all(x > 0 for x in integers) and any(str(x) == str(x)[::-1] for x in integers)

    # Print the result
    print(condition_satisfied)
