def solve(s):
    # Capitalize each word in the string
    capitalized_name = ' '.join(word.capitalize() for word in s.split(' '))
    return capitalized_name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
