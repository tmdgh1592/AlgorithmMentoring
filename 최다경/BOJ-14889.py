import math
n = int(input())
m = n // 2
stats = [list(map(int, input().split())) for _ in range (n)]
team_a = []
team_b = []
team = []
entry = 1
num = (math.factorial(n) // (math.factorial(n-m)*math.factorial(m))) // 2
ret = 999

def calc(arr, stats):
    stat_sum = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j: continue
            stat_sum += stats[arr[i]-1][arr[j]-1]
            
    return stat_sum

def bf(n, m, stats):
    global team_a, team_b, entry, team, ret

    entry = 1
    permutation(list(), n, m, entry)
    for i in range(0, num):
        team_a.append(team[i])
        team_b.append(team[num*2-i-1])
    
    for i in range(0, num):
        ret = min(ret, abs(calc(team_a[i], stats) - calc(team_b[i], stats)))
    
    return ret

def permutation(arr, n, m, entry):
    tmp = []
    global team
    if len(arr) == m:
        tmp = arr.copy()
        team.append(tmp)
        return None
    
    for i in range(entry, n+1):
        if i in arr: continue

        arr.append(i)
        entry += 1
        permutation(arr, n, m, entry)
        post = arr.pop()

print(bf(n, m, stats))


