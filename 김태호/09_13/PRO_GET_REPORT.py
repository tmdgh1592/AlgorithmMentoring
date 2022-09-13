from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    res = defaultdict(set)
    cnt = defaultdict(int)
    
    for id in id_list:
        res[id]
        
    for r in set(report):
        a, b = r.split()
        res[a].add(b)
    
    for value in res.values():
        for v in value:
            cnt[v] += 1
    cnt = {key : val for key, val in cnt.items() if val >= k}

    for val in res.values():
        answer.append(len(set(cnt.keys()).intersection(val)))
    return answer