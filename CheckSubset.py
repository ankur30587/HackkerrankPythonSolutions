def is_subset(set_a, set_b):
    return set_a.issubset(set_b)

if __name__ == "__main__":
    test_cases = int(input())
    
    for _ in range(test_cases):
        _ = input()  # Discard the number of elements in set A (not needed)
        set_a = set(map(int, input().split()))
        
        _ = input()  # Discard the number of elements in set B (not needed)
        set_b = set(map(int, input().split()))
        
        result = is_subset(set_a, set_b)
        print(result)
