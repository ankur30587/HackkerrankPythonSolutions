from collections import namedtuple

# Read input
n = int(input())
columns = input().split()

# Create a namedtuple class
Student = namedtuple('Student', columns)

# Initialize sum of marks
total_marks = 0

# Read and process student data
for _ in range(n):
    student_data = input().split()
    student = Student(*student_data)
    total_marks += int(student.MARKS)

# Calculate and print the average marks
average_marks = total_marks / n
print("{:.2f}".format(average_marks))
