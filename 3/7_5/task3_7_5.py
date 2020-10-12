list_of_heights = []
for i in range(11):
    list_of_heights.append([])
with open("input.txt") as table:
    for row in table:
        row_elems = row.split("\t")
        list_of_heights[int(row_elems[0])-1].append(int(row_elems[2]))
with open("output.txt", "w") as out:
    for i in range(11):
        middle_height = "-"
        if list_of_heights[i]:
            middle_height = str(sum(list_of_heights[i]) / len(list_of_heights[i]))
        out.write(str(i+1) + " " + middle_height + "\n")
