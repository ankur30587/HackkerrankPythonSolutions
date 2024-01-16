if __name__ == '__main__':
    n = int(input())
    initial_set = set(map(int, input().split()))
    num_operations = int(input())

    for _ in range(num_operations):
        operation, _ = input().split()
        other_set = set(map(int, input().split()))

        if operation == 'intersection_update':
            initial_set.intersection_update(other_set)
        elif operation == 'update':
            initial_set.update(other_set)
        elif operation == 'symmetric_difference_update':
            initial_set.symmetric_difference_update(other_set)
        elif operation == 'difference_update':
            initial_set.difference_update(other_set)

    print(sum(initial_set))
