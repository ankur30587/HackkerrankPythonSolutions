if __name__ == "__main__":
    # Read the input string
    s = input()

    # Sort the string based on the specified conditions
    sorted_string = sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))

    # Print the result
    print("".join(sorted_string))
