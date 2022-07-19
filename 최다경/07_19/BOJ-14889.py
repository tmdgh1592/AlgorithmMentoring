import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
stats = [list(MIS()) for _ in range(n)]

teama = []
teamb = []

a = float("inf")

def check_t(num, n): # 조합 가능한 팀인지 체크 함수 / n을 2로 나눈것과 1의 수가 같아야 함
    bi = list(bin(num))
    if bi.count('1') == (n // 2):
        return True
    else:
        return False

def calc(arr): # 팀 능력치 계산 함수
    sum = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] == arr[j]: continue
            sum += stats[arr[i]][arr[j]]
    return sum


for i in range(1 << n): 
    teama = []
    teamb = [] # 팀 초기화
    if not check_t(i, n): # 가능한 팀 조합인지 체크
        continue

    for j in range(n): # 조합 가능한 팀이면 각 팀 배열에 append
        if i & (1 << j):
            teama.append(j)
        else:
            teamb.append(j)
    
    sum_a = calc(teama)
    sum_b = calc(teamb)
    a = min(a, abs(sum_a - sum_b)) # 팀 간의 능력치 차이 최소값 저장

print(a)