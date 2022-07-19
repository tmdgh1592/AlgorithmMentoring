import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = list(MIS())

a = 0
sum = 0
for i in range(1, (1 << n)): # 부분수열의 모든 경우의 수는 (2 ^ n) - 1 / 1~ (2 ^ n) - 1 까지 모든 경우 고려
    sum = 0
    for j in range(n):
        if(i & (1 << j)) != 0: # 반복문 돌면서 j만큼 비트를 밀며 sum에 더해줌
            sum +=arr[j] 
    if sum == m: # sum과 목표 숫자가 같으면 a에 + 1
        a += 1

print(a)
