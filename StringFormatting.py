def print_formatted(number):
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        decimal_format = f"{i:{width}d}"
        octal_format = f"{oct(i)[2:]:>{width}}"
        hexadecimal_format = f"{hex(i)[2:].upper():>{width}}"
        binary_format = f"{bin(i)[2:]:>{width}}"
        
        print(f"{decimal_format} {octal_format} {hexadecimal_format} {binary_format}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)