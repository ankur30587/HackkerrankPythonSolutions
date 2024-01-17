import sys

def average_marks(n, m, marks):
    # Transpose the matrix to get subjects as rows and students as columns
    transposed_marks = zip(*marks)

    # Calculate and print the average for each student
    for student_marks in transposed_marks:
        average = sum(student_marks) / m
        print("{:.2f}".format(average))

if __name__ == "__main__":
    # Read the number of students and subjects
    n, m = map(int, input().split())

    # Read the marks for each subject and student
    marks = [list(map(float, line.split())) for line in sys.stdin.read().splitlines()]

    # Calculate and print the average marks for each student
    average_marks(n, m, marks)
