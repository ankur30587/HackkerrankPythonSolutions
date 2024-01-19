from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for att in attrs:
                print(f'-> {att[0]} > {att[1]}')

    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for att in attrs:
                print(f'-> {att[0]} > {att[1]}')

def main():
    num_lines = int(input())
    html_code = '\n'.join([input() for _ in range(num_lines)])

    parser = MyHTMLParser()
    parser.feed(html_code)

if __name__ == "__main__":
    main()
