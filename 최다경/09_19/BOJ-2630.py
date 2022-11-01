import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
paper = [list(MIS()) for _ in range(n)]

def check(y, x, size):
    tmp = paper[y][x]
    for i in range(size):
        for j in range(size):
            if paper[i + y][j + x] != tmp:
                return False
    return True
blue = 0
white = 0
def rec(y, x, size):
    global white, blue
    if check(y, x, size):
        if paper[y][x] == 0: white += 1
        else: blue += 1 
        return None
    
    rec(y + size // 2, x, size // 2)
    rec(y, x + size // 2, size // 2)
    rec(y + size // 2, x + size // 2, size // 2)
    rec(y, x, size // 2)
    
rec(0, 0, n)
print(white)
print(blue)
    

