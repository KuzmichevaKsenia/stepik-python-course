words_n = int(input())
right_words = set()
for w in range(words_n):
    right_words.add(input().lower())
text_lines_n = int(input())
wrong_words = set()
for line in range(text_lines_n):
    for w in input().lower().split():
        if w not in right_words:
            wrong_words.add(w)
print("\n".join(w for w in wrong_words))
