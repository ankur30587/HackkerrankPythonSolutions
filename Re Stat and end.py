import re

def find_start_end_indices(string, substring):
    pattern = re.compile(r'(?=('+substring+'))')
    matches = re.finditer(pattern, string)
    
    found = False
    for match in matches:
        print(f'({match.start(1)}, {match.end(1) - 1})')
        found = True
    
    if not found:
        print('(-1, -1)')

if __name__ == '__main__':
    string = input().strip()
    substring = input().strip()
    find_start_end_indices(string, substring)
