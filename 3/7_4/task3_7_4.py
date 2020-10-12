n = int(input())
x, y = (0, 0)
for i in range(n):
    direction, steps = input().split()
    steps = int(steps)
    if direction == "север":
        y += steps
    elif direction == "запад":
        x -= steps
    elif direction == "юг":
        y -= steps
    elif direction == "восток":
        x += steps
print(x, y)
