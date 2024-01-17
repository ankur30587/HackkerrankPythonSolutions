import calendar

def find_day(month, day, year):
    # Get the weekday index (Monday is 0 and Sunday is 6)
    weekday_index = calendar.weekday(year, month, day)
    
    # Get the weekday name from the index
    weekday_name = calendar.day_name[weekday_index]
    
    # Print the result in uppercase
    print(weekday_name.upper())

if __name__ == "__main__":
    # Input: space-separated month, day, and year
    month, day, year = map(int, input().split())
    
    # Find and print the day
    find_day(month, day, year)
