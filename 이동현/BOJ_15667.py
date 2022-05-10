MAXSIZE = 10101
k = int(input())
def fire(k):
    for i in range(0, MAXSIZE + 1):
        if k == 1 + i + i * i:
            return i
print(fire(k))