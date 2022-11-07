import sys
from collections import defaultdict
imput = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, s = MIS()
arr = list(MIS())
d1 = defaultdict(int)

data1 = arr[0:len(arr) // 2]
data2 = arr[len(arr) // 2:]

sum = 0

for i in range(1, (1 << len(data1))):
    sum = 0
    for j in range(len(data1)):
        if(i & (1 << j)) != 0: # 반복문 돌면서 j만큼 비트를 밀며 sum에 더해줌
            sum +=data1[j] 
    d1[sum] += 1

sum2 = 0
res = 0
for i in range(1, (1 << len(data2))):
    sum2 = 0
    for j in range(len(data2)):
        if(i & (1 << j)) != 0: # 반복문 돌면서 j만큼 비트를 밀며 sum에 더해줌
            sum2 +=data2[j]
    if  d1[s - sum2] > 0:
        res += 1

    
print(res)
