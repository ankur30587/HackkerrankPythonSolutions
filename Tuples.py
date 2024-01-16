if __name__ == "__main__":
    # Read input from the user
    n = int(input())
    integer_list = map(int, input().split())

    # Create a tuple
    my_tuple = tuple(integer_list)

    # Print the hash value
    result = hash(my_tuple)
    print(result)
