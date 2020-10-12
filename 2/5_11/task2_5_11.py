a = [i for i in input().split()]
a.sort()
res = []
prev = ' '
for i in a:
    if i == prev and (len(res) == 0 or res[-1] != i):
        res.append(i)
    prev = i
print(' '.join(str(value) for value in res))
