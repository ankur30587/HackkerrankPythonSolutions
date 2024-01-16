def average(array):
    distinct_heights = set(array)
    total_height = sum(distinct_heights)
    count = len(distinct_heights)
    result = total_height / count
    return round(result, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)