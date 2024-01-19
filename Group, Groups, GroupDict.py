import re

s = input()

pattern = re.compile(r'([a-zA-Z0-9])\1')

match = pattern.search(s)

if match:
    print(match.group(1))
else:
    print(-1)
