MIS = lambda: map(int, input().rstrip().split())
n = int(input())
stat_table = [list(MIS()) for _ in range(n)]

stat_difference = 987654321

team_start = []
team_link = []
temp = []
start_stat = 0
link_stat = 0
def select():
    global stat_difference
    global team_link
    if len(team_start) == n//2:
        # team_link = determine_team_link(team_link)
        # start_stat = 0
        # link_stat = 0 
        # start_stat = calc(team_start)
        # link_stat = calc(team_link)
        stat_difference = min(stat_difference, calc(team_start))
        return None
    for i in range(n):
        if i in team_start:
            continue
        team_start.append(i)
        select()
        team_start.pop()

# def determine_team_link(team_link):
#     team_link = []
#     for i in range(n):
#         if i in team_start:
#             continue
#         team_link.append(i)
#     return team_link

def calc(team):
    sum_start = 0
    sum_link = 0
    for i in range(n):
        for j in range(n):
            if i in team and j in team:
                sum_start += stat_table[i][j]
            elif i not in team and j not in team:
                sum_link += stat_table[i][j]
    return abs(sum_start - sum_link)

select()
print(stat_difference)