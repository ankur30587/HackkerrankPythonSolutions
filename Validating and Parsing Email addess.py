import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z]+ <[a-zA-Z]+[\.\_\-\w]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>$"
    return re.search(pattern, email) is not None

if __name__ == "__main__":
    num_emails = int(input())
    
    for _ in range(num_emails):
        email = input()
        
        if is_valid_email(email):
            print(email)
