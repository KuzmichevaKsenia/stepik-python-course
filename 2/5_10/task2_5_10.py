a = [int(i) for i in input().split()]
res = []
counter = 0
while counter < len(a) - 1:
    res.append(a[counter-1] + a[counter+1])
    counter += 1
if len(a) > 1:
    res.append(a[-2] + a[0])
    print(' '.join(str(value) for value in res))
else:
    print(a[0])
