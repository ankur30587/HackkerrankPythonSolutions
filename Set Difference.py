if __name__ == '__main__':
    n_english = int(input())
    roll_english = set(map(int, input().split()))
    n_french = int(input())
    roll_french = set(map(int, input().split()))

    english_only = roll_english.difference(roll_french)
    print(len(english_only))
