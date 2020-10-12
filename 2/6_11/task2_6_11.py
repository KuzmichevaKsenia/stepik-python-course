n = int(input())
res = []
for i in range(n):
    res.append([0] * n)
i = 0
j = 0
res[i][j] = 1
number = 2
while number <= n**2:
    if j+1 != n and res[i][j+1] == 0:
        while j+1 < n and res[i][j+1] == 0:
            j += 1
            res[i][j] = number
            number += 1
    elif i+1 != n and res[i+1][j] == 0:
        while i+1 < n and res[i+1][j] == 0:
            i += 1
            res[i][j] = number
            number += 1
    elif j != 0 and res[i][j-1] == 0:
        while j > 0 and res[i][j-1] == 0:
            j -= 1
            res[i][j] = number
            number += 1
    elif i != 0 and res[i-1][j] == 0:
        while i > 0 and res[i-1][j] == 0:
            i -= 1
            res[i][j] = number
            number += 1
for row in res:
    print(' '.join(list(map(str, row))))
