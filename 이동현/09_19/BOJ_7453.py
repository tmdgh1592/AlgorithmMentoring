import sys
from collections import defaultdict
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
A = []
B = []
C = []
D = []

for i in range(n):
    a,b,c,d = MIS()
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# AB = defaultdict(int)
# CD = defaultdict(int)

# for i in range(n):
#     for j in range(n):
#         AB[A[i] + B[j]] += 1
#         CD[C[i] + D[j]] += 1    

# cnt = 0
# for key, value in CD.items():
#     if AB[-key] != 0:
#         cnt += ((AB[-key]) *(value)) 
AB = defaultdict(int)
cnt = 0
for a in A:
    for b in B:
        AB[a + b] += 1
    
for c in C:
    for d in D:
        if -(c + d) in AB:
            cnt += AB[-(c + d)]

print(cnt)