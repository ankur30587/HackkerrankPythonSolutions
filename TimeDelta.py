from datetime import datetime, timedelta

def time_delta(t1, t2):
    # Convert timestamps to datetime objects
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)

    # Calculate the absolute difference in seconds
    delta = abs(dt1 - dt2).total_seconds()

    return int(delta)

if __name__ == "__main__":
    # Input: number of test cases
    t = int(input())

    for _ in range(t):
        # Input: two timestamps
        timestamp1 = input()
        timestamp2 = input()

        # Calculate and print the absolute difference in seconds
        result = time_delta(timestamp1, timestamp2)
        print(result)
