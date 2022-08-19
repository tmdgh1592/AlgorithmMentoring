#왜 틀렸지..
n = int(input())
res = n
cnt = 0

while(1):
    if '666' in str(res):
        cnt += 1
        if cnt == n:
            break
    res += 1
print(res)
