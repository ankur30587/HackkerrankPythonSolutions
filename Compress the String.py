from itertools import groupby

def compress_string(s):
    # Use groupby to group consecutive occurrences of characters
    groups = [(len(list(g)), int(k)) for k, g in groupby(s)]

    # Format the result and join into a string
    result = " ".join(f"({count}, {key})" for count, key in groups)
    return result

# Read input
s = input().strip()

# Print the compressed string
print(compress_string(s))
