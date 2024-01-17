def fun(s):
    # Split the email into username, domain, and extension
    parts = s.split('@')
    
    # Check if there are two parts after splitting by '@'
    if len(parts) == 2:
        username, rest = parts
        # Check if there is at least one dot in the rest
        if '.' in rest:
            domain, extension = rest.split('.', 1)

            # Check conditions for a valid email
            if len(username) > 0 and all(char.isalnum() or char in ['-', '_'] for char in username) and \
                len(domain) > 0 and all(char.isalnum() for char in domain) and \
                0 < len(extension) <= 3 and all(char.isalpha() for char in extension):
                return True

    return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)