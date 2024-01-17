def check_polynomial(x, k, expression):
    # Evaluate the polynomial expression
    result = eval(expression)

    # Check if the result is equal to k
    return result == k

if __name__ == "__main__":
    # Read input values
    x, k = map(int, input().split())

    # Read the polynomial expression
    expression = input()

    # Check and print the result
    print(check_polynomial(x, k, expression))
