def print_rangoli(size):
    # your code goes here
    import string

    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append((s).center(size*4-3, '-'))

    rangoli = "\n".join(lines[::-1] + lines[1:])
    print(rangoli)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)