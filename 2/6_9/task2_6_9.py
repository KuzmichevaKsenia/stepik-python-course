a = [int(i) for i in input().split()]
num = int(input())
res = []
for i in range(len(a)):
    if a[i] == num:
        res.append(i)
if len(res) == 0:
    print("Отсутствует")
else:
    print(' '.join(str(value) for value in res))
