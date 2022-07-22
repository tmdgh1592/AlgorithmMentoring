#python 사간 초과
#Pypy3 맞았습니다...

MIS = lambda: map(int, input().rstrip().split())
n = int(input())
stat_table = [list(MIS()) for _ in range(n)]

stat_difference = float('inf')
team_start = []
team_link = []

def calc(team1, team2):
    sum_start = 0
    sum_link = 0 
    for i in range(len(team1)):
        for j in range(len(team1)):
            if i == j:
                continue
            sum_start += stat_table[team1[i]][team1[j]]
            sum_link += stat_table[team2[i]][team2[j]]
    return abs(sum_start - sum_link)

for i in range(1 << n):
    team_start = []
    team_link = []
    valid = 0
    for j in range(n):
        if i & (1 << j):
            valid += 1
    if valid != n / 2:
        continue
    for j in range(n):
        if i & (1 << j):
            team_start.append(j)
        else:
            team_link.append(j)
    stat_difference = min(stat_difference, calc(team_start, team_link))

print(stat_difference)