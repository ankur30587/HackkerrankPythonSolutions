if __name__ == "__main__":
    a = int(input())
    b = int(input())

    quotient = a // b  # Integer division
    remainder = a % b  # Modulo operator
    divmod_result = divmod(a, b)  # divmod function

    print(quotient)
    print(remainder)
    print(divmod_result)
