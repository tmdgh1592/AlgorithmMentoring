#dp로 접근하려 했으나.. count 때문에 어떻게 할지 몰라서 재귀를 통한 전수 조사로 노선 변경
import sys
sys.setrecursionlimit(1 << 14)
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
a = list(MIS())
a.insert(0,0)

max_size = 0

def nun(size, index, cnt):
    global max_size

    if cnt >= m or index == n:
        if max_size < size:
            max_size = size
        return None

    if index <= n - 1:
        nun(size + a[index + 1], index + 1 ,cnt + 1)
    
    if index <= n - 2:
        nun(size // 2 + a[index + 2], index + 2 ,cnt + 1)

nun(1, 0, 0)
print(max_size)
    
