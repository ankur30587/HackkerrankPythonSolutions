from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def handle_comment(self, comment_data):
        # Check for multiline comments
        if '\n' in comment_data:
            print(">>> Multi-line Comment")
            print(comment_data)
        else:
            # Single-line comments
            print(">>> Single-line Comment")
            print(comment_data)

    def handle_data(self, data):
        # Check for newlines in data
        if '\n' not in data:
            print(">>> Data")
            print(data)

def main():
    num_lines = int(input())
    
    # Read input lines and concatenate into HTML string
    html_content = ""
    for _ in range(num_lines):
        html_content += input().rstrip() + '\n'

    # Initialize and use the custom parser
    custom_parser = CustomHTMLParser()
    custom_parser.feed(html_content)
    custom_parser.close()

if __name__ == "__main__":
    main()
