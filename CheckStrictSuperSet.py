def is_strict_superset(set_a, other_sets):
    for other_set in other_sets:
        if not set_a.issuperset(other_set):
            return False
    return True

if __name__ == "__main__":
    set_a = set(map(int, input().split()))
    num_other_sets = int(input())
    
    other_sets = []
    for _ in range(num_other_sets):
        other_set = set(map(int, input().split()))
        other_sets.append(other_set)

    result = is_strict_superset(set_a, other_sets)
    print(result)
