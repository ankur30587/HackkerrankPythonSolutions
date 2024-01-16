def split_and_join(line):
    # Split the string on spaces and join using a hyphen
    words = line.split(" ")
    result = "-".join(words)
    return result

if __name__ == "__main__":
    # Read input from the user
    input_line = input()

    # Call the split_and_join function and print the result
    output_line = split_and_join(input_line)
    print(output_line)
