def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    total_score = 0
    for word in words:
        vowel_count = sum(1 for char in word if is_vowel(char))
        if vowel_count % 2 == 0:
            total_score += 2
        else:
            total_score += 1
    return total_score


n = int(input())
words = input().split()
print(score_words(words))