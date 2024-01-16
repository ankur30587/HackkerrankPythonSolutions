def calculate_happiness(array, set_a, set_b):
    happiness = 0
    for num in array:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1
    return happiness

if __name__ == '__main__':
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    result = calculate_happiness(array, set_a, set_b)
    print(result)