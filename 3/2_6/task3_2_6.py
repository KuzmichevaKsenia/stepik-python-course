res = {}
for i in input().lower().split():
    if res.get(i) is None:
        res.update({i: 1})
    else:
        res[i] += 1

for key, value in res.items():
    print(key, value)
