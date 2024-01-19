import re 

def modify_text(text):
    return re.sub(r'(?<=\s)&&(?=\s)', 'and', re.sub(r'(?<=\s)\|\|(?=\s)', 'or', text))
    
if __name__ == '__main__':
    modify_texts = [
        modify_text(input())
        for _ in range(int(input()))
    ]

    for result_text in modify_texts:
        print(result_text)
