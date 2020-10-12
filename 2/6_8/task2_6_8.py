n = int(input())
res = []
cntr = 1
while len(res) < n:
    for i in range(cntr):
        res.append(cntr)
        if len(res) == n:
            break
    cntr += 1
print(' '.join(str(value) for value in res))
