from collections import Counter

def company_logo(s):
    # Count occurrences of each character
    char_count = Counter(s)

    # Sort characters by occurrence count and then alphabetically
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

    # Print the top three characters and their occurrence count
    for i in range(3):
        print(f"{sorted_chars[i][0]} {sorted_chars[i][1]}")

if __name__ == "__main__":
    # Read input
    s = input()

    # Call the function
    company_logo(s)
