def count_distinct_stamps(n, country_list):
    distinct_stamps = set(country_list)
    return len(distinct_stamps)

if __name__ == "__main__":
    # Read the total number of country stamps
    n = int(input())

    # Read the country stamps and store them in a list
    country_list = [input().strip() for _ in range(n)]

    # Calculate the total number of distinct country stamps
    result = count_distinct_stamps(n, country_list)

    # Print the result
    print(result)
