import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
eggs = list()
for i in range(n):
    eggs.append(list(MIS()))

rst = 0

def hit(index):
    global rst
    if index == n:
        cnt = 0
        for i in range(n):
            if eggs[i][0] <= 0: cnt += 1
        if rst < cnt: rst = cnt
        return None

    broken = True
    for egg in range(n):
        if egg == index: continue
        if eggs[egg][0] > 0:
            broken = False
            break
        if broken == True:
            hit(n)
            return    
    
    #들고 있는 계란이 깨지는 경우
    if eggs[index][0] <= 0:
        hit(index + 1)

    for egg in range(n):
        if egg == index: continue
        if eggs[egg][0] <= 0: continue
        eggs[egg][0] -= eggs[index][1]
        eggs[index][0] -= eggs[egg][1]
        hit(index + 1)
        eggs[egg][0] += eggs[index][1]
        eggs[index][0] += eggs[egg][1]
hit(0)
print(rst)
