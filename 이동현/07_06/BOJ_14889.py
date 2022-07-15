
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
stat_table = [list(MIS()) for _ in range(n)]

stat_difference = 987654321

team_start = []
team_link = []
temp = {}
start_stat = 0
link_stat = 0
def select():
    global stat_difference
    global team_link
    if len(team_start) == n//2:
        temp = set(team_start)
        temp = set(range(n)) - temp
        team_link = list(temp) 
        stat_difference = min(stat_difference, abs(calc(team_start) - calc(team_link)))
        return None
    for i in range(n):
        if i in team_start:
            continue
        select()
        team_start.append(i)
        team_start.pop()

def calc(team):
    sum = 0 
    for i in range(n//2):
        for j in range(n//2):
           sum += stat_table[team[i]][team[j]] 
    return sum

select()
print(stat_difference)