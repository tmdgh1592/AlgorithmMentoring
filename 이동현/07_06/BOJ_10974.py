MIS = lambda: map(int, input().rstrip().split())
n = int(input())
number = []
for i in range(n):
    number.append(i+1)
temp = []
def per():
    if len(temp) == n:
        print(*temp)
        return None
    for i in range(1,n+1):
        if i in temp:
            continue
        temp.append(i)
        per()
        temp.pop()
per()