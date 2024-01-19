import re

def extract_hex_color_codes(css_code):
    pattern = r'#(?:[0-9a-fA-F]{3}){1,2}\b'
    return re.findall(pattern, css_code)

if __name__ == "__main__":
    num_lines = int(input())
    css_lines = [input() for _ in range(num_lines)]

    in_block = False
    for line in css_lines:
        if '{' in line:
            in_block = True
        elif '}' in line:
            in_block = False
        elif in_block:
            color_codes = extract_hex_color_codes(line)
            for code in color_codes:
                print(code)
