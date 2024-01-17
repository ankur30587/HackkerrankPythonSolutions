from collections import Counter

def calculate_earnings(shoe_sizes, customer_requests):
    shoe_inventory = Counter(shoe_sizes)
    total_earnings = 0

    for size, price in customer_requests:
        if shoe_inventory[size] > 0:
            total_earnings += price
            shoe_inventory[size] -= 1

    return total_earnings

# Read input
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())
customer_requests = [tuple(map(int, input().split())) for _ in range(num_customers)]

# Calculate and print the result
earnings = calculate_earnings(shoe_sizes, customer_requests)
print(earnings)
