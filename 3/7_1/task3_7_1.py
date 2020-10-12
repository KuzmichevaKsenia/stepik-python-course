def add_result(team, balls):
    if balls > 0:
        res = [1, 1, 0, 0, 3]
    elif balls < 0:
        res = [1, 0, 0, 1, 0]
    else:
        res = [1, 0, 1, 0, 1]
    global teams
    old_val = teams.get(team)
    if old_val is None:
        teams.update({team: res})
    else:
        teams.update({team: [old_val[0] + res[0], old_val[1] + res[1], old_val[2] + res[2], old_val[3] + res[3],
                             old_val[4] + res[4]]})


teams = {}
n = int(input())
for match in range(n):
    team1, balls1, team2, balls2 = input().split(";")
    balls1 = int(balls1)
    balls2 = int(balls2)
    add_result(team1, balls1 - balls2)
    add_result(team2, balls2 - balls1)
for key, value in teams.items():
    print(key + ":", end="")
    for v in value:
        print(str(v), end=" ")
    print()
