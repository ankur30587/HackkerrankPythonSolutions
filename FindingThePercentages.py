if __name__ == "__main__":
    # Read input from the user
    n = int(input())
    student_marks = {}

    # Populate the dictionary with names and marks
    for _ in range(n):
        line = input().split()
        name, marks = line[0], list(map(float, line[1:]))
        student_marks[name] = marks

    # Read the query_name
    query_name = input()

    # Calculate and print the average marks for the specified student
    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{:.2f}".format(average_marks))
