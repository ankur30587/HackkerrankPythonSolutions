if __name__ == "__main__":
    # Read values of n and m
    n, m = map(int, input().split())

    # Read athlete details into a list of lists
    arr = [list(map(int, input().split())) for _ in range(n)]

    # Read k, the attribute to sort the table by
    k = int(input())

    # Sort the table based on the k-th attribute
    arr.sort(key=lambda x: x[k])

    # Print the sorted table
    for row in arr:
        print(*row)
