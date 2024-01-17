def can_stack_cubes(test_cases):
    for cubes in test_cases:
        left_index = 0
        right_index = len(cubes) - 1
        current_cube = float('inf')

        while left_index <= right_index:
            left_cube = cubes[left_index]
            right_cube = cubes[right_index]

            if left_cube >= right_cube and left_cube <= current_cube:
                current_cube = left_cube
                left_index += 1
            elif right_cube >= left_cube and right_cube <= current_cube:
                current_cube = right_cube
                right_index -= 1
            else:
                print("No")
                break
        else:
            print("Yes")

if __name__ == '__main__':
    t = int(input().strip())  # Number of test cases

    test_cases = []
    for _ in range(t):
        n = int(input().strip())  # Number of cubes
        blocks = list(map(int, input().split()))  # Side lengths of cubes
        test_cases.append(blocks)

    can_stack_cubes(test_cases)
