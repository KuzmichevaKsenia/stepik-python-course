book = {}
with open("input.txt", "r") as input:
    for line in input:
        for word in line.lower().split():
            if book.get(word) is None:
                book.update({word: 1})
            else:
                book[word] += 1
maxfrequency = max(book.values())
res = ""
for key, value in book.items():
    if value == maxfrequency and (res == "" or key < res):
        res = key
print(res, maxfrequency)
