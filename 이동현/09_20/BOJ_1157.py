from collections import defaultdict
string = list(input().upper())
# print(string)

d = defaultdict(int)

# for i in set(string):
#     d[i] = 0

for i in string:
    d[i] += 1

# print(d)

max = 0


res = sorted(d.items(), key=lambda x : -x[-1])
if len(res) >= 2 and res[0][1] == res[1][1]:
    print('?')
else:
    print(res[0][0])

