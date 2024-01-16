if __name__ == "__main__":
    # Initialize an empty list
    my_list = []

    # Read the number of commands
    n = int(input())

    # Process each command
    for _ in range(n):
        command = input().split()

        # Execute the corresponding command
        if command[0] == "insert":
            position, element = int(command[1]), int(command[2])
            my_list.insert(position, element)
        elif command[0] == "print":
            print(my_list)
        elif command[0] == "remove":
            element = int(command[1])
            my_list.remove(element)
        elif command[0] == "append":
            element = int(command[1])
            my_list.append(element)
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "pop":
            my_list.pop()
        elif command[0] == "reverse":
            my_list.reverse()
