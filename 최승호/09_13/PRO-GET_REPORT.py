from collections import defaultdict


def solution(id_list, report, k):
    answer = {id:0 for id in id_list}
    reported = {id:set() for id in id_list}


    for r in report:
        user, reported_user= r.split()
        reported[reported_user].add(user)

    for reported_user, users in reported.items():
        if len(users) >= k:
            for user in users:
                answer[user] += 1

    return list(answer.values())