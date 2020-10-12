matrix = []
res = []
string = input()
while string != "end":
    matrix.append([int(i) for i in string.split()])
    string = input()
for i in range(len(matrix)):
    row = []
    for j in range(len(matrix[i])):
        number = matrix[i-1][j] + matrix[i][j-1]
        if i == len(matrix) - 1:
            number += matrix[0][j]
        else:
            number += matrix[i+1][j]
        if j == len(matrix[i]) - 1:
            number += matrix[i][0]
        else:
            number += matrix[i][j+1]
        row.append(number)
    res.append(row)
for row in res:
    print(' '.join(list(map(str, row))))
