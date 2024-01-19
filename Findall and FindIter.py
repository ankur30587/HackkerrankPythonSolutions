import re

def find_vowel_substrings(s):
    pattern = re.compile(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])')
    matches = re.findall(pattern, s)
    
    if matches:
        for match in matches:
            print(match)
    else:
        print(-1)

if __name__ == '__main__':
    s = input()
    find_vowel_substrings(s)
