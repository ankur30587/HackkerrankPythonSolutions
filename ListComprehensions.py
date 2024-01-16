if __name__ == "__main__":
    # Read input from the user
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Generate all possible coordinates using list comprehensions
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

    # Filter out coordinates where the sum is not equal to n
    result = [coord for coord in coordinates if sum(coord) != n]

    # Print the result
    print(result)
