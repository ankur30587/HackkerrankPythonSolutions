if __name__ == "__main__":
    # Read input from the user
    n = int(input())
    
    # Create a nested list to store names and grades
    student_list = []
    for _ in range(n):
        name = input()
        score = float(input())
        student_list.append([name, score])

    # Find the second lowest grade
    second_lowest_grade = sorted(set(score for name, score in student_list))[1]

    # Filter and sort names with the second lowest grade
    result_names = sorted(name for name, score in student_list if score == second_lowest_grade)

    # Print the result
    for name in result_names:
        print(name)
